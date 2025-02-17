# import streamlit as st
# import re
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np

# def preprocess_text(text):
#     """Basic text preprocessing: remove special characters and lowercase."""
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
#     return text.lower()

# def extract_keywords_tfidf(text, top_n=5):
#     """Extract top keywords using TF-IDF."""
#     vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = vectorizer.fit_transform([text])
#     feature_array = np.array(vectorizer.get_feature_names_out())
#     tfidf_sorting = np.argsort(tfidf_matrix.toarray()).flatten()[::-1]
#     top_keywords = feature_array[tfidf_sorting][:top_n]
#     return top_keywords

# def generate_boolean_query(text):
#     """Generate a Boolean search query from extracted keywords."""
#     keywords = extract_keywords_tfidf(preprocess_text(text))
#     boolean_query = ' AND '.join([f'("{kw}")' for kw in keywords])
#     return boolean_query

# def main():
#     st.title("Automated Search Strategy Generator")
#     st.markdown("Enter a job description to generate an optimized Boolean search query.")
    
#     job_description = st.text_area("Paste Job Description Here:", height=200)
    
#     if st.button("Generate Search Query"):
#         if job_description.strip():
#             generated_query = generate_boolean_query(job_description)
#             st.subheader("Generated Boolean Search Query:")
#             st.code(generated_query, language="sql")
#         else:
#             st.warning("Please enter a job description.")
    
#     st.subheader("Feedback")
#     feedback = st.radio("How relevant is this query?", ["1 - Poor", "2 - Fair", "3 - Good", "4 - Very Good", "5 - Excellent"], index=2)
#     if st.button("Submit Feedback"):
#         st.success("Thank you for your feedback!")
    
# if __name__ == "__main__":
#     main()




# import streamlit as st
# import re
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np

# def preprocess_text(text):
#     """Basic text preprocessing: remove special characters and lowercase."""
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
#     return text.lower()

# def extract_keywords_tfidf(text, top_n=5):
#     """Extract top keywords using TF-IDF."""
#     vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = vectorizer.fit_transform([text])
#     feature_array = np.array(vectorizer.get_feature_names_out())
#     tfidf_sorting = np.argsort(tfidf_matrix.toarray()).flatten()[::-1]
#     top_keywords = feature_array[tfidf_sorting][:top_n]
#     return top_keywords

# def generate_boolean_query(text):
#     """Generate a Boolean search query from extracted keywords."""
#     keywords = extract_keywords_tfidf(preprocess_text(text))
#     boolean_query = ' AND '.join([f'("{kw}")' for kw in keywords])
#     return boolean_query

# def main():
#     st.title("Automated Search Strategy Generator")
#     st.markdown("Enter a job description to generate an optimized Boolean search query.")
    
#     job_description = st.text_area("Paste Job Description Here:", height=200)
    
#     if st.button("Generate Search Query"):
#         if job_description.strip():
#             generated_query = generate_boolean_query(job_description)
#             st.subheader("Generated Boolean Search Query:")
#             st.code(generated_query, language="sql")
#         else:
#             st.warning("Please enter a job description.")
    
#     st.subheader("Feedback")
#     feedback = st.radio("How relevant is this query?", ["1 - Poor", "2 - Fair", "3 - Good", "4 - Very Good", "5 - Excellent"], index=2)
#     if st.button("Submit Feedback"):
#         st.success("Thank you for your feedback!")
    
# if __name__ == "__main__":
#     main()


# import streamlit as st
# import re
# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
# import spacy

# # Load English NLP model
# nlp = spacy.load("en_core_web_sm")

# def preprocess_text(text):
#     """Basic text preprocessing: remove special characters and lowercase."""
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
#     return text.lower()

