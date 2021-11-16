from src.DB import DB

class Log(DB): 
    def __init__(self, customer_id): 
        DB.__init__(self)
        self.customer_id = customer_id

    def insert_log(self):
        query = """
                INSERT INTO `LogHistory` VALUES ({}, CURTIME(), CURDATE());
        """.format(self.customer_id)
        self.write(query)
    
    def get_log_history(self):
        query = """
                SELECT LH.customer_id, LH.login_time, LH.login_date
                FROM LogHistory LH
                WHERE LH.customer_id = {}
                ORDER BY LH.login_date DESC;
        """.format(self.customer_id)
        return self.read(query) 

    def get_log_history_by_day(self, day):
        query = """
                SELECT LH.customer_id, LH.login_time, LH.login_date
                FROM LogHistory LH
                WHERE LH.customer_id = {} AND 
                      DAY(LH.login_date) = {}
                ORDER BY LH.login_date DESC;
        """.format(self.customer_id, day)
        return self.read(query)

    def get_log_history_by_month(self, month):
        query = """
                SELECT LH.customer_id, LH.login_time, LH.login_date
                FROM LogHistory LH
                WHERE LH.customer_id = {} AND 
                      MONTH(LH.login_date) = {}
                ORDER BY LH.login_date DESC;
        """.format(self.customer_id, month)
        return self.read(query)
    
    def get_log_history_by_year(self, year):
        query = """
                SELECT LH.customer_id, LH.login_time, LH.login_date
                FROM Log_History LH
                WHERE LH.customer_id = {} AND 
                      YEAR(LH.login_date) = {}
                ORDER BY LH.login_date DESC;
        """.format(self.customer_id, year)
        return self.read(query)