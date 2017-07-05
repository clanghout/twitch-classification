from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords


def tf_idf_train(data):
	count_vect = CountVectorizer(stop_words = stopwords.words('english'))
	
	# Do the tf-idf part
	X_train_counts = count_vect.fit_transform(data['messages'])

	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

	# Train naive bayes classifier
	clf = MultinomialNB().fit(X_train_tfidf, data['label'])
	
	return (count_vect, tfidf_transformer, clf)
	
def tf_idf_predict(train, test):
	count_vect, tfidf_transformer, clf = tf_idf_train(train)
	docs_new = test['messages']
	X_new_counts = count_vect.transform(docs_new)
	X_new_tfidf = tfidf_transformer.transform(X_new_counts)

	predicted = clf.predict(X_new_tfidf)
	return predicted
