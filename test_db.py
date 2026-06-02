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

cur.execute("""
CREATE TABLE IF NOT EXISTS news_data (
    id SERIAL PRIMARY KEY,
    news_date DATE,
    source_name VARCHAR(255),
    title TEXT,
    sentiment_score FLOAT,
    sentiment_label VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Save changes
conn.commit()

print("Table created successfully!")

# Close cursor and connection
cur.close()
conn.close()
