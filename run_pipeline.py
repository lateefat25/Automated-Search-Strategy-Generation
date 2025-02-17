from src.preprocessing import preprocess_dataset
from src.ner_extraction import extract_entities
from src.keyword_extraction import extract_tfidf_keywords, extract_rake_keywords, extract_bert_keywords
from src.query_generator import generate_boolean_query
from src.evaluate import evaluate_queries
import pandas as pd

def extract_entities_from_text(text, row):
    """
    Extracts job title, skills, and location from the row data.
    """
    job_title = row.get("Job Title", "Unknown Job Title")
    
    skills = row.get("skills", "").split(",")  # Assuming skills are comma-separated
    skills = [skill.strip() for skill in skills if skill]  # Clean up spaces
    
    if not skills:
        skills = ["Unknown Skills"]
    
    location = row.get("location", "Unknown Location")
    
    return {"Job Title": [job_title], "Skills": skills, "Location": [location]}

# def main():
#     # Step 1: Preprocess the data
#     preprocess_dataset("data/job_descriptions.csv", "data/processed_data.csv")

#     # Step 2: Load processed data
#     data = pd.read_csv("data/processed_data.csv")
    
#     # Step 3: Extract entities and generate boolean queries
#     for index, row in data.iterrows():
#         print(f"Text: {row['Processed_Text']}")
        
#         # Extract entities (Job Title, Skills, Location) from the row data
#         entities = extract_entities_from_text(row['Processed_Text'], row)
#         print(f"Entities: {entities}")
        
#         # Safely access job title and location
#         job_title = entities.get("Job Title", ["Unknown Job Title"])[0]
#         location = entities.get("Location", ["Unknown Location"])[0]
#         skills = entities.get("Skills", ["Unknown Skills"])

#         # Step 4: Extract keywords using TF-IDF (or other methods)
#         tfidf_keywords = extract_tfidf_keywords([row['Processed_Text']])
        
#         # Step 5: Generate Boolean query using extracted data
#         boolean_query = generate_boolean_query(
#             job_title=job_title,  
#             skills=tfidf_keywords,
#             location=location
#         )
        
#         print(f"Boolean Query for {row['Job Title']}: {boolean_query}")

# if __name__ == "__main__":
#     main()
def main():
    # Step 1: Preprocess the data
    preprocess_dataset("data/job_descriptions.csv", "data/processed_data.csv")

    # Step 2: Load processed data
    data = pd.read_csv("data/processed_data.csv")
    
    # Step 3: Extract entities and generate boolean queries for the first 10 rows
    for index, row in data.head(10).iterrows():  # Only iterate through the first 10 rows
        print(f"Text: {row['Processed_Text']}")
        
        # Extract entities (Job Title, Skills, Location) from the row data
        entities = extract_entities_from_text(row['Processed_Text'], row)
        print(f"Entities: {entities}")
        
        # Safely access job title and location
        job_title = entities.get("Job Title", ["Unknown Job Title"])[0]
        location = entities.get("Location", ["Unknown Location"])[0]
        skills = entities.get("Skills", ["Unknown Skills"])

        # Step 4: Extract keywords using TF-IDF (or other methods)
        tfidf_keywords = extract_tfidf_keywords([row['Processed_Text']])
        
        # Step 5: Generate Boolean query using extracted data
        boolean_query = generate_boolean_query(
            job_title=job_title,  
            skills=tfidf_keywords,
            location=location
        )
        
        print(f"Boolean Query for {row['Job Title']}: {boolean_query}")

if __name__ == "__main__":
    main()
