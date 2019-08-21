import tweepy
import imp
import os
import csv

###########################################################################################################
# NOTE: I handle CSVs horribly. Hopefully their naming convention is straightforward and not too confusing.
###########################################################################################################

# Loads Twitter Start File
twitter = imp.load_source('twit', '/Users/lucas/OneDrive/Documents/SCHOOL/Programming/Python Scripts/Essential Scripts/start_twitter.py')
# Initiatizes API Call
api = twitter.client

# Returns list of all followers for provided twitter id
# id: Twitter id
def get_followers(id):
    followers = []
    for item in tweepy.Cursor(api.followers_ids, id).items():
    	followers.append(item)
    return followers

# Returns list of all users who the provided id follows
# id: Twitter id
def get_following(id):
    follows = []
    for item in tweepy.Cursor(api.friends_ids, id).items():
    	follows.append(item)
    return follows


# Grabs information from a list of twiiter ids
# followers: List of twitter ids
# start: Index in id list to start from (Useful in case of errors)
# fileName: Name for stored csv file (NOTE: function can't append csv files)
def get_follow_info(followers, start = 0, fileName = 'twitter_data.csv'):
    with open(fileName, 'w') as f:
        my_writer = csv.DictWriter(f, fieldnames = ("Screen Name", "Follower Count","Total Tweets","Type"),lineterminator = '\n')
        my_writer.writeheader()
        stop=len(followers)

        # Loops through twitter ids

        for i in range(start,stop):
            # Creates user object
            try:
                user_call = api.get_user(followers[i])
            except:
                pass
            # Gathers user stats
            s_name = user_call.screen_name
            f_count = user_call.followers_count
            s_count = user_call.statuses_count

            # Checks follower count to determine type lable

            if f_count < 100:
                my_writer.writerow({"Screen Name":s_name, "Follower Count":f_count,"Total Tweets":s_count,"Type":"Layman"})
            elif f_count < 1000:
                my_writer.writerow({"Screen Name":s_name, "Follower Count":f_count,"Total Tweets":s_count,"Type":"Expert"})
            else:
                my_writer.writerow({"Screen Name":s_name, "Follower Count":f_count,"Total Tweets":s_count,"Type":"Celebrity"})
            print("Follower %d of %d added"%(i + 1,stop))
    return

# Grabs follower lists from a list of twitter ids
# followers: List of twitter ids
# start: Index in id list to start from (Useful in case of errors)
# fileName: Name for stored csv file (NOTE: function can't append csv files)
# f: Whether you want followers or following (Seems like a lazy way to reuse code)
def get_all_follow(followers, start = 0, fileName = 'twitter_data.csv',f=True):
    with open(fileName, 'w') as f:
        my_writer = csv.writer(f,lineterminator = '\n')
        stop = len(followers)

        # Loops through twitter id's
        for i in range(start,stop):

            # Excludes Celebrity
            if followers[i]['Type'] == 'Celebrity':
                print("Excluding followers of Celebrity %d of %d"%(i + 1,stop))
                pass
            # Tries to get follower list
            else:
                try:
                    # Checks whether it wants followers or following
                    if f == True:
                        follows_list=get_followers(followers[i]["Screen Name"])
                    else:
                        follows_list=get_following(followers[i]["Screen Name"])
            # Catches privacy settings/other errors
                except:
                    print("Unable to add followers of %d of %d"%(i  +1,stop))
                    pass
            # Writes list to csv file
                for j in follows_list:
                    my_writer.writerow([j])
                print("Added followers of %d of %d"%(i + 1,stop))
    return


# Finds the max item in a list (I made this due to how I handled CSV's and data (i.e. very poorly))
# item: list of follower info
# count_type: whether to count followers or tweets
def get_max(item, count_type = 'f'):
    # Checks what aspect to count
    if(count_type == 'f'):
        t = "Follower Count"
    else:
        t = "Total Tweets"
    # The max amount
    maxb = 0
    # Loops through each item in the list
    for i in range(1,len(item)):
        # Catches small exception due to header when reading csv (lazy fix)
        try:
            # Checks if item is greater than previous max
            if int(item[i][t]) > maxb:
                # Sets item as new max
                maxb=int(item[i][t])
                maxName= item[i]['Screen Name']
        except:
            pass
    return [maxName,maxb]


