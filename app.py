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




# import streamlit as st
# import re
# import spacy

# # Load spaCy English NLP model
# nlp = spacy.load("en_core_web_sm")

# def preprocess_text(text):
#     """Remove special characters and lowercase text."""
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
#     return text.lower()

# def extract_entities(text):
#     """Extract job title, skills, and location from text using spaCy."""
#     doc = nlp(text)
    
#     job_title = []
#     skills = []
#     location = []
    
#     for ent in doc.ents:
#         if ent.label_ in ["ORG", "WORK_OF_ART"]:  # Assuming job titles appear as work-related terms
#             job_title.append(ent.text)
#         elif ent.label_ in ["GPE", "LOC"]:  # Locations
#             location.append(ent.text)
#         elif ent.label_ in ["NOUN"]:  # Extract possible skills
#             skills.append(ent.text)
    
#     return {
#         "Job Title": list(set(job_title)) or ["Unknown"],
#         "Skills": list(set(skills)) or ["Unknown"],
#         "Location": list(set(location)) or ["Unknown"]
#     }

# def generate_boolean_query(entities):
#     """Generate Boolean query based on extracted entities."""
#     job_title = f'("{entities["Job Title"][0]}")' if entities["Job Title"] else ""
#     skills = " OR ".join([f'"{skill}"' for skill in entities["Skills"]])
#     location = f'("{entities["Location"][0]}")' if entities["Location"] else ""

#     boolean_query = f"{job_title} AND ({skills}) AND {location}"
#     return boolean_query

# def main():
#     st.title("Automated Search Strategy Generator")
#     st.markdown("Enter a job description to generate an optimized Boolean search query.")
    
#     job_description = st.text_area("Paste Job Description Here:", height=200)
    
#     if st.button("Generate Search Query"):
#         if job_description.strip():
#             entities = extract_entities(job_description)
#             generated_query = generate_boolean_query(entities)
            
#             st.subheader("Extracted Entities:")
#             st.json(entities)
            
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
# import spacy

# # Load spaCy English NLP model
# nlp = spacy.load("en_core_web_sm")

# # Predefined list of skills (can be expanded)
# SKILL_LIST = ["Python", "SQL", "Java", "Machine Learning", "Deep Learning", "Tableau", "AWS", "React", "Angular"]

# def preprocess_text(text):
#     """Remove special characters and lowercase text."""
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
#     return text.lower()

# def extract_entities(text):
#     """Extract job title, skills, and location from text using spaCy."""
#     doc = nlp(text)
    
#     job_title = []
#     skills = []
#     location = []

#     for ent in doc.ents:
#         if ent.label_ in ["PERSON", "ORG"]:  # Job titles are often under ORG or PERSON
#             job_title.append(ent.text)
#         elif ent.label_ in ["GPE", "LOC"]:  # Locations
#             location.append(ent.text)

#     # Extract skills from text using predefined skill list
#     words = text.split()
#     detected_skills = [word for word in words if word in SKILL_LIST]

#     return {
#         "Job Title": list(set(job_title)) or ["Unknown"],
#         "Skills": list(set(detected_skills)) or ["Unknown"],
#         "Location": list(set(location)) or ["Unknown"]
#     }

# def generate_boolean_query(entities):
#     """Generate Boolean query based on extracted entities."""
#     job_title = f'("{entities["Job Title"][0]}")' if entities["Job Title"] and entities["Job Title"][0] != "Unknown" else ""
#     skills = " OR ".join([f'"{skill}"' for skill in entities["Skills"] if skill != "Unknown"])
#     location = f'("{entities["Location"][0]}")' if entities["Location"] and entities["Location"][0] != "Unknown" else ""

#     boolean_query = f"{job_title} AND ({skills}) AND {location}".strip()
#     return boolean_query if boolean_query != " AND () AND " else "No valid query generated."

# def main():
#     st.title("Automated Search Strategy Generator")
#     st.markdown("Enter a job description to generate an optimized Boolean search query.")
    
#     job_description = st.text_area("Paste Job Description Here:", height=200)
    
#     if st.button("Generate Search Query"):
#         if job_description.strip():
#             entities = extract_entities(job_description)
#             generated_query = generate_boolean_query(entities)
            
#             st.subheader("Extracted Entities:")
#             st.json(entities)
            
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
from src.ner_extraction import extract_entities  # Ensure correct import path
from src.query_generator import generate_boolean_query  # Ensure correct import path
from src import evaluate  

# Title
st.title("Automated Boolean Query Generator")

# User input
job_description = st.text_area("Paste Job Description Here:", height=200)

if st.button("Generate Query"):
    if job_description.strip():
        # Extract entities
        entities = extract_entities(job_description)
        job_title = entities.get("Job Title", [])
        skills = entities.get("Skills", [])
        location = entities.get("Location", [])

        # Generate Boolean Query
        query = generate_boolean_query(job_title, skills, location)

        # Display extracted entities
        st.subheader(" Extracted Entities")
        st.json(entities)

        # Display boolean query
        st.subheader(" Generated Boolean Query")
        st.code(query, language="sql")
    else:
        st.warning("Please enter a job description.")
    import streamlit as st  
    import evaluate  # Import your evaluation script  

    # Run evaluation and get metrics  
    results = evaluate.run_evaluation()  # Ensure this function returns precision, recall, F1  

    # Display the results in Streamlit  
    st.title("Entity Extraction Evaluation")  
    st.write(f" **Precision:** {results['precision']:.2f}")  
    st.write(f" **Recall:** {results['recall']:.2f}")  
    st.write(f" **F1 Score:** {results['f1_score']:.2f}")  
