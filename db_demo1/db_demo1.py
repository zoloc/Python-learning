from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

#articletable:
#create table articl(
#    id int primary key autoincrement,
#    title varchar(100) not null,
#    content text not null,
#)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/')
def hello_world():
    # article1 = Article.query.filter(Article.content == 'bbb').first()
    # db.session.delete(article1)
    # db.session.commit()


    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug= True)
