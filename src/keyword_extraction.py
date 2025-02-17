from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake
from transformers import pipeline
from keybert import KeyBERT
import nltk
nltk.download('stopwords')

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Suppresses most TensorFlow warnings


# TF-IDF
def extract_tfidf_keywords(corpus, top_n=5):
    vectorizer = TfidfVectorizer(max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform(corpus)
    return vectorizer.get_feature_names_out()

# RAKE
def extract_rake_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()[:5]

# BERT
#def extract_bert_keywords(text):
 #   nlp_pipeline = pipeline("feature-extraction", model="bert-base-uncased")
 #   return nlp_pipeline(text)

kw_model = KeyBERT()

def extract_bert_keywords(text):
    return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=5)
