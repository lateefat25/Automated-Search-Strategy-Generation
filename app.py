import streamlit as st
import spacy
from spacy.pipeline import EntityRuler

# Load spaCy English NLP model
nlp = spacy.load("en_core_web_sm")

# Define job titles & skills for rule-based matching
job_titles = ["Data Scientist", "Software Engineer", "Machine Learning Engineer"]
skills = ["Python", "SQL", "Machine Learning", "Deep Learning", "NLP", "TensorFlow", "Pandas"]

# Add rule-based entity recognition
if "entity_ruler" in nlp.pipe_names:
    nlp.remove_pipe("entity_ruler")  # Remove existing instance if present

ruler = nlp.add_pipe("entity_ruler", before="ner")


patterns = [{"label": "JOB_TITLE", "pattern": title} for title in job_titles] + \
           [{"label": "SKILL", "pattern": skill} for skill in skills]

ruler.add_patterns(patterns)

def extract_entities(text):
    """Extract job title, skills, and location from text using spaCy."""
    doc = nlp(text)

    job_title = []
    skill_set = []
    location = []

    for ent in doc.ents:
        if ent.label_ == "JOB_TITLE":
            job_title.append(ent.text)
        elif ent.label_ == "SKILL":
            skill_set.append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:  # Locations
            location.append(ent.text)

    return {
        "Job Title": list(set(job_title)) or ["Unknown"],
        "Skills": list(set(skill_set)) or ["Unknown"],
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
