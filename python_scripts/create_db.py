import psycopg2

conn = psycopg2.connect("dbname=postgres host=localhost port=5432 user=postgres")
conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE DATABASE storm_data")
conn.commit()