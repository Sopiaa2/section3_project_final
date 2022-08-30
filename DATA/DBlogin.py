import psycopg2

conn = psycopg2.connect(
    host="jelani.db.elephantsql.com",
    database="dgwizwfv",
    user="dgwizwfv",
    password="NA-i9Pf-g5WWLwhj7Rs-BWFRFfwaArSB")

cur = conn.cursor()
sql = "select * from eth_data"
cur.execute(sql)

result = cur.fetchall()
print(result)