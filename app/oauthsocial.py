import tweepy

class TwitterAuth():

    def __init__(self): 
        
        #Twitter Tokens
        # == OAuth Authentication ==
        # == https://dev.twitter.com/apps (under "OAuth settings")
        self.consumerKeyTwitter       = "hhIhCUOwVeY7rzHdlRoSTjNhN"
        self.consumerSecretTwitter    = "4FdQScnELAWr5xp4TvoDg6BKoeQ2JFXE4B5dPQJ0B9R2qYVRYV"
        self.accessTokenTwitter       = "313808280-zww8PwqqucUcrSEIDg1tGOmLfuYe3ZjzLHgBmejR"
        self.accessTokenSecretTwitter = "xMXV3EvHjx9fTphkXAOV6pMpCv53LK87s5BadXXiuYfIw"
        
        #Insta Tokens
        #How to get?
        #https://www.instagram.com/oauth/authorize/?client_id=68926847741d41d082fb967e281c3fd3&redirect_uri=http://46.101.135.163:5000/&response_type=token&scope=public_content
        self.instaCLientID   = "68926847741d41d082fb967e281c3fd3"
        self.accessTokenInsta = "350728463.6892684.b52e38823bee41cc9338b4cad1bbfea4"

        self._doOauth()

    def _doOauth(self):
        self.authTwitter = tweepy.OAuthHandler(self.consumerKeyTwitter, self.consumerSecretTwitter)
        self.authTwitter.set_access_token(self.accessTokenTwitter, self.accessTokenSecretTwitter)    

    def _getAPIObj(self):
        self.twitterAPI = tweepy.API(self.authTwitter)
        return self.twitterAPI, self.accessTokenInsta

    def _refreshAPI(self):
        self.auth = self._doOauth()






