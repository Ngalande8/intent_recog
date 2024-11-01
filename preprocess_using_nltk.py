import spacy
import string
from nltk.corpus import stopwords
import nltk

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text)
    filtered_text = [word.lower() for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

def remove_punctuation(text):
    punctuation_table = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(punctuation_table)
    return text_without_punctuation

def lemmatize(text):
    '''This performs stemming''' 
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc])
    text_lower = lemmatized_text.lower()
    text_without_stopwords = remove_stopwords(text_lower)
    text_without_stopwords_and_punctuation = remove_punctuation(text_without_stopwords)
    return text_without_stopwords_and_punctuation


# sentence = '''i want to make a tpin. My name is Francis. Please test this.
#             i CANNot be flying. I have great abilities. I can't eat now.'''
            
#print(lemmatize(sentence))

# Example usage
input_file_path = 'questions.txt'
output_file_path = 'output.txt'

# Read input file, lemmatize sentences, and write to output file
with open(input_file_path, 'r', encoding='utf-8') as input_file, \
     open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        # Lemmatize each line (sentence) in the input file
        lemmatized_sentence = lemmatize(line.strip())
        # Write lemmatized sentence to output file
        output_file.write(lemmatized_sentence + '\n')

print("Lemmatization complete. Output saved to:", output_file_path)
