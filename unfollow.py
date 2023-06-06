import tweepy
from cred import *

auth = tweepy.OAuth1UserHandler(
   "API / Consumer Key here", "API / Consumer Secret here",
   "Access Token here", "Access Token Secret here"
)
api = tweepy.API(auth)


def unfollower():

    followers = api.get_follower_ids(screen_name=api.verify_credentials().screen_name)
    friends = api.get_friend_ids(screen_name=api.verify_credentials().screen_name)
    print("You follow:", len(friends))    
    
    for friend in friends[::-1]:
        if friend not in followers:
            api.destroy_friendship(user_id = friend)
        else:
            pass
        
    friends = api.get_friend_ids(screen_name=api.verify_credentials().screen_name)
    print("Now you're following:", len(friends))

unfollower()	