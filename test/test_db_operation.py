import os
import mysql.connector
from mysql.connector import errorcode
from src.utils.db_operation import DB
from unittest import TestCase
from dotenv import load_dotenv
load_dotenv()

test_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_TEST_DB'),
    'port': os.getenv('MYSQL_TEST_PORT')
    }

class TestUtils(TestCase):

    def setUp(self):
        self.cnx = mysql.connector.connect(
            host=test_config['host'],
            user=test_config['user'],
            password=test_config['password'],
            port = test_config['port']
        )
        self.cursor = self.cnx.cursor()
        
        try:
            self.cursor.execute("DROP DATABASE {}".format(test_config['database']))
            self.cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(test_config['database'], err))

        self.cursor = self.cnx.cursor()
        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(test_config['database']))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

        # connection to test_DB is established
        self.db = DB(test_config)

    def test_create_table(self):
        self.create_table_query = """CREATE TABLE `Customer` (
                                    `customer_id` int NOT NULL,
                                    `name` varchar(50) NOT NULL,
                                    `login_time` time NOT NULL,
                                    `login_date` date NOT NULL
                            ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """
        
        self.create_table_response = self.db.write(self.create_table_query)
        self.assertEqual(self.create_table_response, True)

    def test_create_record(self):
        self.create_table_query = """CREATE TABLE `Customer` (
                                    `customer_id` int NOT NULL,
                                    `name` varchar(50) NOT NULL,
                                    `login_time` time NOT NULL,
                                    `login_date` date NOT NULL
                            ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """
        
        self.create_table_response = self.db.write(self.create_table_query)
        self.assertEqual(self.create_table_response, True)
        
        self.insert_record_query = """INSERT INTO `Customer` VALUES (1, "JACK", NOW(), '2021-10-29')"""
        self.insert_record_response = self.db.write(self.insert_record_query)
        self.assertEqual(self.insert_record_response, True)

    def test_read_record(self):
        self.create_table_query = """CREATE TABLE `Customer` (
                                    `customer_id` int NOT NULL,
                                    `name` varchar(50) NOT NULL,
                                    `login_time` time NOT NULL,
                                    `login_date` date NOT NULL
                            ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """
        
        self.create_table_response = self.db.write(self.create_table_query)
        self.assertEqual(self.create_table_response, True)
        
        self.insert_record_query = """INSERT INTO `Customer` VALUES (1, "JACK", NOW(), '2021-10-29')"""
        self.insert_record_response = self.db.write(self.insert_record_query)
        self.assertEqual(self.insert_record_response, True)
        
        self.read_record_query = """SELECT `name` FROM Customer WHERE `customer_id` = 1;"""
        self.read_record_response = self.db.read(self.read_record_query)[0][0]
        self.assertEqual(self.read_record_response, 'JACK')

        self.read_record_query = """SELECT `login_date` FROM Customer WHERE `customer_id` = 1;"""
        self.read_record_response = self.db.read(self.read_record_query)[0][0]
        self.assertEqual(str(self.read_record_response), '2021-10-29')

    def tearDown(self):
        self.cnx = mysql.connector.connect(
            host=test_config['host'],
            user=test_config['user'],
            password=test_config['password']
        )
        self.cursor = self.cnx.cursor()

        # drop test database
        try:
            self.cursor.execute("DROP DATABASE {}".format(test_config['database']))
            #self.cursor.execute("SHOW DATABASES;")
            self.cnx.commit()
            self.cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exist. Dropping db failed".format(test_config['database']))
        self.cnx.close()
