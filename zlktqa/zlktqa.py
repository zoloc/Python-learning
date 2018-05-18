from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User
from exts import db
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            #如果想在31天内都不需要登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '手机或者密码错误，请重试'


@app.route('/regist/', methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该手机已被注册'
        else:
            if password1 != password2:
                return '两次密码不相等，请重试'
            else:
                user = User(telephone=telephone, username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))

@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        pass


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id') #这里不用session['user_id']为了避免抛出异常
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            print(user)
            return {'user':user}
    return {}


if __name__ == '__main__':
    app.run()
