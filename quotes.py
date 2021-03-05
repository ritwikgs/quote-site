from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:yourpassword@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gtcmbepdxkfwcp:fb2acd45f68b78acc84194e8fc7bbb49293582e0adfa8fa967aabc14a7b592c8@ec2-54-166-242-77.compute-1.amazonaws.com:5432/dafpdsqrjherp2'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html') 

@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))