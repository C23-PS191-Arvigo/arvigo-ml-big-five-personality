# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EexcEbXLdZD6ibfqH185IRCpizz-WgNB
"""

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from joblib import dump
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer

# Mount Google Drive to access dataset
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Set up directory path
file_path = '/content/drive/MyDrive/Dataset Personality/data-final.csv'

# Read CSV file into a Pandas DataFrame
df = pd.read_csv(file_path, sep='\t')

# Drop columns from 51 onwards
df.drop(df.columns[50:], axis=1, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert all columns to integer
df = df.astype(int)

# Groups and Questions
ext_questions = {'EXT1' : 'I am the life of the party',
                 'EXT2' : 'I dont talk a lot',
                 'EXT3' : 'I feel comfortable around people',
                 'EXT4' : 'I keep in the background',
                 'EXT5' : 'I start conversations',
                 'EXT6' : 'I have little to say',
                 'EXT7' : 'I talk to a lot of different people at parties',
                 'EXT8' : 'I dont like to draw attention to myself',
                 'EXT9' : 'I dont mind being the center of attention',
                 'EXT10': 'I am quiet around strangers'}

est_questions = {'EST1' : 'I get stressed out easily',
                 'EST2' : 'I am relaxed most of the time',
                 'EST3' : 'I worry about things',
                 'EST4' : 'I seldom feel blue',
                 'EST5' : 'I am easily disturbed',
                 'EST6' : 'I get upset easily',
                 'EST7' : 'I change my mood a lot',
                 'EST8' : 'I have frequent mood swings',
                 'EST9' : 'I get irritated easily',
                 'EST10': 'I often feel blue'}

agr_questions = {'AGR1' : 'I feel little concern for others',
                 'AGR2' : 'I am interested in people',
                 'AGR3' : 'I insult people',
                 'AGR4' : 'I sympathize with others feelings',
                 'AGR5' : 'I am not interested in other peoples problems',
                 'AGR6' : 'I have a soft heart',
                 'AGR7' : 'I am not really interested in others',
                 'AGR8' : 'I take time out for others',
                 'AGR9' : 'I feel others emotions',
                 'AGR10': 'I make people feel at ease'}

csn_questions = {'CSN1' : 'I am always prepared',
                 'CSN2' : 'I leave my belongings around',
                 'CSN3' : 'I pay attention to details',
                 'CSN4' : 'I make a mess of things',
                 'CSN5' : 'I get chores done right away',
                 'CSN6' : 'I often forget to put things back in their proper place',
                 'CSN7' : 'I like order',
                 'CSN8' : 'I shirk my duties',
                 'CSN9' : 'I follow a schedule',
                 'CSN10' : 'I am exacting in my work'}

opn_questions = {'OPN1' : 'I have a rich vocabulary',
                 'OPN2' : 'I have difficulty understanding abstract ideas',
                 'OPN3' : 'I have a vivid imagination',
                 'OPN4' : 'I am not interested in abstract ideas',
                 'OPN5' : 'I have excellent ideas',
                 'OPN6' : 'I do not have a good imagination',
                 'OPN7' : 'I am quick to understand things',
                 'OPN8' : 'I use difficult words',
                 'OPN9' : 'I spend time reflecting on things',
                 'OPN10': 'I am full of ideas'}

# Group Names and Columns
EXT = [column for column in df if column.startswith('EXT')]
EST = [column for column in df if column.startswith('EST')]
AGR = [column for column in df if column.startswith('AGR')]
CSN = [column for column in df if column.startswith('CSN')]
OPN = [column for column in df if column.startswith('OPN')]

# Defining a function to visualize the questions and answers distribution
def vis_questions(groupname, questions, color):
    plt.figure(figsize=(40,60))
    for i in range(1, 11):
        plt.subplot(10,5,i)
        plt.hist(df[groupname[i-1]], bins=14, color= color, alpha=.5)
        plt.title(questions[groupname[i-1]], fontsize=18)

print('Q&As Related to Extroversion Personality')
vis_questions(EXT, ext_questions, 'orange')

print('Q&As Related to Neuroticism Personality')
vis_questions(EST, est_questions, 'pink')

print('Q&As Related to Agreeable Personality')
vis_questions(AGR, agr_questions, 'red')

print('Q&As Related to Conscientious Personality')
vis_questions(CSN, csn_questions, 'purple')

print('Q&As Related to Open Personality')
vis_questions(OPN, opn_questions, 'blue')

# Scale the data using MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
df_sample = df.iloc[:10000,:]
df_scaled = scaler.fit_transform(df_sample)
columns = df_sample.columns
df_scaled = pd.DataFrame(df_scaled, columns=columns)

# Visualize the elbow
kmeans = KMeans(n_init=10)
visualizer = KElbowVisualizer(kmeans, k=(2,10))
visualizer.fit(df_scaled)
visualizer.poof()

# Fit KMeans model to the data
kmeans = KMeans(n_clusters=5, n_init=100)
kmeans.fit(df)

# save model to joblib file
dump(kmeans, 'model_kmeans.joblib')

# Assign the clusters to each data point
cluster_labels = kmeans.labels_
df['cluster'] = cluster_labels
df.head()

# Group the DataFrame by the cluster labels and compute the mean of each column for each cluster
df = df.groupby('cluster').mean()

# Summing up the different questions groups
col_list = list(df)
ext = col_list[0:10]
est = col_list[10:20]
agr = col_list[20:30]
csn = col_list[30:40]
opn = col_list[40:50]

data_sums = pd.DataFrame()
data_sums['extroversion'] = df[ext].sum(axis=1)/10
data_sums['neurotic'] = df[est].sum(axis=1)/10
data_sums['agreeable'] = df[agr].sum(axis=1)/10
data_sums['conscientious'] = df[csn].sum(axis=1)/10
data_sums['open'] = df[opn].sum(axis=1)/10
data_sums['clusters'] = df.index
data_sums.groupby('clusters').mean()

# Visualizing the means for each cluster
dataclusters = data_sums.groupby('clusters').mean()
plt.figure(figsize=(22,3))
for i in range(0, 5):
    plt.subplot(1,5,i+1)
    plt.bar(dataclusters.columns, dataclusters.iloc[:, i], color='green', alpha=0.2)
    plt.plot(dataclusters.columns, dataclusters.iloc[:, i], color='blue')
    plt.title('Cluster ' + str(i))
    plt.xticks(rotation=45)
    plt.ylim(0,4);