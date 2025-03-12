from transformers import pipeline

def generate_summary(text, max_length=150):
    """Generate a summary of the given text."""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Split text into chunks if too long
    chunks = split_into_chunks(text, max_chars=1000)
    summaries = []
    
    for chunk in chunks:
        if len(chunk.strip()) > 10:  # Only summarize non-empty chunks
            summary = summarizer(chunk, max_length=max_length, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
    
    return " ".join(summaries)