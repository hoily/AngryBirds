from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_analysis(text):
    vs = analyzer.polarity_scores(text)
    return(vs)
