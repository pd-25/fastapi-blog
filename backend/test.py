import psycopg2
print('first')
conn = psycopg2.connect("dbname=fastapi_blog user=postgres host='localhost' port=5432")  # Replace with actual port if needed

print('2nd')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM user")

# Retrieve query results
records = cur.fetchall()

print("Connected to PostgreSQL database!")