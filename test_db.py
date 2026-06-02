import psycopg2
conn = psycopg2.connect(
    host="database-1.cvkg622c6us1.ap-southeast-2.rds.amazonaws.com",
    database="news_db",
    user="postgres",
    password="saniyabijoy",
    port="5432"
)

print("Database connected successfully!")


cur = conn.cursor()