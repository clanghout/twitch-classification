import csv
import os
import psycopg2
import argparse
import urllib2
import json
import random
# 
import numpy as np
from sklearn import svm
import itertools

emoteJson = json.loads(urllib2.urlopen("https://twitchemotes.com/api_cache/v2/global.json").read())
emoteString = "(%s)" % ('|'.join(emoteJson['emotes'].keys()))

parser = argparse.ArgumentParser(description='Retrieve the data from the database and store it in a csv file')
parser.add_argument('-u', '--user', help='The username for the postgress database')
parser.add_argument('-p', '--password', help='The password for the database')
args = parser.parse_args()

# Name of the CSV file
filename = 'data/data.csv'

emote_per_minute_perchannel_query = """
SELECT viewers.rchannel, AVG(viewers.emotePerMinute) as averageEmotePerMinute
FROM
 (SELECT channel as rchannel, COUNT(message) as emotePerMinute
 FROM chat_log
     WHERE message ~* '{}'
 GROUP BY date_trunc('minute', to_timestamp(date/1000)), channel) viewers
GROUP BY viewers.rchannel
ORDER BY averageEmotePerMinute;
""".format(emoteString)

# The query for the database
query = "SELECT channel, sender, date, message FROM chat_log"


msg_per_minute_per_channel_query = """
SELECT rchannel, AVG(a.rcount)
FROM
  	(SELECT channel as rchannel, COUNT(*) as rcount
    FROM chat_log
    GROUP BY date_trunc('minute', to_timestamp(date/1000)), channel) a
GROUP BY a.rchannel
"""

average_length_msg_per_channel_query = """
SELECT channel, AVG(char_length(message))
FROM chat_log
GROUP BY channel
"""

amount_distinct_chatters_query = """
SELECT channel, COUNT(DISTINCT sender)
FROM chat_log
GROUP BY channel
"""
distinct_chatters_per_minute_query = """
SELECT viewers.rchannel, AVG(viewers.distinctsenders)
FROM
	(SELECT channel as rchannel, COUNT(DISTINCT sender) as distinctsenders
	FROM chat_log
	GROUP BY date_trunc('minute', to_timestamp(date/1000)), channel) viewers
GROUP BY viewers.rchannel
"""

# Get the label dictionary
label_dict = {}
with open('label_dictionary.txt') as f:
	for line in f:
		dat = line.split()
		key = dat[0]
		val = ' '.join(dat[1:])
		label_dict[key] = val

# Get the database connection
try:
	conn = psycopg2.connect("""dbname='twitch'
	                           user='%s'
	                           host='localhost'
	                           password='%s'""" % (args.user, args.password))
except:
	print("Unable to connect to the database")

def executeQuery(query, entries, features):
	cur.execute(query)

	for result in cur.fetchall():
		if result[0] not in entries:
			entries[result[0]] = []
		entries[result[0]].append(result[1])
	features += 1

	for items in entries.itervalues():
		if len(items) != features:
			items.append(0)

	return features

# Name of the CSV file
filename = 'data/features.csv'

# Check if the csv file exists and creates it when it does not
exists = os.path.exists(filename)
f = open(filename, 'w')
writer = csv.DictWriter(f, fieldnames=['channel', 'distinct_chatters/min', 'emote/min', 'msg/min', 'average_length_msg'])
writer.writeheader()

cur = conn.cursor()

# ---- 
features = [
	'distinct_chatters/min',
	'emote/min', 
	'msg/min', 
	'average_length_msg'
]

results_dict = {}
counter = executeQuery(distinct_chatters_per_minute_query, results_dict, 0)
counter = executeQuery(emote_per_minute_perchannel_query, results_dict, counter)
counter = executeQuery(msg_per_minute_per_channel_query, results_dict, counter)
counter = executeQuery(average_length_msg_per_channel_query, results_dict, counter)

for channel, features_results in results_dict.iteritems():
    writer.writerow({
        'channel': channel,
        'distinct_chatters/min': features_results[0],
        'emote/min': features_results[1], 
        'msg/min': features_results[2], 
        'average_length_msg': features_results[3]
    })

categories = set([])
cates = {}
count = 0
labels = []
for channel in results_dict.iterkeys():
	if label_dict[channel] not in cates:
		cates[label_dict[channel]] = { 
			'channels': [channel], 
			'index': count 
		}
		count += 1
	else:
		cates[label_dict[channel]]['channels'].append(channel)
	labels.append(cates[label_dict[channel]]['index'])

def findCategory(index):
	for key, values in cates.iteritems():
		if values['index'] == index:
			return key

def getCategoryIndex(category):
	return cates[category]['index']

for i in range(2, len(features) + 1):
	for combination in set(itertools.combinations(features, i)):
		print combination
		# counter = executeQuery(features[combination[0]], results_dict, 0)
		# for feature in combination[1:]:
		# 	counter = executeQuery(features[feature], results_dict, counter)
		# counter = executeQuery(msg_per_minute_per_channel_query, results_dict, counter)
		# counter = executeQuery(average_length_msg_per_channel_query, results_dict, counter)

			# categories.add(label_dict[channel])

		X = np.array([[sample_feature for idx, sample_feature in enumerate(sample) if idx in [features.index(combi) for combi in combination]] for sample in results_dict.itervalues()])

		clf = svm.SVC(kernel='poly', C = 1.0)
		clf.fit(X,labels)

		# print list(cates.iterkeys())

		with open('data/testfeatures.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			results = []
			bla = list(reader)
			for row in bla:
				# print row['channel']
				prediction = clf.predict(np.array([row[f] for f in combination]).reshape(1, -1))
				# print "{} {} {}".format(prediction, findCategory(prediction[0]), label_dict[row['channel']] == findCategory(prediction[0]))
				results.append(label_dict[row['channel']] == findCategory(prediction[0]))
			print float(sum(results))/len(results)

# f.close()
