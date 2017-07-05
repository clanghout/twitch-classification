import csv
import os
import psycopg2
import argparse
import urllib2
import json

emoteJson = json.loads(urllib2.urlopen("https://twitchemotes.com/api_cache/v2/global.json").read())
emoteString = "(%s)" % ('|'.join(emoteJson['emotes'].keys()))

print emoteString

parser = argparse.ArgumentParser(description='Retrieve the data from the database and store it in a csv file')
parser.add_argument('-u', '--user', help='The username for the postgress database')
parser.add_argument('-p', '--password', help='The password for the database')
args = parser.parse_args()
print(args.user)

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

# Check if the csv file exists and creates it when it does not
exists = os.path.exists(filename)
f = open(filename, 'a')
writer = csv.DictWriter(f, fieldnames=['channel', 'sender', 'date', 'message'])
if not exists:
	writer.writeheader()

cur = conn.cursor()
cur.execute(query)

# print cur.fetchall()

def writeToCsv (queryResult) :
    count = 0
    while True:
    	rows = queryResult.fetchmany()
    	count += len(rows)
    	print(count)
    	if not rows:
    		break
    	for row in rows:
    		writer.writerow({
    			'channel' : row[0],
    			'sender' : row[1],
    			'date' : row[2],
    			'message' : row[3]
    		})

writeToCsv(cur)

f.close()
