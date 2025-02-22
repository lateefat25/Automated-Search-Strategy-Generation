# About The Project

This codebase is part of the CM3070 Final Project submission for the University of London BSc Computer Science degree. The project aims to develop a system that automates creating search queries from job descriptions. In traditional recruitment, human resource professionals and recruiters must manually craft search queries based on job descriptions to find suitable candidates on various job portals and databases.

# Directory Structure of the project
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


# Setup Instructions


