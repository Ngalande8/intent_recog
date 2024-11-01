import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def lemmatize(text):
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc])
    return lemmatized_text

# Example usage
text = "This is an example ate sentence with stop word's and punctuation, that we want to remove! can't won't"
text_lemmatized = lemmatize(text)
print("Lemmatized text:", text_lemmatized)
