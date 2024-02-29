import demoji
from scrape2 import GetPublicComments, GetPrivateComments
from textblob import TextBlob
import csv


def EmojiSentiment(emoji_list):
    emoji_score = 0
    emoji_len = 0
    with open('output.csv', 'r') as f:
        reader = csv.reader(f)
        for emoji in emoji_list:
            for row in reader:
                if row[2].upper() == emoji:
                    emoji_score += row[1]
                    emoji_len += 1
    if emoji_len > 0:
        return emoji_score/emoji_len
    else:
        return emoji_score

def CalculateCommSentiment(comment):

    cleaned_comm = demoji.replace_with_desc(comment, " ")
    comm_emoji_list = demoji.findall_list(comment, desc=True)

    comm_analysis = TextBlob(comment)
    if len(comm_emoji_list) > 0:
        emoji_sentiment = EmojiSentiment(comm_emoji_list)
    else:
        emoji_sentiment = 0.0
    comm_sentiment = (comm_analysis.sentiment.polarity * 0.8) + (emoji_sentiment * 0.2)

    return(comm_sentiment, comm_analysis.sentiment.subjectivity)

def SentimentAnalysis(post_link, user_token=None):
    if user_token != None:
        all_comments = GetPrivateComments()
    else:
        all_comments = GetPublicComments(post_link)

    final_sentiment = 0
    final_subjectivity = 0

    for comment in all_comments:
        comm_sentiment, comm_subjectivity = CalculateCommSentiment(comment)
        final_sentiment += comm_sentiment * comm_subjectivity
        final_subjectivity += comm_subjectivity

    final_sentiment /= final_subjectivity
    final_subjectivity /= len(all_comments)

    print(final_sentiment)
    print(final_subjectivity)

SentimentAnalysis("https://www.instagram.com/p/CpxnsErrY_j/")