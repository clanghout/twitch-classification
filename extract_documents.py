import csv
import pandas as pd

df = pd.DataFrame()

def combine(x):
	return pd.Series(dict(genre = x['genre'],
						  channel = x['channel'],
						  messages = "{%s}" % ", ".join[x['message']]))
						

with open('data/data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	next(reader)
	for row in reader:
		df = df.append(row, ignore_index=True)

#df_messages = df.groupby(['genre', 'channel'])['message'].apply(lambda x: ', '.join(x)).reset_index()
df_messages = df.groupby(['genre', 'channel'])['message'].apply(lambda x: '\n'.join(x)).reset_index()
message = df_messages.iloc[0]['message']
for m in message.split('\n'):
	print(m)
