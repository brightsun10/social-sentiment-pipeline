import gradio as gr
import pandas as pd
from sentiment import analyze_sentiment_batch
from dashboard import plot_sentiment_trend, sentiment_distribution_pie
from utils import detect_crisis_trend

def run_pipeline(texts):
    texts = [t.strip() for t in texts.split("\n") if t.strip()]
    df = analyze_sentiment_batch(texts)
    pie = sentiment_distribution_pie(df)
    line = plot_sentiment_trend(df)
    alert = detect_crisis_trend(df)
    return df, pie, line, alert

demo = gr.Interface(
    fn=run_pipeline,
    inputs=gr.Textbox(lines=10, label="Paste social media posts (one per line)"),
    outputs=[
        gr.Dataframe(label="Sentiment Results"),
        gr.Plot(label="Sentiment Distribution"),
        gr.Plot(label="Sentiment Trend"),
        gr.Textbox(label="Crisis Alert")
    ],
    title="Social Sentiment Analysis Pipeline",
    description="Simulates an ETL pipeline for analyzing sentiment from social media posts."
)

if __name__ == "__main__":
    demo.launch()