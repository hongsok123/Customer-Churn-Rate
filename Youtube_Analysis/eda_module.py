import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec

def highest_subscribe(df):
  top10_channelsub = df[['creator_name', 'creator_gender','total_channel_subscriber']].groupby('creator_name').max().\
                        sort_values(by = 'total_channel_subscriber',ascending = False).head(10)
  top10_channelsub.reset_index(drop = False, inplace = True)
  gender_palette =  {'Male': 'moccasin', 'Female': 'gold', 'Company': 'orange'}
  plt.figure(figsize = (9,4))
  sns.barplot(x = 'creator_name',y = 'total_channel_subscriber', hue = 'creator_gender', palette = gender_palette, data =     top10_channelsub )
  plt.xticks(rotation = 45)
  plt.title('Top 10 Channels subscriber wise', color = 'black')
  plt.xlabel('Creator Name')
  plt.ylabel('Total Channel Subscriber')
  plt.legend(loc = 1)

def highest_views(df):
  top10_channelview = df[['creator_name','total_channel_views', 'creator_gender']].groupby('creator_name').max().\
                        sort_values(by = 'total_channel_views',ascending = False).head(10)
  top10_channelview.reset_index(drop = False, inplace = True)
  gender_palette = {'Male': 'moccasin', 'Female': 'gold', 'Company': 'orange'}
  plt.figure(figsize = (9,4))
  sns.barplot(x = 'creator_name',y = 'total_channel_views', hue = 'creator_gender', palette = gender_palette, data =     top10_channelview )
  plt.xticks(rotation = 45)
  plt.title('Top 10 Channels views wise', color = 'black')
  plt.xlabel('Creator Name')
  plt.ylabel('Total Channel with highest views')
  plt.legend(loc = 1)

def numberOfLike_byGen(df):
  gender_palette =  {'Male': 'moccasin', 'Female': 'gold', 'Company': 'orange'}
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 6), sharey=True)
  sns.barplot(x="creator_gender", y="no_of_likes", palette = gender_palette, data=df, ci = None, ax = ax1)
  ax1.set_xlabel("")
  ax1.set_ylabel("No of Likes")
  fig.suptitle('Gender Vs Likes')
  ax1.ticklabel_format(style='plain', axis='y')

  sns.barplot(x="creator_gender", y="no_of_likes", palette = gender_palette, data=df, ax = ax2)
  ax2.set_xlabel("")
  ax2.set_ylabel("No of Likes")
  ax2.ticklabel_format(style='plain', axis='y')
  fig.legend(loc = 1, handles=ax2.get_children()[0:3], labels=gender_palette.keys())
  
def avg_per_video(df) :
  cata_palette =  {'Supershort': '#8aacc8', 'Short': '#5d99c6', 'Medium': '#2286c3', 'Long':'#0077c2', 'SuperLong': '#0069c0'}
  plt.figure(figsize = (7,4))
  sns.barplot(x ="length_catagories", y = 'no_of_likes', data = df, ci = None, palette = cata_palette )
  plt.title('Average likes per Video Category', fontsize = 10)
  plt.xlabel('Video Cateogory')
  plt.ylabel('No of likes')
  plt.legend(('Supershort', 'Short', 'Meduim', 'Long', 'SuperLong'),
           loc= 1, shadow=True)

def video_quality_Like(df):
  
  quality_palette =  {"240p": "#4bacb8" , "360p":"#009faf", "480p": "#0095a8", "720p": "#008ba3","1080p" : "#007c91", "1440p" : "#006978", "2160p": "#005662"}
  fig, ax1= plt.subplots(1, figsize=(9, 6), sharey=True)
  sns.barplot(x="maximum_quality_of_the_video", y="no_of_likes", palette = quality_palette, data=df, ci = None, ax = ax1)
  ax1.set_xlabel("Maximumn Video Quality")
  ax1.set_ylabel("No of Likes")
  fig.suptitle("Number_of_Like VS Quality Video", fontsize = 10)
  ax1.ticklabel_format(style='plain', axis='y')
  fig.legend(loc = 1, handles=ax1.get_children()[0:8], labels=quality_palette.keys())
  
def video_quality_view(df):
  
  quality_palette =  {"240p": "#4bacb8" , "360p":"#009faf", "480p": "#0095a8", "720p": "#008ba3","1080p" : "#007c91", "1440p" : "#006978", "2160p": "#005662"}
  fig, ax1= plt.subplots(1, figsize=(9, 6), sharey=True)
  sns.barplot(x="maximum_quality_of_the_video", y="vid_view", palette = quality_palette, data=df, ci = None, ax = ax1)
  ax1.set_xlabel("Maximumn Video Quality")
  ax1.set_ylabel("Vid_View")
  fig.suptitle("Video_View VS Quality Video", fontsize = 10)
  ax1.ticklabel_format(style='plain', axis='y')
  fig.legend(loc = 1, handles=ax1.get_children()[0:8], labels=quality_palette.keys())