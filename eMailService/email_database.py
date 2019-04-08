from pymysql import connect, IntegrityError
from datetime import datetime

def open_connection():

    connection = connect(host='host',user='user',password='password',db='database')
    return connection

def insert(connection,email,message):

    cursor = connection.cursor()
    send_datetime = datetime.now()
    cursor.execute('INSERT INTO users_emails VALUES ("{}")'.format(email))
    cursor.execute('INSERT INTO messages (email,message,datetime) VALUES("{}","{}", "{}")'.format(email,message,send_datetime.strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()

def close_connection(connection):

    connection.close()
