def detect_crisis_trend(df):
    counts = df["sentiment"].value_counts(normalize=True)
    if counts.get("NEGATIVE", 0) > 0.4:
        return "⚠️ Crisis Detected: Negative sentiment spike!"
    return "✅ Sentiment levels normal."
