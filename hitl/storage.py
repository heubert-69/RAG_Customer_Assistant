import psycopg2

conn = psycopg2.connect(
    dbname="rag_db",
    user="postgres",
    password="jorge69",
    host="localhost"
)

def save_escalation(query):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO escalations (query) VALUES (%s)",
        (query,)
    )
    conn.commit()
