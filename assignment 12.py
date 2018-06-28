from twitterapi import Consumer_key,Consumer_secret,Access_token,Access_secret
import tweepy

oauth =tweepy.OAuthHandler(Consumer_key,Consumer_secret)
oauth.set_access_token(Access_token,Access_token)
api=tweepy.API(oauth)
print(api.search("#sanju"))
user=api.get_user('madhavahuja6')
print(user.screen_name)
print(user.followers_count)