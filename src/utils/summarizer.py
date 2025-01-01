from transformers import pipeline, AutoTokenizer


def summarize_text(description, verbose=False):
    # Load tokenizer for better length handling
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    token_count = len(tokenizer(description)["input_ids"])
    max_length = min(150, token_count)
    min_length = min(50, max_length // 2)  # Ensure min_length is valid

    summarizer = pipeline("summarization", model="facebook/bart-base")
    summarizer_text = summarizer(description, max_length=max_length, min_length=min_length, do_sample=False)

    summary_text = summarizer_text[0]["summary_text"] if summarizer_text else ""

    if verbose:
        print(f"Summarized text: {summary_text}")
    return summary_text


summarized_text = description_summarizer(
    "To curb gang killings and a rise in homicides, the measure empowers the military to make arrests and allows the authorities to "
    "enter suspects’ homes without warrants and deny them bail.", True
)
