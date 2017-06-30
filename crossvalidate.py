import csv
import pandas as pd

# Load channel dictionary
label_dict = {}
with open('label_dictionary.txt') as f:
	for line in f:
		dat = line.split()
		key = dat[0]
		val = ' '.join(dat[1:])
		label_dict[key] = val

# Load training data (to test performance on unseen data)
messages = {}
with open('data/data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		channel = row['channel']
		message = row['message']
		if channel not in messages:
			messages[channel] = []
		messages[channel].append(message)

data = pd.DataFrame(messages)
channels = data.channel.unique()
