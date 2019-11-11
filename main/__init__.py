from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://enilcqpnnvivrd:9e1f93cf1c67489a93a2b856d48c1b84a78d5338992d29d5d984d309bcb28812@ec2-54-197-238-238.compute-1.amazonaws.com:5432/d7h77110l6d2fi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_shhh'

db = SQLAlchemy(app)
from main.models import Post
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))


from main.views import dashboard_bp, post_bp
app.register_blueprint(dashboard_bp)
app.register_blueprint(post_bp)
