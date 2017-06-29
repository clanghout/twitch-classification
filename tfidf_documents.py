import csv
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords

label_dict = {}
with open('label_dictionary.txt') as f:
	for line in f:
		dat = line.split()
		key = dat[0]
		val = ' '.join(dat[1:])
		label_dict[key] = val
	
messages = {}
with open('data/data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		channel = row['channel']
		message = row['message']
		if channel not in messages:
			messages[channel] = []
		messages[channel].append(message)

count_vect = CountVectorizer()
for k in messages.keys():
	message_list = messages[k]
	message = '\n'.join(message_list)
	messages[k] = message
	
X_train_counts = count_vect.fit_transform(messages.values())

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, list(messages.keys()))

new_messages = {}
with open('data/data_chak.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		channel = row['channel']
		message = row['message']
		if channel not in new_messages:
			new_messages[channel] = []
		new_messages[channel].append(message)

docs_new = []
for k in new_messages.keys():
	message_list = new_messages[k]
	message = '\n'.join(message_list)
	docs_new.append(message)

X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for i in range(0, len(predicted)):
	print(predicted[i], ' ', label_dict[predicted[i]], ' ', list(new_messages.keys())[i])

