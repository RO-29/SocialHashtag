from __future__ import absolute_import, print_function

import tweepy



class TwitterAuth():

    def __init__(self): 
    # == OAuth Authentication ==
    # == https://dev.twitter.com/apps (under "OAuth settings")
    self.consumerKey="hhIhCUOwVeY7rzHdlRoSTjNhN"
    self.consumerSecret="4FdQScnELAWr5xp4TvoDg6BKoeQ2JFXE4B5dPQJ0B9R2qYVRYV"

    self.accessToken="313808280-zww8PwqqucUcrSEIDg1tGOmLfuYe3ZjzLHgBmejR"
    self.accessTokenSecret="xMXV3EvHjx9fTphkXAOV6pMpCv53LK87s5BadXXiuYfIw"

    def _doOauth(self):
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)    
        return auth

class TwiiterSearch():

    def __init__(self):
        self.apiObj = tweepy.API(TwitterAuth()._doOauth())

    def _getSearchResult(self):
        return