# def extract_keywords_tfidf(text, top_n=5):
#     """Extract top keywords using TF-IDF."""
#     vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))  # Include bigrams
#     tfidf_matrix = vectorizer.fit_transform([text])
#     feature_array = np.array(vectorizer.get_feature_names_out())
#     tfidf_sorting = np.argsort(tfidf_matrix.toarray()).flatten()[::-1]
#     top_keywords = feature_array[tfidf_sorting][:top_n]
#     return list(top_keywords)

# def extract_key_phrases(text, top_n=5):
#     """Extract key phrases using spaCy NLP."""
#     doc = nlp(text)
#     noun_chunks = [chunk.text.lower() for chunk in doc.noun_chunks]
#     return list(set(noun_chunks))[:top_n]  # Get unique key phrases

# def generate_boolean_query(text):
#     """Generate an optimized Boolean search query."""
#     keywords = extract_keywords_tfidf(preprocess_text(text), top_n=3)
#     key_phrases = extract_key_phrases(text, top_n=2)  # Extract key phrases separately

#     all_terms = keywords + key_phrases  # Combine extracted terms
#     boolean_query = ' AND '.join([f'("{kw}" OR "{kw}s")' if not " " in kw else f'("{kw}")' for kw in all_terms])

#     return boolean_query

# def main():
#     st.title("Automated Search Strategy Generator")
#     st.markdown("Enter a job description to generate an optimized Boolean search query.")
    
#     job_description = st.text_area("Paste Job Description Here:", height=200)
    
#     if st.button("Generate Search Query"):
#         if job_description.strip():
#             generated_query = generate_boolean_query(job_description)
#             st.subheader("Generated Boolean Search Query:")
#             st.code(generated_query, language="sql")
#         else:
#             st.warning("Please enter a job description.")
    
#     st.subheader("Feedback")
#     feedback = st.radio("How relevant is this query?", ["1 - Poor", "2 - Fair", "3 - Good", "4 - Very Good", "5 - Excellent"], index=2)
#     if st.button("Submit Feedback"):
#         st.success("Thank you for your feedback!")

# if __name__ == "__main__":
#     main()




import streamlit as st
import re
import spacy

# Load spaCy English NLP model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Remove special characters and lowercase text."""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()

def extract_entities(text):
    """Extract job title, skills, and location from text using spaCy."""
    doc = nlp(text)
    
    job_title = []
    skills = []
    location = []
    
    for ent in doc.ents:
        if ent.label_ in ["ORG", "WORK_OF_ART"]:  # Assuming job titles appear as work-related terms
            job_title.append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:  # Locations
            location.append(ent.text)
        elif ent.label_ in ["NOUN"]:  # Extract possible skills
            skills.append(ent.text)
    
    return {
        "Job Title": list(set(job_title)) or ["Unknown"],
        "Skills": list(set(skills)) or ["Unknown"],
        "Location": list(set(location)) or ["Unknown"]
    }

def generate_boolean_query(entities):
    """Generate Boolean query based on extracted entities."""
    job_title = f'("{entities["Job Title"][0]}")' if entities["Job Title"] else ""
    skills = " OR ".join([f'"{skill}"' for skill in entities["Skills"]])
    location = f'("{entities["Location"][0]}")' if entities["Location"] else ""

    boolean_query = f"{job_title} AND ({skills}) AND {location}"
    return boolean_query

def main():
    st.title("Automated Search Strategy Generator")
    st.markdown("Enter a job description to generate an optimized Boolean search query.")
    
    job_description = st.text_area("Paste Job Description Here:", height=200)
    
    if st.button("Generate Search Query"):
        if job_description.strip():
            entities = extract_entities(job_description)
            generated_query = generate_boolean_query(entities)
            
            st.subheader("Extracted Entities:")
            st.json(entities)
            
            st.subheader("Generated Boolean Search Query:")
            st.code(generated_query, language="sql")
        else:
            st.warning("Please enter a job description.")
    
    st.subheader("Feedback")
    feedback = st.radio("How relevant is this query?", ["1 - Poor", "2 - Fair", "3 - Good", "4 - Very Good", "5 - Excellent"], index=2)
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()
