import tweepy
import time
import random

API_KEY = "0PMvNHU0reC54p1ZzrQ9cg9ZN"
API_SECRET = "kPRtPGaSUVVxfGJEqW7ray2fNQPD8CWgg9ymdZljFLXG57NRZTهkPRtPGaSUVVxfGJEqW7ray2fNQPD8CWgg9ymdZljFLXG57NRZT"
ACCESS_TOKEN = "2000830256111083521-AnDycdfypu58ZQR5PrSMUyBkxBKzhM"
ACCESS_SECRET = "PHBWuNVoy3uI5TDIEgkzYiVog8ALA64aVJWDYvBiPUB8C"

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET,
    ACCESS_TOKEN, ACCESS_SECRET
)

api = tweepy.API(auth)

texts = [
    "🚀 تابعنا لمحتوى مميز!",
    "🔥 لا تفوت أحدث التحديثات",
    "✨ كل 15 دقيقة فكرة جديدة",
    "📢 ترقب المزيد قريبًا!"
]

while True:
    tweet = random.choice(texts)
    api.update_status(tweet)
    print("تم نشر:", tweet)
    time.sleep(900)  # 15 دقيقة
