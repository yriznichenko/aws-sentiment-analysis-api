import json

positive_words = [
    "love",
    "amazing",
    "excellent",
    "fantastic",
    "good",
    "great"
]

negative_words = [
    "hate",
    "terrible",
    "bad",
    "awful",
    "worst"
]

def predict_sentiment(text):
    text = text.lower()

    positive_score = 0
    negative_score = 0

    for word in positive_words:
        if word in text:
            positive_score += 1

    for word in negative_words:
        if word in text:
            negative_score += 1

    if positive_score > negative_score:
        return "positive", positive_score

    elif negative_score > positive_score:
        return "negative", negative_score

    else:
        return "neutral", 0

def lambda_handler(event, context):

    body = event

    if "body" in event:
        body = json.loads(event["body"])

    text = body.get("text", "")

    sentiment, confidence = predict_sentiment(text)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "text": text,
            "sentiment": sentiment,
            "confidence": confidence
        })
    }