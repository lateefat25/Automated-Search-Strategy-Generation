# About The Project

This codebase is part of the CM3070 Final Project submission for the University of London BSc Computer Science degree. The project aims to develop a system that automates creating search queries from job descriptions. In traditional recruitment, human resource professionals and recruiters must manually craft search queries based on job descriptions to find suitable candidates on various job portals and databases.

# Directory Structure of the project
```
Automated-Search-Strategy-Generation/
├── data/
│   ├── job_descriptions.csv          # Input dataset of job descriptions
│   ├── processed_data.csv            # Preprocessed job descriptions
│   └── evaluation_results.csv        # Results from evaluation
├── src/
│   ├── preprocessing.py              # Preprocessing pipeline
│   ├── ner_extraction.py             # Named Entity Recognition (NER)
│   ├── keyword_extraction.py         # TF-IDF, RAKE, BERT keyword extraction
│   ├── query_generator.py            # Boolean query generator
│   └── evaluate.py                   # Evaluation metrics (Precision, Recall, F1-Score)
├── notebooks/
│   ├── exploratory_analysis.ipynb    # Exploratory Data Analysis (EDA)
│   └── prototype_demo.ipynb          # Prototype demonstration notebook
├── results/
│   ├── query_samples.txt             # Examples of generated queries
│   └── evaluation_metrics.png        # Visualized evaluation results
├── README.md                         # Project documentation
├── requirements.txt                  # Dependencies
└── run_pipeline.py                   # Main script to execute the full pipeline
```

# Setup Instructions

### 1. Create a Virtual Environment
Run the following command to create and activate a virtual environment:

On macOS/Linux:
````
python3 -m venv venv

source venv/bin/activate
````

On Windows (PowerShell):
````
python -m venv venv
venv\Scripts\activate
````

### 2. Install Dependencies
Once activated, install the required dependencies:

````
pip install rake-nltk keybert pandas nltk spacy
pip install streamlit scikit-learn numpy
pip install scikit-learn rake-nltk transformers keybert nltk
pip install keybert --no-deps
pip install --no-cache-dir sentence-transformers
pip install tf-keras
pip install torch==1.9.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
````

### 3. Download Spacy Model

If spacy is installed but the model is missing, download it:
````
python -m spacy download en_core_web_sm
````

### 4. Create requirements.txt
If requirements.txt doesn’t exist, generate it:
````
pip freeze > requirements.txt
````
Then, in the future, you can install all dependencies using:
````
pip install -r requirements.txt
````

### 5. Run the Scripts
Execute the main scripts:
````
python src/preprocessing.py
python src/ner_extraction.py
python src/keyword_extraction.py
python src/query_generator.py
python src/evaluate.py
python run_pipeline.py
````

### 6. Set Up Testing
To run tests using pytest, install it:
````
pip install pytest
````
Verify the installation:
````
pytest --version
````
Run the tests:
````
pytest tests/
````
