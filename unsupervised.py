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

def findChannel(cz) :
    features, channels = readFeatures()
    categories = cluster(features,cz)
    streams_dict = {}
    for i in range(len(channels)):
        channel = channels[i]
        category = categories[i]
        if category not in streams_dict:
            streams_dict[category] = []
        streams_dict[category].append(channel)
        # print(category)
        # print(channel)
    return streams_dict

def cluster(features, clustersize) :
    kmeans = KMeans(n_clusters=clustersize)
    kmeans.fit(features)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    # print(centroids)
    return labels

def combineClusters():
    counter = 0
    features, channels = readFeatures()
    print("number of channels: {}".format(len(channels)))
    clusters8 = findChannel(8)
    clusters9 = findChannel(9)
    clusters10 = findChannel(10)
    for cluster8 in clusters8.itervalues() :
        # print cluster8
        cluster8s = set(cluster8)
        for cluster9 in clusters9.itervalues() :
            cluster9s = set(cluster9)
            for cluster10 in clusters10.itervalues() :
                cluster10s = set(cluster10)
                intersect = cluster8s.intersection(cluster9s).intersection(cluster10s)
                if len(intersect) > 1:
                    print ("Intersection {}".format([item.encode("utf-8") for item in list(intersect)]))
    # for i in range(len(channels)):
    #     cnm = channels[i]
    #     c8m = clusters8[i]
    #     c9m = clusters9[i]
    #     c10m = clusters10[i]
    #     for j in range(len(channels)):
    #         cn = channels[j]
    #         c8 = clusters8[j]
    #         c9 = clusters9[j]
    #         c10 = clusters10[j]
    #         if cn != cnm and c8m == c8 and c9m == c9 and c10m == c10 :
    #             counter+=1
    #             print ("{} - {}").format(cn,cnm)
    # print (counter)

# findChannel()

combineClusters()
