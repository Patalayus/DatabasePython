import mysql.connector
from mysql.connector import MySQLConnection, Error
#imports librarys for python to use

def connect():
    #creates a function called connect
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='example1',
                                       user='root',
                                       password='')
        #establishes connection with the database through these ports
        if conn.is_connected():
            print('Connected to MySQL database')
            #lets user know that it has connected to the database

    except Error as e:
        print(e)

    return conn

def update(conn, num, name):
    # prepare query and data
    query = """ UPDATE Department
                SET DepartmentName = %s
                WHERE DepartmentNo = %s """

    data = (name, num)

    try:
        cursor = conn.cursor()
        cursor.execute(query, data)

        conn.commit()

    except Error as error:
        print(error)

def view_all(conn):
    #creates function called view_all
    try:
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


if __name__ == '__main__':
    conn = connect()
    update(conn, 'L028', 'Recruitment')
    #updates record with information listed above
    view_all(conn)
