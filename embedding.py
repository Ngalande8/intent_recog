import spacy

# Load the spaCy model with Universal Sentence Encoder
nlp = spacy.load('en_use_md')

# Define two documents
sen_1 = nlp('tpin create')
sen_2 = nlp('tpin register')
sen_3 = nlp('make tpin')
sen_4 = nlp('evolve')
sen_5 = nlp ('evolve')

# Calculate the cosine similarity between the two document vectors
cosine_similarity = sen_1.vector.dot(sen_2.vector) / (sen_1.vector_norm * sen_2.vector_norm)
cosine_similarity_2 = sen_2.vector.dot(sen_3.vector) / (sen_2.vector_norm * sen_3.vector_norm)
cosine_similarity_3 = sen_1.vector.dot(sen_4.vector) / (sen_1.vector_norm * sen_4.vector_norm)
cosine_similarity_4 = sen_4.vector.dot(sen_5.vector) / (sen_4.vector_norm * sen_5.vector_norm)

print("Embedding for first sentence is: ", sen_1.vector)
print("Embedding for second sentence is: ", sen_2.vector)

# Print the cosine similarity
print("Cosine similarity between the two sentences:", cosine_similarity)
print("Cosine similarity between the two sentences:", cosine_similarity_2)
print("Cosine similarity between the two sentences:", cosine_similarity_3)
print("Cosine similarity between the two sentences:", cosine_similarity_4)
