# # from sklearn.feature_extraction.text import CountVectorizer
# from nltk.corpus import stopwords

# # Sample text data
# corpus = [
#     "This is a sample sentence with stop words.",
#     "We want to remove these stop words from the sentences.",
#     "Stop words like 'is', 'a', 'we', 'to', 'from' should be removed."
# ]

# # Create a CountVectorizer object with NLTK's English stop words
# stop_words = set(stopwords.words('english'))
# vectorizer = CountVectorizer(stop_words=stop_words)

# # Fit the vectorizer to the data
# vectorizer.fit(corpus)

# # Get the feature names (words)
# feature_names = vectorizer.get_feature_names_out()

# # Print the feature names after stop word removal
# print("Features after stop word removal:")
# print(feature_names)
