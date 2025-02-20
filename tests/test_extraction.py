import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ner_extraction import extract_entities

def test_extract_entities():
    text = "We need a Data Scientist skilled in Python and SQL in New York."
    expected = {
        "Job Title": ["Data Scientist"],
        "Skills": ["Python", "SQL"],
        "Location": ["New York"]
    }

    result = extract_entities(text)
    print("Extracted Output:", result)  # Debugging line
    assert result == expected
