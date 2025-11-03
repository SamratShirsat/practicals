import pandas as pd

df = pd.read_csv("YoutubeCommentsDataSet.csv")
print(df.columns)

# #Dropping the irrelevant columns
# columns_to_drop = [
#  'channel_username', 'channel_id', 'video_id', 'video_title',
#  'comment_id', 'author', 'published_at',
#  'label_sentiment', 'label_toxicity'
# ]
# df = df.drop(columns=columns_to_drop)
# print(df.columns)
# #Checking the null values and removing them
# print(df.isnull().sum())
# df = df[df['comment_text'].notna()]
# df = df[df['language'].notna()]
# print(df.isnull().sum()) 

# #Plotting the boxplot to identify the outliers
# plt.figure(figsize=(8, 4))
# plt.boxplot(df['like_count'], vert=False)
# plt.title('Boxplot of Like Count')
# plt.xlabel('Like Count')
# plt.grid(True)
# plt.show()
# plt.figure(figsize=(8, 4))
# plt.boxplot(df['like_count'], vert=False)
# plt.title('Boxplot of Reply Count')
# plt.xlabel('Reply Count')
# plt.grid(True) 
# plt.show() 

# #Removing the outliers
# df = df[df['like_count'] <= 5000]
# df = df[df['reply_count'] <= 500]
# print("Remaining rows:", df.shape[0])
# #Filtering and removing the values other than spam and not spam df
# df[df['label_spam'].isin(['spam', 'not spam'])]
# df['spam_label'] = df['label_spam'].map({'not spam': 0, 'spam': 1}) 

# heatmap_data = df[['like_count', 'reply_count', 'spam_label']]
# correlation = heatmap_data.corr()
# plt.figure(figsize=(6, 4))
# plt.imshow(correlation, cmap='coolwarm')
# plt.colorbar()
# plt.xticks(range(len(correlation.columns)), correlation.columns) 

# plt.yticks(range(len(correlation.columns)), correlation.columns)
# plt.title("Correlation Heatmap")
# plt.tight_layout()
# plt.show() 

# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as px
# import numpy as np
# df = pd.read_csv('anime_data.csv') 

# import re
# #Clean airing date, duration and demographic
# df['Aired_from'] = df['Aired'].str.extract(r'^(.*) to')[0]
# df['Aired_from'] = pd.to_datetime(df['Aired_from'])
# df['Duration_min'] = df['Duration'].str.extract(r'(\d+)').astype(float)
# df['Demographic'] = df['Demographic'].str.replace(r'(\w+)\1', r'\1',
# regex=True)
# # Extract broadcast day
# df['Broadcast_Day'] = df['Broadcast'].str.extract(r'(\w+days?)')
# # Extract time (e.g., "23:00")
# df['Broadcast_Time'] = df['Broadcast'].str.extract(r'(\d{2}:\d{2})')
# # Fix repeated genre words
# def clean_genres(text):
#  if pd.isna(text):
#      return text
#  return re.sub(r'(\w+)\1', r'\1', text)
# # Apply the function to the 'Genres' column
# df['Genres'] = df['Genres'].apply(clean_genres) 

# df['Genres'] = df['Genres'].str.split(', ')
# df['Producers'] = df['Producers'].str.split(', ')
# df['Studios'] = df['Studios'].str.split(', ')
# df['Rating'] = df['Rating'].str.extract(r'^(.*?)(?:\s*-|$)')[0].str.strip()
# df = df[df['Episodes'] != 'Unknown']
# df['Episodes'] = df['Episodes'].astype(int)
# columns_to_drop = ['Description', 'Synonyms', 'Japanese', 'English','Licensors', 'Members', 'Broadcast', 'Aired', 'Duration']
# df = df.drop(columns=columns_to_drop)
# df.head() 

# columns_to_analyze = ['Score', 'Rank', 'Episodes', "Duration_min"]
# desc_stats = df[columns_to_analyze].agg(['mean', 'median'])
# mode_stats = df[columns_to_analyze].mode().iloc[0]
# print(desc_stats)
# print(mode_stats)
# for col in columns_to_analyze:
#  mean = df[col].mean()
#  median = df[col].median()
#  if abs(mean - median) < 1:
#     print(f"{col}: Symmetric (mean ≈ median)")
#  elif mean > median:
#     print(f"{col}: Right-skewed (mean > median)")
#  else:
#      print(f"{col}: Left-skewed (mean < median)") 

# sns.countplot(x='Type', data=df)
# plt.title("Anime Count by Type")
# plt.show()
# pd.crosstab(df['Demographic'], df['Rating']).plot(kind='bar',
# stacked=True)
# plt.title("Stacked Bar: Demographic vs Rating")
# plt.ylabel("Count")
# plt.show() 

# # plt.figure(figsize=(30, 15))
# sns.histplot(df['Type'], bins=20 )
# plt.title("Distribution of Episodes")
# plt.show() 
# sns.scatterplot(x='Score', y='Popularity', hue='Type', data=df)
# plt.title("Score vs Popularity by Type")
# plt.show() 
# sns.boxplot(x='Broadcast_Day', y='Score', data=df)
# plt.title("Score by Broadcast Day")
# plt.show() 
# df['Year'] = pd.to_datetime(df['Aired_from']).dt.year
# df['Year'].value_counts().sort_index().plot(kind='line')
# plt.title("Anime Releases Over Time")
# plt.xlabel("Year")
# plt.ylabel("Number of Anime")
# plt.show() 
# sns.violinplot(x='Rating', y='Episodes', data=df)
# plt.title("Episodes by Rating")
# plt.show() 

# sns.swarmplot(x='Type', y='Score', data=df)
# plt.title("Score Distribution by Type")
# plt.show() 