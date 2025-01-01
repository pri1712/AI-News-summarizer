from transformers import pipeline, AutoTokenizer


def description_summarizer(description, verbose=False):
    # Load tokenizer for better length handling
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    token_count = len(tokenizer(description)["input_ids"])
    max_length = min(150, token_count)
    min_length = min(50, max_length // 2)  # Ensure min_length is valid

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarizer_text = summarizer(description, max_length=max_length, min_length=min_length, do_sample=False)

    summary_text = summarizer_text[0]["summary_text"] if summarizer_text else ""

    if verbose:
        print(f"Summarized text: {summary_text}")
    return summary_text
