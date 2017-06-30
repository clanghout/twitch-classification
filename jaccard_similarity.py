def compute_shingles(message, window):
	seq = set()
	for m in message.split('\n'):
		m = m.lower()
		m = re.sub(r'[^a-z ]+', '', m)
		m = m.replace(' ', ' ')
		words = m.split(' ')
		words = [x for x in words if x not in stopwords.words('english')]
		if len(words) < window:
			continue
		for i in range(0, len(words) - window + 1):
			seq.add(tuple(words[i:i+window]))
	return seq
	
def jacard_similarity(x, y):
	inter = x.intersection(y)
	un = x.union(y)
	return len(inter) / len(un)

#df_messages = df.groupby(['genre', 'channel'])['message'].apply(lambda x: '\n'.join(x)).reset_index()
#df_messages['message'] = df_messages['message'].apply(lambda x: compute_shingles(x, 2))
#channels = df_messages['channel']
#jac_sim = pd.DataFrame(index=channels, columns=channels)
#for index_i, row_i in df_messages.iterrows():
#	for index_j, row_j in df_messages.iterrows():
#		jac_sim.ix[row_i['channel'], row_j['channel']] = jacard_similarity(row_i['message'], 																		row_j['message'])

