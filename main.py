"""
This program utilizes the Instaloader Python Package to manage your Instagram account. 
There is a lot more functionality on Instaloader, but this script is meant to be easy to run for those without coding knowledge!
Instaloader GitHub: https://github.com/instaloader

BEFORE YOU RUN THIS SCRIPT, follow the instructions in the README file.
"""

import instaloader
import pandas as pd

loader = instaloader.Instaloader()
USERNAME = input("Enter the name of your instagram account: ")
loader.load_session_from_file(USERNAME)
profile = instaloader.Profile.from_username(loader.context,
                                            USERNAME)

# Import our basic dataframes
df_followers = pd.DataFrame(columns=['Followers'])
df_following = pd.DataFrame(columns=['Following'])
df_list1 = pd.DataFrame(columns=['list1'])
df_list2 = pd.DataFrame(columns=['list2'])

# Get Followers 
followers = profile.get_followers()
er_list = []
for follower in followers:
    er_list.append(follower.username)
df_followers['Followers'] = er_list

# Get Following
followees = profile.get_followees()
ee_list = []
for followee in followees:
    ee_list.append(followee.username)
df_following['Following'] = ee_list

# Get accounts who you follow, but don't follow you
list1 = []
for followee in ee_list:
    if followee in er_list:
        continue
    else:
        list1.append(followee)
df_list1['list1'] = list1

# Get accounts who follow you, but you don't follow
list2 = []
for follower in er_list:
    if follower in ee_list:
        continue
    else:
        list2.append(follower)
df_list2['list2'] = list2

# Export everything to .csv files
df_followers.to_csv("followers.csv")
df_following.to_csv("following.csv")
df_list1.to_csv("list1.csv")
df_list2.to_csv("list2.csv")