from transformers import pipeline
import pandas as pd

classifier = pipeline("sentiment-analysis")

def analyze_sentiment_batch(texts):
    results = classifier(texts)
    df = pd.DataFrame(results)
    df["text"] = texts
    df.rename(columns={"label": "sentiment", "score": "confidence"}, inplace=True)
    return df[["text", "sentiment", "confidence"]]
