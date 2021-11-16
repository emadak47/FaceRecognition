from os import name
from src.DB import DB

class Customer(DB):
    def __init__(self, customer_id): 
        DB.__init__(self)
        self.customer_id = customer_id
    
    def get_login_details(self, email, password): #login by email and password
        query = """
                SELECT C.customer_id, C.email, C.password
                FROM Customer C
                WHERE C.email = "{}" AND 
                      C.password = "{}" AND 
                      C.customer_id = "{}";
        """.format(email, password, self.customer_id) 
        return self.read(query)

    def get_user_details(self):
        query1 = """
                SELECT *
                FROM Customer C
                WHERE C.customer_id = {};
        """.format(self.customer_id)
        response1 = self.read(query1)
        response1[0]["phone_numbers"] = []

        query2 = """
                SELECT * 
                FROM Phone P
                WHERE customer_id = {}
        """.format(self.customer_id)
        response2 = self.read(query2)

        for record in response2:
            response1[0]['phone_numbers'].append(record['phone_numbers'])
        
        return response1

    def insert_new_user(self, name_first, name_last, email, password, address_city, address_street, address_flat_no, address_country):
        query = """
                INSERT INTO `Customer` VALUES ({}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");
        """.format(
            self.customer_id,
            name_first,
            name_last,
            email,
            password,
            address_city, 
            address_street,
            address_flat_no,
            address_country
        )
        self.write(query)

    def edit_user_details(self, email, password, address_flat_no, address_street, address_city, address_country):
        query = """
                UPDATE Customer
                SET email = '{}', password = '{}', address_flat_no = '{}', 
                address_street = '{}', address_city = '{}', address_country = '{}'
                WHERE customer_id = {};
        """.format(
            email,
            password,
            address_flat_no,
            address_street,
            address_city,
            address_country,
            self.customer_id
        )
        self.write(query)

    def edit_user_phone(self, phone_numbers):
        query = """
                DELETE FROM Phone
                WHERE customer_id = {}
        """.format(self.customer_id)
        self.write(query)

        for index,phone in enumerate(phone_numbers):
            query = """
                    INSERT INTO Phone VALUES({},'{}')
            """.format(self.customer_id, phone)
            self.write(query)
    

    

    