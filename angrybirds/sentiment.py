from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_analysis(text):
    return analyzer.polarity_scores(text)
