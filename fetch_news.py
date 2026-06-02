import requests
import pg8000
from textblob import TextBlob
from datetime import datetime

API_KEY = "53571c2a4caf4ab4ae1c27abc5fd2153"

conn = pg8000.connect(
    host="database-1.cvkg622c6us1.ap-southeast-2.rds.amazonaws.com",
    database="news_db",
    user="postgres",
    password="saniyabijoy",
    port="5432"
)
url = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "category": "technology",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

print(response.json())

articles = response.json().get("articles", [])

cur = conn.cursor()