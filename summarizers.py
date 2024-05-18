from transformers import pipeline
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
summarizer = pipeline("summarization", model = "facebook/bart-large-cnn", device = device)
summarizer.model.to(device)

def summarize_bart(text: str) -> str:
    return summarizer(text, max_length = 150, min_length = 30, do_sample = False)[0]["summary_text"]