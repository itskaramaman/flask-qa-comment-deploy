from flask import Blueprint, request
from main.forms import RegisterForm

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register')
def register():
	form = RegisterForm(request.form)
	return render_template('register.html', form=form)