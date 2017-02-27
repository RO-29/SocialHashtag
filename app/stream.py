import tweepy
import oauthsocial
import datetime
import traceback

class StreamSocial():

    def __init__(self):
        self.twitterApiObj, self.instaApiObj = oauthsocial.SocialAuth()._getAPIObj()

    def process_tweets(self, status,mode):
        result = {}
        media       = status.entities.get("media",[])
        includMedia = 0
        media_url   = ""
        if media:
            media_url   = media[0].get("media_url","")
            includMedia = 1

        result["mediaLink"] = media_url
        result["includMedia"] = includMedia
        result["content"] = status.text
        result["userDisplay"] = status.user.profile_image_url_https
        result["screenName"] = status.user.screen_name
        result["name"] = status.user.name
        result["displayFlag"] = mode
        result["time"] = (status.created_at +datetime.timedelta(hours = 5,minutes = 30)).strftime("%Y-%m-%d %H:%M:%S")
        result["linkOriginalPost"] = "https://twitter.com/{screen_name}/status/{id}".format(screen_name = result["screenName"], id = status.id)
        result["type"] = "tweet"
        return result,status.id

    def twitterSearch(self, search ,start_date, end_date, mode, location, sinceid, old_post, results_number):
        results = []
        api = self.twitterApiObj
        q ="#"+search+" since:"+start_date+" until:"+end_date
        try:
            cursor = tweepy.Cursor(api.search, q =q)
            if sinceid >0 and not old_post:
                cursor = tweepy.Cursor(api.search, q =q, since_id = sinceid)

            for status in cursor.items():
                status_process,last_id = self.process_tweets(status, mode)
                if last_id > sinceid:
                    sinceid = last_id
                results.append(status_process)
                if results_number and len(results) >= results_number:
                    break
        except:
            pass
        results.reverse()
        return results,sinceid


    def process_insta(self, status, mode):
        result = {}
        user = status.get("user",{})
        try:
            date_created = status.get("taken_at","")
            date_created = datetime.datetime.fromtimestamp(int(date_created)).strftime('%Y-%m-%d %H:%M:%S')
        except:
            date_created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            media_link = status["images"]["standard_resolution"]["url"]
        except:
            media_link = ""
            pass
        try:
            medias = status["image_versions"]["candidates"]
            media_link = medias[0]["url"]
        except:
            pass
        try:
            medias = status["image_versions2"]["candidates"]
            media_link = medias[0]["url"]
        except:
            pass

        try:
            caption = status["caption"]["text"]
        except:
            caption = ""

        result["mediaLink"]        = media_link
        result["includMedia"]      = 1
        result["content"]          = caption
        result["userDisplay"]      = user.get("profile_pic_url","")
        result["screenName"]       = user.get("username","")
        result["name"]             = user.get("full_name","")
        result["displayFlag"]      = mode
        result["time"]             = date_created
        result["linkOriginalPost"] = "https://www.instagram.com/p/{insta_post}/".format(insta_post = status.get("code",""))
        result["type"]             = "insta"
        return result

    def instaSearch(self, search, mode, location, sinceid, old_post, results_number):
        results      = []
        api          = self.instaApiObj
        search       = search.split("#")[1] if "#" in search else search
        search       = search.split(" ")[0]
        try:
            instaPosts = api.feed_tag(search)
        except:
            print traceback.format_exc()
        if "items" in instaPosts:
            posts = instaPosts["items"]
            try:
                for post in posts:
                    post_code = post["code"]
                    if old_post or ((not old_post) and post_code not in sinceid):
                        status_process = self.process_insta(post, mode)
                        results.append(status_process)
                    if post_code not in sinceid:
                        sinceid.append(post_code)
                    if results_number and (len(results) >= results_number):
                        break
            except:
                pass
        results.reverse()
        return results, sinceid


    def _getSearchResults(self, search,start_date, end_date, mode, location,type_search, sinceid,old_post, results_number):
        if type_search == "tweets":
            return self.twitterSearch(search,start_date, end_date, mode, location, sinceid,old_post,results_number)
        if type_search == "insta" and self.instaApiObj:
            return self.instaSearch(search, mode, location, sinceid, old_post, results_number)
        return [], 0
