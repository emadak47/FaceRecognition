from flask import Flask, redirect, url_for, render_template, request
from src.utils import get_latest_customer_id
from face_capture import faceCapture
from faces import login_system
from train import train
from src.Customer import Customer
from src.Log import Log
from src.Account import Account
app = Flask(__name__)

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
    return render_template('profile.html', data = data)


@app.route('/signup/', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        result = request.form
        username = result['name']

        faceCapture(username, 100)
        train()

        customer_id = get_latest_customer_id()
        customer = Customer(customer_id)
        # customer.insert_new_user(
        #     name_first,
        #     name_last,
        #     email,
        #     password,
        #     address_city, 
        #     address_street,
        #     address_flat_no,
        #     address_country
        # )
        log = Log(customer_id)
        log.insert_log()

        return redirect(url_for('index', message = "Signed Up successfully"))

    return render_template('signup.html')

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        customer_id = login_system()
        if(customer_id != -1):
            return redirect(url_for('profile', customer_id = customer_id))
        else:
            return render_template('index.html', message = login_string)

    if request.args:
        message = request.args['message']
        return render_template('index.html', message = message)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)
