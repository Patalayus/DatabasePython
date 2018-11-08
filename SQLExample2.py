import mysql.connector
#this imports librarys for the SQL database to work
from mysql.connector import MySQLConnection, Error

def connect():
    #this defines a function
    """ Connect to MySQL database """
    try:
        #the code below, will choose which ports to connect using and the user of the connection (root)
        conn = mysql.connector.connect(host='localhost',
                                       database='example1',
                                       user='root',
                                       password='')
        if conn.is_connected():
            #whence it is connected, print the statement below
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    return conn

def view_all(conn):
    #defines a function
    try:
        #this will go to the database and return information about the records
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM department")
        rows = cursor.fetchall()

        print('Total Record(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
        #this closes the application

if __name__ == '__main__':
    conn = connect()
    view_all(conn)
    #displays the contents of the database
