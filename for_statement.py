# encoding: utf-8
from flask import Flask, render_template

app = Flask(__name__)


#for遍历字典

@app.route('/')
def index():
    user = {
        'username': 'Zac',
        'age': 20
    }
    return render_template('index.html', user = user)

if __name__ == '__main__':
    app.run(debug=True)