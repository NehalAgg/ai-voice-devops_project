from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from data import data

# prepare data
texts = [x[0] for x in data]
labels = [x[1] for x in data]

# vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# train model
model = MultinomialNB()
model.fit(X, labels)

# save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained successfully!")
