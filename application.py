from flask import Flask, render_template

app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/payments",methods=['GET', 'POST'])
def payments():
    return render_template('payments.html')
