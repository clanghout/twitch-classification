import csv
import os
import psycopg2
import argparse

parser = argparse.ArgumentParser(description='Retrieve the data from the database and store it in a csv file')
parser.add_argument('-u', '--user', help='The username for the postgress database')
parser.add_argument('-p', '--password', help='The password for the database')
args = parser.parse_args()
print(args.user)

# Name of the CSV file
filename = 'data/data.csv'

# The query for the database
query = "SELECT channel, sender, date, message FROM chat_log"

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
writer = csv.DictWriter(f, fieldnames=['genre', 'channel', 'sender', 'date', 'message'])
if not exists:
	writer.writeheader()

cur = conn.cursor()
cur.execute(query)

count = 0
while True:
	rows = cur.fetchmany()
	count += len(rows)
	print(count)
	if not rows:
		break
	for row in rows:
		genre = label_dict[row[0]]
		writer.writerow({
			'genre' : genre,
			'channel' : row[0],
			'sender' : row[1],
			'date' : row[2],
			'message' : row[3]
		})

f.close()
