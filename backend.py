from flask import Flask, redirect, url_for, render_template, request
from src.utils import get_latest_customer_id, get_user_id_from_email, get_latest_account_no
from face_capture import faceCapture
from faces import login_system
from train import train
from src.Customer import Customer
from src.Log import Log
from src.Account import Account
from src.Transaction import Transaction
from flask import jsonify
app = Flask(__name__)

@app.route('/login_history/<int:customer_id>')
def login_history(customer_id):
    customer = Customer(customer_id)
    customer_data = customer.get_user_details()

    customer_log = Log(customer_id)
    customer_log_history = customer_log.get_log_history()

    data = [customer_data[0], customer_log_history]
    return render_template('login_history.html', data = data)

@app.route('/account_settings/<int:customer_id>' ,methods=['POST','GET'])
def account_settings(customer_id):
    customer = Customer(customer_id)
    if request.method == 'POST':
        result = request.form
        customer.edit_user_details(
            result['email'],
            result['password'],
            result['address_flat_no'],
            result['address_street'],
            result['address_city'],
            result['address_country']
        )
        phone_numbers = result['phone_numbers'].split()
        customer.edit_user_phone(phone_numbers)


    customer_data = customer.get_user_details()

    customer_log = Log(customer_id)
    customer_log_history = customer_log.get_log_history()

    data = [customer_data[0], customer_log_history]
    return render_template('account_settings.html', data = data)


@app.route('/profile/<int:customer_id>')
def profile(customer_id):
    customer = Customer(customer_id)
    customer_data = customer.get_user_details()

    customer_log = Log(customer_id)
    customer_log_history = customer_log.get_log_history()

    customer_accounts = Account(customer_id)
    customer_current_account_info = customer_accounts.get_current_account_info()
    customer_savings_account_info = customer_accounts.get_savings_account_info()
    customer_accounts_info = customer_current_account_info + customer_savings_account_info

    data = [customer_data[0], customer_log_history, customer_accounts_info]
    if request.args:
        data.append({'message': True})

    return render_template('profile.html', data = data)


@app.route('/signup/', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        result = request.form

        faceCapture(result['name'].split()[0], 100)
        train()

        customer_id = get_latest_customer_id()
        customer = Customer(customer_id)
        customer.insert_new_user(
            result['name'].split()[0],
            result['name'].split()[1],
            result['email'],
            result['password'],
            result['city'],
            result['street'],
            result['apartment'],
            result['country']
        )

        log = Log(customer_id)
        log.insert_log()

        account_id = get_latest_account_no()
        account = Account(customer_id)
        account.insert_new_account(account_id)

        return redirect(url_for('index', message = "Signed Up successfully"))

    return render_template('signup.html')

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        if not request.form:  #face-id login
            customer_id = login_system()
            if(customer_id != -1):
                return redirect(url_for('profile', customer_id = customer_id, message = True))
            else:
                return render_template('index.html', message = "Failed Login")
        else:   #normal login
            credentials = request.form
            customer_id = get_user_id_from_email(credentials['email'])
            if customer_id != -1:
                customer = Customer(customer_id)
                login = customer.get_login_details(credentials['email'], credentials['password'])
                if login:
                    log = Log(customer_id)
                    log.insert_log()
                    return redirect(url_for('profile', customer_id = customer_id, message = True))
                else:
                    return render_template('index.html', message = "Failed Login")
            else:
                return render_template('index.html', message = "Failed Login")

    if request.args:
        message = request.args['message']
        return render_template('index.html', message = message)
    else:
        return render_template('index.html')

@app.route('/transactions/<int:customer_id>/<int:account_no>', methods = ['POST','GET'])
def transactionsWithAccount(customer_id, account_no):
    return redirect(url_for('transactions', customer_id = customer_id, account_no=account_no) )

@app.route('/transactions/<int:customer_id>', methods = ['POST','GET'])
def transactions(customer_id, account_no=None):
    customer_log = Log(customer_id)
    customer = Customer(customer_id)
    customer_data = customer.get_user_details()
    customer_log_history = customer_log.get_log_history()
    data = [customer_data[0], customer_log_history]

    return render_template('transactions.html', data = data)


@app.route('/transactionsBackend/<int:customer_id>', methods=['GET', 'POST'])
def retreiveTxData(customer_id):
    # GET request
    if request.method == 'GET':
        newTransaction = Transaction(customer_id)
        transactions = newTransaction.get_tx_by_amount({"test":"value"});
        return {'data':transactions}

    # POST request
    if request.method == 'POST':
        data = request.get_json()
        newTransaction = Transaction(customer_id)
        transactions = newTransaction.get_tx(data);
        return {'data':transactions}

@app.route('/getAccounts/<int:customer_id>', methods=['GET', 'POST'])
def getAccountsAndTypes(customer_id):
    if request.method == 'POST':
        customer_accounts = Account(customer_id)
        accountTypes = customer_accounts.get_accounts_and_type()
        return {'data': accountTypes}


if __name__ == '__main__':
    app.run(debug = True)
