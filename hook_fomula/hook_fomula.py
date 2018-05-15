from flask import Flask, render_template,g, request, session, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def hello_world():
    print('index')
    return render_template('index.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    print('login')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Zac' and password == '1234':
            session['username'] = 'Zac'
            return '登录成功'
        else:
            return '用户名密码错误'

@app.route('/edit/')
def edit():
    # if hasattr(g, 'username'):
    #     return '修改成功'
    # else:
    #     return redirect(url_for('login'))
    return render_template('edit.html')

#before_request: 在请求前执行
#before_request是在视图函数执行前执行的
#before_request这个函数只是一个装饰器, 他可以把需要设置为钩子函数的代码放到视图函数执行之前来执行

@app.before_request
def my_before_request():
    if session.get('username'):
        g.username = session.get('username')
    print('hello world')




@app.context_processor
def my_context_procesor():
    # username = session.get('username')
    # if username:
    return {'username': 'Zac'}


if __name__ == '__main__':
    app.run(debug=True)