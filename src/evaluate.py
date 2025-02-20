from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_queries(manual_results, generated_results):
    precision = precision_score(manual_results, generated_results, average='weighted')
    recall = recall_score(manual_results, generated_results, average='weighted')
    f1 = f1_score(manual_results, generated_results, average='weighted')
    return precision, recall, f1

def evaluate_extraction(predictions, ground_truth):
    correct = 0
    total_extracted = 0
    total_expected = 0

    for pred, expected in zip(predictions, ground_truth):
        extracted_set = set(pred)
        expected_set = set(expected)

        correct += len(extracted_set & expected_set)
        total_extracted += len(extracted_set)
        total_expected += len(expected_set)

    precision = correct / total_extracted if total_extracted > 0 else 0
    recall = correct / total_expected if total_expected > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1_score:.2f}")

    return {"precision": precision, "recall": recall, "f1_score": f1_score}

if __name__ == "__main__":
    # Example predictions and ground truth
    predictions = [["Python", "Django"], ["SQL", "Machine Learning"]]
    ground_truth = [["Python", "Django"], ["SQL", "ML"]]

    results = evaluate_extraction(predictions, ground_truth)

    print("=" * 30)
    print("Entity Extraction Evaluation")
    print("=" * 30)
    print(f"Precision: {results['precision']:.2f}")
    print(f"Recall: {results['recall']:.2f}")
    print(f"F1 Score: {results['f1_score']:.2f}")
    print("=" * 30)
