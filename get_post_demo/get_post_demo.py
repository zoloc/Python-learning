from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search/')
def search():
    print(request.args)
    return 'search'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return 'post request'
if __name__ == '__main__':
    app.run(debug=True)
