import pandas as pd
import re
import nltk
nltk.download('stopwords')  # Download stop words 
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip().lower()  # Clean up spaces
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    doc = nlp(' '.join(tokens))
    lemmatized = [token.lemma_ for token in doc]
    return ' '.join(lemmatized)

def preprocess_dataset(file_path, output_path):
    df = pd.read_csv(file_path)
    df['Processed_Text'] = df['Job Description'].apply(preprocess_text)
    df.to_csv(output_path, index=False)



if __name__ == "__main__":
    preprocess_dataset("data/job_descriptions.csv", "data/processed_data.csv")
