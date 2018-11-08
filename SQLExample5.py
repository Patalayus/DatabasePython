import mysql.connector
from mysql.connector import MySQLConnection, Error
#imports librarys for the python file to use

def connect():
    #creates a function called connect
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='example1',
                                       user='root',
                                       password='')
        #establishes connection through the ports above
        if conn.is_connected():
            print('Connected to MySQL database')
            #lets the user know that a connection has been established

    except Error as e:
        print(e)

    return conn

def delete(conn, id):
    #creates function called delete
    query = "DELETE FROM department WHERE DepartmentNo = %s"

    try:
        cursor = conn.cursor()
        cursor.execute(query, (id,))

        conn.commit()

    except Error as error:
        print(error)

def view_all(conn):
    #creates funciton called view_all
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM department")
        rows = cursor.fetchall()

        print('Total Record(s):', cursor.rowcount)
        #shows total number of records
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    conn = connect()
    delete(conn, 'L028')
    #deletes L028
    view_all(conn)

