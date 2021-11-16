from src.DB import DB

class Account(DB):
    def __init__(self, customer_id):
        DB.__init__(self)
        self.customer_id = customer_id

    def get_accounts(self):
        query = """
                SELECT account_no
                FROM Account
                WHERE customer_id = {}
        """.format(self.customer_id)
        response = self.read(query)
        return [record['account_no'] for record in response]

    def get_account_branches(self):
        query = """
                SELECT A.account_no, B.branch_id, B.location
                FROM Account A, Branch B
                WHERE A.branch_id = B.branch_id AND
                      A.customer_id = {};
        """.format(self.customer_id)
        return self.read(query)

    # ASSUMPTION: ONE CURRENT ACCOUNT PER PERSON
    def get_current_balance(self):
        query = """
                SELECT SUM(balance) AS Balance
                FROM CurrentAccount CA, (
                    SELECT account_no
                    FROM Account
                    WHERE customer_id = {}
                ) T1
                WHERE CA.account_no = T1.account_no;
        """.format(self.customer_id)
        return self.read(query)

    def get_savings_balance(self):
        query = """
                SELECT SUM(SA.balance) AS balance, SA.currency
                FROM SavingsAccount SA, (
                    SELECT account_no
                    FROM Account
                    WHERE customer_id = {}
                ) T1
                WHERE SA.account_no = T1.account_no
                GROUP BY SA.currency;
        """.format(self.customer_id)
        return self.read(query)

    def get_current_account_info(self):
        query = """
                SELECT A.account_no, B.location, 'Current' AS 'type', CA.balance, 'HKD' AS currency
                FROM Account A, Branch B, CurrentAccount CA
                WHERE A.branch_id = B.branch_id
                AND A.customer_id = {}
                AND A.account_no = CA.account_no;
        """.format(self.customer_id)
        return self.read(query)

    def get_savings_account_info(self):
        query = """
                SELECT A.account_no, B.location, 'Savings' AS 'type', SA.balance, SA.currency
                FROM Account A, Branch B, SavingsAccount SA
                WHERE A.branch_id = B.branch_id
                AND A.customer_id = {}
                AND A.account_no = SA.account_no;
        """.format(self.customer_id)
        return self.read(query)

    def get_accounts_and_type(self):
        print("here")
        query = """
        SELECT A.account_no, (SELECT IF(
        (SELECT EXISTS(SELECT * FROM CurrentAccount CA WHERE CA.account_no = A.account_no) as existsOrNot),
        'Current Account', 'Savings Account') Account_Type) Account_type
        FROM Account A
        WHERE customer_id = {};
        """.format(self.customer_id)
        return self.read(query)

    def insert_new_account(self, account_no):
        query1 = """
                INSERT INTO `Account` VALUES ({}, {}, {});
        """.format(
            account_no,
            self.customer_id,
            2
        )
        self.write(query1)

        query2 = """
                INSERT INTO `Account` VALUES ({}, {}, {});
        """.format(
            account_no + 1,
            self.customer_id,
            2
        )
        self.write(query2)

        query3 = """
                INSERT INTO `SavingsAccount` VALUES ({}, {}, "{}");
        """.format(
            account_no + 1,
            0,
            "HKD"
        )
        self.write(query3)

        query4 = """
                INSERT INTO `CurrentAccount` VALUES ({}, {});
        """.format(
            account_no,
            0
        )
        self.write(query4)
