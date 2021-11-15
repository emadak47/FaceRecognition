from src.DB import DB

#all time data is giving me problems when converting from mysql output --> jsonify(mysql query output)
#so i have removed it for now
class Transaction(DB):
    def __init__(self, customer_id):
        DB.__init__(self)
        self.customer_id = customer_id

    def get_tx(self):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_date
                -- T.creation_time,
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {}
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id)
        return self.read(query)

    def get_tx_by_day(self, day):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      DAY(T.creation_date) = {}
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, day)
        return self.read(query)

    def get_tx_by_month(self, month):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      MONTH(T.creation_date) = {}
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, month)
        return self.read(query)

    def get_tx_by_year(self, year):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      YEAR(T.creation_date) = {}
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, year)
        return self.read(query)

    def get_tx_between_dates(self, date1, date2):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      T.creation_date BETWEEN "{}" AND "{}"
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, date1, date2)
        return self.read(query)

    def get_tx_after_date(self, date):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      T.creation_date >= "{}"
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, date)
        return self.read(query)

    def get_tx_before_date(self, date):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      T.creation_date <= "{}"
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, date)
        return self.read(query)

    def get_tx_to_merchant(self, merchant_id):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      T.merchant_id = {}
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, merchant_id)
        return self.read(query)

    def get_tx_to_merchant_between_dates(self, merchant_id, date1, date2):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      T.merchant_id = {} AND
                      T.creation_date BETWEEN "{}" AND "{}"
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, merchant_id, date1, date2)
        return self.read(query)

    def get_tx_to_merchant_after_date(self, merchant_id, date):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      T.merchant_id = {} AND
                      T.creation_date >= "{}"
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, merchant_id, date)
        return self.read(query)

    def get_tx_to_merchant_before_date(self, merchant_id, date):
        query = """
                SELECT T.account_no, T.merchant_id, T.amount, T.description, T.creation_time, T.creation_date
                FROM Transaction T, Account A
                WHERE T.account_no = A.account_no AND
                      A.customer_id = {} AND
                      T.merchant_id = {} AND
                      T.creation_date <= "{}"
                ORDER BY T.creation_date DESC, T.creation_time DESC;
        """.format(self.customer_id, merchant_id, date)
        return self.read(query)
