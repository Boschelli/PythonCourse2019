import tweepy
import imp
import os
import csv


twitter = imp.load_source('twit', '/Users/lucas/OneDrive/Documents/SCHOOL/Programming/Python Scripts/Essential Scripts/start_twitter.py')
api = twitter.client


def get_followers(id):
    followers = []
    for item in tweepy.Cursor(api.followers_ids, id).items():
    	followers.append(item)
    return followers

def get_following():
    follows = []
    for item in tweepy.Cursor(api.friends_ids, id).items():
    	follows.append(item)
    return follows

def get_follow_info(followers,start=0,fileName='twitter_data.csv'):
    with open(fileName, 'w') as f:
        my_writer = csv.DictWriter(f, fieldnames = ("Screen Name", "Follower Count","Total Tweets","Type"),lineterminator = '\n')
        my_writer.writeheader()
        stop=len(followers)
        follower_summary={"Layman":{},"Expert":{},"Celebrity":{}}
        for i in range(start,stop):
            try:
                user_call = api.get_user(followers[i])
            except:
                pass
            s_name = user_call.screen_name
            f_count = user_call.followers_count
            s_count = user_call.statuses_count
            if f_count < 100:
                follower_summary["Layman"][s_name]=[f_count,s_count]
                my_writer.writerow({"Screen Name":s_name, "Follower Count":f_count,"Total Tweets":s_count,"Type":"Layman"})
            elif f_count < 1000:
                follower_summary["Expert"][s_name]=[f_count,s_count]
                my_writer.writerow({"Screen Name":s_name, "Follower Count":f_count,"Total Tweets":s_count,"Type":"Expert"})
            else:
                follower_summary["Celebrity"][s_name]=[f_count,s_count]
                my_writer.writerow({"Screen Name":s_name, "Follower Count":f_count,"Total Tweets":s_count,"Type":"Celebrity"})
            print("User %d of %d added"%(i+1,stop))
    return follower_summary


def get_max(item,count_type='f'):
    if(count_type=='f'):
        t=0
    else:
        t=1
    maxb=0
    for i in item:
        if item[i][t] >maxb:
            maxb=item[i][t]
            maxName= i
    return [maxName,maxb]


wustl_followers=get_followers('WUSTL')
wustl_following=get_following('WUSTL')

test01=get_followers('WUSTLPoliSci')
test02=get_follow_info(test01,fileName='WUSTLPoliSci_twitter_data.csv')

for type in test02:
    print(get_max(test02[type]))
