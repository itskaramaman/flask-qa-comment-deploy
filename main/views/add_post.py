"""Add Post business logic."""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from main import db
from main.forms import AddPost
from main.models import Post

post_bp = Blueprint('post_bp', __name__)


@post_bp.route('/post', methods=['GET', 'POST'])
def add_post():
    """Add Post view."""
    form = AddPost(request.form)
    if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            new_post = Post(title, content)
            db.session.add(new_post)
            try:
                db.session.commit()
                flash('Comments are posted successfully', 'success')
                return redirect(url_for('dashboard_bp.dashboard'))
            except:
                flash('Comments couldn\'t got posted', 'danger')
                return render_template('add_posts.html', form=form)
    return render_template('add_posts.html', form=form)
