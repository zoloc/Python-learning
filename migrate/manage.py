from flask_script import Manager
from migrate_demo import app
from flask_migrate import MigrateCommand, Migrate
from exts import db
from models import Article

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


