import tweepy

class TwitterAuth():

    def __init__(self): 
        # == OAuth Authentication ==
        # == https://dev.twitter.com/apps (under "OAuth settings")
        self.consumerKey="hhIhCUOwVeY7rzHdlRoSTjNhN"
        self.consumerSecret="4FdQScnELAWr5xp4TvoDg6BKoeQ2JFXE4B5dPQJ0B9R2qYVRYV"
        self.accessToken="313808280-zww8PwqqucUcrSEIDg1tGOmLfuYe3ZjzLHgBmejR"
        self.accessTokenSecret="xMXV3EvHjx9fTphkXAOV6pMpCv53LK87s5BadXXiuYfIw"
        self._doOauth()

    def _doOauth(self):
        self.auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        self.auth.set_access_token(self.accessToken, self.accessTokenSecret)    

    def _getAPIObj(self):
        self.API = tweepy.API(self.auth)
        return self.API

    def _refreshAPI(self):
        self.auth = self._doOauth()
        





