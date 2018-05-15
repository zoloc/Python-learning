from flask import Flask, g, render_template, request
from utils import login_log
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Zac' and password == '1234':
            g.username = 'Zac'
            login_log()
            return '登录成功！'
        else:
            return '帐号密码错误!'

if __name__ == '__main__':
    app.run(debug=True)
login_log()