# Extracts follower information from csv files
# fileName: name of the csv file
def get_followers_from_csv(fileName):
    with open(fileName, 'r') as f:
      my_reader = csv.DictReader(f,fieldnames = ("Screen Name", "Follower Count","Total Tweets","Type"),lineterminator = '\n')
      results = []
      for row in my_reader:
        results.append(row)
    return results

# Extracts follower ids from csv files
# fileName: name of the csv file
def get_follow_id_from_csv(fileName):
    with open(fileName, 'r') as f:
      my_reader = csv.reader(f,lineterminator = '\n')
      results = []
      for row in my_reader:
        results.append(row[0])
    return results



# Grabs WUSTL followers
wustl_followers=get_followers('WUSTL')
# Grabs users who WUSTL is following
wustl_following=get_following('WUSTL')

# Grabs information from above lists
get_follow_info(wustl_following,fileName='wustl_following_twitter_data.csv')
get_follow_info(wustl_followers,fileName='wustl_followers_twitter_data.csv')
# Restarting due to windows update
get_follow_info(wustl_followers,fileName='wustl_followers_twitter_data_part2.csv',start=14181)

# Reads results from CSVs
wustl_followers_info=get_followers_from_csv('wustl_followers_twitter_data.csv')
wustl_followers_info.extend(get_followers_from_csv('wustl_followers_twitter_data_part2.csv'))
wustl_following_info=get_followers_from_csv('wustl_following_twitter_data.csv')

# Finds who has the greatest number of total tweets
get_max(wustl_followers_info,count_type='t')
# Finds who has the greatest number of followers
get_max(wustl_followers_info)

# Finds who has the greatest number of followers
get_max(wustl_following_info)


# Crudely sorts who wustl follows (Really should use pandas)
celebrties=[]
layman=[]
expert=[]
for i in range(1,len(wustl_following_info)):
    if wustl_following_info[i]['Type'] == 'Layman':
        layman.append(wustl_following_info[i])
    elif wustl_following_info[i]['Type'] == 'Expert':
        expert.append(wustl_following_info[i])
    else:
        celebrties.append(wustl_following_info[i])

# Finds max for each group
get_max(celebrties,count_type='t')
get_max(layman,count_type='t')
get_max(expert,count_type='t')



# Grabs WUSTLPoliSci followers
wustlPoliSci_followers=get_followers('WUSTLPoliSci')
# Grabs users who WUSTLPoliSci is following
wustlPoliSci_following=get_following('WUSTLPoliSci')

# Grabs information from above lists
get_follow_info(wustlPoliSci_followers,fileName='WUSTLPoliSci_follower_twitter_data.csv')
get_follow_info(wustlPoliSci_following,fileName='WUSTLPoliSci_following_twitter_data.csv')


# Reads results from CSV
wustlPoliSci_followers_info=get_followers_from_csv('WUSTLPoliSci_follower_twitter_data.csv')
wustlPoliSci_following_info=get_followers_from_csv('WUSTLPoliSci_following_twitter_data.csv')


# Grabs followers of followers/following
get_all_follow(wustlPoliSci_followers_info,fileName='wustlpolisci_all_follower_ids_twitter_data.csv')
get_all_follow(wustlPoliSci_following_info,fileName='wustlpolisci_all_following_ids_twitter_data.csv',f=False)


###################################################################################################################
# NOTE: I didn't have time to run the rest of the homework. It should work just fine, but will take quite some time
###################################################################################################################


# Reads IDs from CSV
tempList=get_follow_id_from_csv('wustlpolisci_all_follower_ids_twitter_data.csv')
# Grabs information from above list
wustlpolisci_all_followers_info=get_follow_info(tempList,fileName='wustlpolisci_all_following_twitter_data.csv')


# Reads IDs from CSV
tempList=get_follow_id_from_csv('wustlpolisci_all_following_ids_twitter_data.csv')
# Grabs information from above list
wustlpolisci_all_following_info=get_follow_info(tempList,fileName='wustlpolisci_all_following_twitter_data.csv')

# Finds greatest number of tweets of followers
get_max(wustlpolisci_all_followers_info,count_type='t')
# Finds greatest number of tweets of users who are followed
get_max(wustlpolisci_all_following_info,count_type='t')
