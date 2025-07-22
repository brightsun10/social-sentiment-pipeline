import plotly.express as px

def plot_sentiment_trend(df):
    df["date"] = "Today"
    grouped = df.groupby(["date", "sentiment"]).size().reset_index(name="count")
    fig = px.bar(grouped, x="sentiment", y="count", color="sentiment", title="Sentiment Trend")
    return fig

def sentiment_distribution_pie(df):
    pie_data = df["sentiment"].value_counts().reset_index()
    pie_data.columns = ["sentiment", "count"]
    fig = px.pie(pie_data, names="sentiment", values="count", title="Sentiment Distribution")
    return fig
