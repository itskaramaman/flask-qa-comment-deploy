from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vjwqqednitmzbt:b7c62297c87d2f2e2d5eb990f5deea63ed9de9b973feaece0197300ef432520f@ec2-174-129-253-47.compute-1.amazonaws.com:5432/d94ljkebh92d46'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_shhh'

db = SQLAlchemy(app)
from main.models import Post
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))


from main.views import dashboard_bp, post_bp
app.register_blueprint(dashboard_bp)
app.register_blueprint(post_bp)
