import csv
import os
import json

import numpy as np
from sklearn.cluster import KMeans

# Name of the CSV file
filename = 'data/features.csv'

# Check if the csv file exists and creates it when it does not
exists = os.path.exists(filename)



# If more than
# x = [1, 5, 1.5, 8, 1, 9]
# y = [2, 8, 1.8, 8, 0.6, 11]
# plt.scatter(x,y)
# plt.show()
# X = np.array([[1, 2],
#               [5, 8],
#               [1.5, 1.8],
#               [8, 8],
#               [1, 0.6],
#               [9, 11]])

def readFeatures() :
    # with open('data/data.csv') as csvfile:
    # 	reader = csv.DictReader(csvfile)
    # 	for row in reader:
    # 		channel = row['channel']
    # 		message = row['message']
    # 		if channel not in messages:
    # 			messages[channel] = []
    # 		messages[channel].append(message)
    #
    X = []
    channels = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            channels.append(row['channel'])
            distinct_chatters_min= row['distinct_chatters/min']
            emote_min	= row['emote/min']
            msg_min	= row['msg/min']
            average_length_msg= row['average_length_msg']
            X.append([distinct_chatters_min,emote_min,msg_min,average_length_msg])
        return np.array(X), np.array(channels)

def findChannel() :
    features, channels = readFeatures()
    categories = cluster(features,10)
    streams_dict = {}
    for i in range(len(channels)):
        channel = channels[i]
        category = categories[i]
        if category not in streams_dict:
            streams_dict[category] = []
        streams_dict[category].append(channel)
        # print(category)
        # print(channel)
    print streams_dict

def cluster(features, clustersize) :
    kmeans = KMeans(n_clusters=clustersize)
    kmeans.fit(features)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    # print(centroids)
    return labels

def clusters():
    clusters8 = json.load(open('data/unsupervised_8_groups.json'))
    clusters9 = json.load(open('data/unsupervised_9_groups.json'))
    clusters10 = json.load(open('data/unsupervised_10_groups.json'))
    


# findChannel()
combineClusters()
