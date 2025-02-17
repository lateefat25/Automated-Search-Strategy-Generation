from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_queries(manual_results, generated_results):
    precision = precision_score(manual_results, generated_results, average='weighted')
    recall = recall_score(manual_results, generated_results, average='weighted')
    f1 = f1_score(manual_results, generated_results, average='weighted')
    return precision, recall, f1
