import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
load_dotenv()

db_config = {
        # mysql://beb5c38bddd99e:26328889@us-cdbr-east-04.cleardb.com/heroku_12ebac061f78d2f?reconnect=true
        'host': os.getenv('MYSQL_HOST'),
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'database': os.getenv('MYSQL_DB')
    }

class DB:
    def __init__(self):
        self.config = db_config

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
            self.cursor = self.cnx.cursor(dictionary=True)
            #print("Connection Successful")
            #print("Connected to {}".format(self.config['database']))
            return True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User authorization error")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            else:
                print(err)
            return False

    def disconnect(self):
        if self.cnx.is_connected():
            self.cursor.close()
            self.cnx.close()
            #print("Connection closed")

    # use try and catch for fetching and execution
    def read(self, query):
        if self.connect():
            try:
                self.cursor.execute(query)
                response = self.cursor.fetchall()
                self.disconnect()
                return [record for record in response]
            except:
                print("Failed to read")
                self.disconnect()
        else:
            print("Connection Failed")

    # catch and report error
    def write(self, query):
        if self.connect():
            try:
                self.cursor.execute(query)
                self.cnx.commit()
                self.disconnect()
                return True

            except:
                print("Failed to write")
                self.disconnect()
                return False
        else:
            print("Connection Failed")
