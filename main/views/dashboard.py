"""Dashboard business logic."""
from flask import Blueprint, render_template
from main.models import Post

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route('/')
def dashboard():
    """Dashboard business logic."""
    posts = Post.query.all()
    return render_template('dashboard.html', posts=posts)
