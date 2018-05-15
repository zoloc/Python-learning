from flask import Flask, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def hello_world():
    session['username'] = 'Zac'
    session.permanent = True
    return 'Hello World!'

@app.route('/get/')
def get():
    return session.get('username')

@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success'

if __name__ == '__main__':
    app.run()
