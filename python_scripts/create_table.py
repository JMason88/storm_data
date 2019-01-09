import psycopg2

conn = psycopg2.connect("dbname=storm_data host=localhost port=5432 user=postgres")
conn.autocommit = True

cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE storm (
        fid BIGINT PRIMARY KEY,
        date TIMESTAMP,
        btid INTEGER,
        name VARCHAR(15),
        lat DECIMAL(3,1),
        long DECIMAL(4,1),
        wind_kts INT,
        pressure INT,
        cat VARCHAR(2),
        basin VARCHAR(15),
        shape_leng DECIMAL(7,5)
    )
    '''
)