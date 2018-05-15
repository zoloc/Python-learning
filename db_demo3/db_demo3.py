from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=True)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text, nullable=True)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = db.relationship('Users', backref=db.backref('articles'))

db.create_all()

@app.route('/')
def index():
    # 先添加一个新user用来添加新文章
    # user1 = Users(username = 'Zac')
    # db.session.add(user1)
    # db.session.commit()

    # 再添加一片新文章
    # article1 = Article(title = 'title1', content = 'content1', author_id = 1)
    # db.session.add(article1)
    # db.session.commit()

    # 找标题为aaa的作者
    # 复杂方法：
    # article = Article.query.filter(Article.title == 'title1').first()
    # author_id = article.author_id
    # user = Users.query.filter(Users.id == author_id).first()
    # print(user.username)
    # 简单方法：
    # 在Article类中加入author = db.relateionship('Users', backref=db.backref('articles'))
    # article = Article(title = 'title1', content='content1')
    # article.author = Users.query.filter(Users.id == 1).first()
    # db.session.add(article)
    # db.session.commit()
    article = Article.query.filter(Article.title == 'title1').first()
    print(article.author.username)
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)
