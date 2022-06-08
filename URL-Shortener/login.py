# TAKES CARE OF ADDING USERS TO DATABASE AND LOGGING IN

from datetime import datetime
import constants
import psycopg2
from psycopg2 import Error
from getpass import getpass

def startup_login():
    start = input('1. Create User\t2. Login   ')

    if start == '1': create_user()
    elif start == '2': login()
    else:
        print('--- INCORRECT RESPONSE ---\n\n')

def create_user():
    username = input("Create a username: ")
    password = input("Create a password: ")

    postgres_insert_query="""INSERT INTO users (username, password, last_login) VALUES (%s, %s, %s)"""
    record_to_insert = (username, password, datetime.now().strftime("%H:%M:%S"))
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    print('--- User Created ---')

def login():
    username_input = input("Username: ")
    cursor.execute("SELECT password FROM users WHERE username='"+username_input+"'")
    result = cursor.fetchone()

    if result == None:
        print('--- User Does Not Exist {Try Sign In} ---\n')
        startup_login()

    password = getpass()

    if password == result[0]:
        print('--- successfully logged in ---')
    else:
        print('--- incorrect credentials ---')
        login()


if __name__=='__main__':
    try:
        connection = psycopg2.connect(user='postgres',password=constants.SQL_PASS,host=constants.HOST_IP,port='5432', database=constants.SQL_DATABASE)
        cursor = connection.cursor()

        startup_login()

    except (Exception, psycopg2.Error) as error:
        print(error)
