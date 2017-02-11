import tweepy
import oauthsocial
import datetime

class StreamSocial():

    def __init__(self):
        self.twitterApiObj, self.instaAccessToken = oauthsocial.TwitterAuth()._getAPIObj()

    def process_tweets(self, status,mode):
        result = {}
        result["mediaLink"] = ""
        result["includMedia"] = 0
        result["content"] = status.text
        result["userDisplay"] = status.user.profile_image_url_https
        result["screenName"] = status.user.screen_name
        result["name"] = status.user.name
        result["displayFlag"] = mode
        result["time"] = (status.created_at +datetime.timedelta(hours = 5,minutes = 30)).strftime("%Y-%m-%d %H:%M:%S")
        result["linkOriginalPost"] = "https://twitter.com/{screen_name}/status/{id}".format(screen_name = result["screenName"], id = status.id)
        result["type"] = "tweet"
        return result,status.id
  
    def twitterSearch(self, search ,start_date, end_date, mode, location, sinceid, old_post):
        results = []
        api = self.twitterApiObj
        q ="#"+search+" since:"+start_date+" until:"+end_date
        cursor = tweepy.Cursor(api.search, q =q)
        if sinceid >0 and not old_post:
            cursor = tweepy.Cursor(api.search, q =q, since_id = sinceid)

        for status in cursor.items():
            status_process,last_id = self.process_tweets(status, mode)
            if last_id > sinceid:
                sinceid = last_id
            results.append(status_process)

        return results,sinceid
        
    def _getSearchResults(self, search,start_date, end_date, mode, location,type_search, sinceid,old_post):
        if type_search == "tweets":
            return self.twitterSearch(search,start_date, end_date, mode, location, sinceid,old_post)
        return [], 0


