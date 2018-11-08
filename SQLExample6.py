import mysql.connector
from mysql.connector import MySQLConnection, Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='example1',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    return conn

def view_all(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()

        print('Total Record(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    conn = connect()
    view_all(conn)
