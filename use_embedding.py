import tensorflow as tf
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity
from preprocess_using_nltk import lemmatize

def preprocess_sentences(sentences):
    preprocessed_sentences = []
    for sentence in sentences:
        preprocessed_sentence = lemmatize(sentence)
        preprocessed_sentences.append(preprocessed_sentence)
    return preprocessed_sentences

def embed_sentences(sentences, model_path):
    embed = hub.load(model_path)
    embeddings = embed(sentences)
    return embeddings

def get_top_similar_sentences(sentence, sentences, embeddings, original_sentences, top_n=3):
    sentence_embedding = embed_sentences([sentence], model_path)[0]
    similarity_scores = cosine_similarity([sentence_embedding], embeddings)[0]
    top_indices = similarity_scores.argsort()[-top_n:][::-1]
    top_sentences = [(original_sentences[i], similarity_scores[i]) for i in top_indices]
    return top_sentences

# Example sentence to compare
my_sentence = "explain leave pay tax"
query_sentence = lemmatize(my_sentence)

# Load sentences from a text file (assuming one sentence per line)
with open("questions.txt", "r", encoding="utf-8") as file:
    sentences = [line.strip() for line in file]

# Preprocess sentences
preprocessed_sentences = preprocess_sentences(sentences)

# Path to the locally saved model
model_path = "C:/Users/NGALANDM/Downloads/archive (1)"

# Get embeddings for the preprocessed sentences
embeddings = embed_sentences(preprocessed_sentences, model_path)

# Get top similar sentences
top_similar_sentences = get_top_similar_sentences(query_sentence, preprocessed_sentences, embeddings, sentences, top_n=3)

# Print top similar sentences
print("Top similar sentences to '{}':".format(query_sentence))
for i, (sentence, similarity_score) in enumerate(top_similar_sentences, 1):
    print("{}. Sentence: '{}', Similarity Score: {:.4f}".format(i, sentence, similarity_score))
