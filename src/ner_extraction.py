import spacy  

# Load the English NLP model  
nlp = spacy.load("en_core_web_sm")  

def extract_entities(text):  
    doc = nlp(text)  
    entities = {"Job Title": [], "Skills": [], "Location": []}  
    for ent in doc.ents:  
        if ent.label_ == "ORG":  
            entities["Job Title"].append(ent.text)  
        elif ent.label_ == "GPE":  
            entities["Location"].append(ent.text)  
        elif ent.label_ == "SKILL":  # Custom label, requires a trained model  
            entities["Skills"].append(ent.text)  
    return entities  
