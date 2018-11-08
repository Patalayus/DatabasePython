import mysql.connector
from mysql.connector import MySQLConnection, Error
#imports the libraries for python to use

def connect():
    #this defines a function called connect
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='example1',
                                       user='root',
                                       password='')
        #establishes connection through the ports listed above
        if conn.is_connected():
            print('Connected to MySQL database')
            #prints this statement once it has connected to the database

    except Error as e:
        print(e)

    return conn

def insert(conn, num, name):
    #creates function called insert
    #it then inserts a query into the Department section for department name and number
    query = "INSERT INTO Department(DepartmentNo,DepartmentName) " \
            "VALUES(%s,%s)"
    args = (num, name)

    try:
        cursor = conn.cursor()
        cursor.execute(query, args)
        #prints the records listed
        print('Number of records inserted: ', cursor.rowcount)
        conn.commit()

    except Error as error:
        print(error)

def view_all(conn):
    #defines function called view_all
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM department")
        rows = cursor.fetchall()

        #prints total records
        print('Total Record(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        #closes application
        cursor.close()
        conn.close()


if __name__ == '__main__':
    conn = connect()
    insert(conn, 'L009', 'HR')
    view_all(conn)

