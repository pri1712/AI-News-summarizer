from rouge_score import rouge_scorer


def compute_rouge_scores(ground_truth_summary, generated_summary):
    """
    This function computes a Rouge score between the generated summary and the ground truth summary which we get
        via the rss feeds.
    Returns: A dict of 3 scores , rouge 1 , rouge 2 and rouge L.
    """

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(ground_truth_summary, generated_summary)
    return {
        "Rouge-1": scores['rouge1'].fmeasure,
        "Rouge-2": scores['rouge2'].fmeasure,
        "Rouge-L": scores['rougeL'].fmeasure
    }
