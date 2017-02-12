import tweepy
import json
import datetime
import os
import instagram_private_api as app_api


class SocialAuth():

    def onlogin_callback(self,api, new_settings_file):
    cache_settings = api.settings
    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, indent=2)
        print('SAVED: %s' % new_settings_file)


    def instaLogin(self):
        #pip install git+ssh://git@github.com/ping/instagram_private_api.git@1.0.9
        print('Insta Client version: %s' % app_api.__version__)
        api = None
        settings_file =self.settings_file_insta
        try:
            if not os.path.isfile(settings_file):
                # settings file does not exist
                print('Unable to find file: %s' % settings_file)
                # login new
                api = app_api.Client(
                    self.InstaUsername, se;f.InstaPassword,
                    on_login=lambda x: self.onlogin_callback(x, settings_file))
            else:
                with open(settings_file) as file_data:
                    cached_settings = json.load(file_data)
                print('Reusing settings: %s' % settings_file)

                # reuse auth settings
                api = app_api.Client(
                    args.username, args.password,
                    settings=cached_settings)

        except (app_api.ClientCookieExpiredError, app_api.ClientLoginRequiredError) as e:
            print('ClientCookieExpiredError/ClientLoginRequiredError: %s' % e)
            # Login expired
            # Do relogin but use default ua, keys and such
            api = app_api.Client(
                args.username, args.password,
                on_login=lambda x: self.onlogin_callback(x, settings_file))

        except app_api.ClientLoginError as e:
            print('ClientLoginError %s' % e)
            pass
        except app_api.ClientError as e:
            print('ClientError %s (Code: %d, Response: %s)' % (e.msg, e.code, e.error_response))
            pass
        except Exception as e:
            print('Unexpected Exception: %s' % e)
            pass

        # Show when login expires
        cookie_expiry = api.cookie_jar.expires_earliest
        print('Cookie Expiry: %s' % datetime.datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ'))
        return api


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
        
        #Todo Change this
        self.InstaUsername        = "rohit.sync"
        self.InstaPassword        = "rohit2929_s"
        self.settings_file_insta  = "insta_settings.txt"

        self._doOauth()

    def _doOauth(self):
        self.authTwitter = tweepy.OAuthHandler(self.consumerKeyTwitter, self.consumerSecretTwitter)
        self.authTwitter.set_access_token(self.accessTokenTwitter, self.accessTokenSecretTwitter)    

    def _getAPIObj(self):
        self.twitterAPI = tweepy.API(self.authTwitter)
        self.instaAPI = self.instaLogin()
        return self.twitterAPI, self.instaAPI

    def _refreshAPI(self):
        self.auth = self._doOauth()






