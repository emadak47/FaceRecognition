from src.DB import DB

# Assuming that username is unique
def get_user_id_from_name(name_first):
    db = DB()
    query = """
            SELECT customer_id
            FROM Customer
            WHERE name_first = "{}";
    """.format(name_first)
    response = db.read(query)
    if response is None:
        return -1
    else:
        return response[0]['customer_id']

def get_user_id_from_email(email):
    db = DB()
    query = """
            SELECT customer_id
            FROM Customer
            WHERE email = "{}";
    """.format(email)
    response = db.read(query)
    if response is None:
        return -1
    else:
        return response[0]['customer_id']


def get_latest_customer_id():
    db = DB()
    query = """
            SELECT MAX(customer_id) AS Latest
            FROM Customer;
    """
    response = db.read(query)
    return response[0]['Latest'] + 1


def get_latest_account_no():
    db = DB()
    query = """
            SELECT MAX(account_no) AS Latest
            FROM Account;
    """
    response = db.read(query)
    return response[0]['Latest'] + 1
