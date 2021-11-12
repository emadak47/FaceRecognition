from flask import Flask, redirect, url_for, render_template, request
from src.utils import get_latest_customer_id
from face_capture import faceCapture
from faces import login_system
from train import train
from src.Customer import Customer
from src.Log import Log
from src.Transaction import Transaction
from flask import jsonify
app = Flask(__name__)

@app.route('/signup', methods=['POST','GET'])
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
        login_string = login_system()
        if(login_string == 'Successful Login'):
            return render_template('profile.html')
        else:
            return render_template('index.html', message = login_string)

    if request.args:
        message = request.args['message']
        return render_template('index.html', message = message)
    else:
        return render_template('index.html')

@app.route('/transactions', methods = ['POST','GET'])
def transactions():
    return render_template('transactions.html')

@app.route('/transactionsBackend', methods=['GET', 'POST'])
def retreiveTxData():
    # GET request
    if request.method == 'GET':
        newTransaction = Transaction(1) #using customer_id = 1 for testing
        transactions = newTransaction.get_tx()
        print(transactions)

        # return {'data':[{'data1':'hello'}, {'data2':'bye'}]}
        return {'data':transactions}
        message = [{'greeting':'Hello from Flask!'}]
        return message # serialize and use JSON headers

    # POST request
    if request.method == 'POST': #this doesn't do anything
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

if __name__ == '__main__':
    app.run(debug = True)
