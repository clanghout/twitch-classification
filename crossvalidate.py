import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from tfidf_documents import tf_idf_predict

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
with open('data/data_new.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		channel = row['channel']
		message = row['message']
		if channel not in label_dict:
			continue
		if channel not in messages:
			messages[channel] = []
		messages[channel].append(message)

for k in messages:
	m = messages[k]
	messages[k] = '\n'.join(m)

data = pd.DataFrame(list(messages.items()), columns=['channel', 'messages'])
data['label'] = data['channel'].apply(lambda x: label_dict[x])
channels = data.channel

kf = KFold(n_splits=4)
results = []
for train, test in kf.split(channels):
	predicted = tf_idf_predict(data[data['channel'].isin(channels[train])],
							   data[data['channel'].isin(channels[test])])
	labels = data[data['channel'].isin(channels[test])]['label']
	
	results.extend(zip(labels, predicted))

res = pd.DataFrame(results, columns=['label', 'prediction'])
counts = res.groupby(['label', 'prediction']).size()
print(counts)
