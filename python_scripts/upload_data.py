import psycopg2
import pandas as pd
import csv

conn = psycopg2.connect("dbname=storm_data host=localhost port=5432 user=analyst")
conn.autocommit = True

cur = conn.cursor()

with open('storm_data.csv', 'r') as f:
    next(f)
    reader = pd.read_csv(f)
    updated_rows = []

    #print(len(reader))

    for row in reader:

        print(row)

        cur.execute(
            '''
            INSERT INTO storm VALUES (
                %s, 
                to_timestamp(%s || '-' || %s || '-' || %s|| ' ' || %s, 'YYYY-MM-DD HH:MI'), 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s
                )
            ''', row)
