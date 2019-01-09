import psycopg2

conn = psycopg2.connect("dbname=storm_data host=localhost port=5432 user=postgres")
conn.autocommit = True

cur = conn.cursor()

cur.execute(
    '''
    DROP USER analyst
    '''
)

cur.execute(
    '''
    CREATE USER analyst
    '''
)

cur.execute(
    '''
    REVOKE ALL PRIVILEGES ON DATABASE storm_data FROM analyst
    '''
)

cur.execute(
    '''
    GRANT SELECT ON TABLE storm TO analyst
    '''
)

cur.execute(
    '''
    GRANT INSERT ON TABLE storm TO analyst
    '''
)

cur.execute(
    '''
    GRANT UPDATE ON TABLE storm TO analyst
    '''
)