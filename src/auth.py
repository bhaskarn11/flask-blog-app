from datetime import datetime
from functools import wraps
from flask import Blueprint, request, render_template, redirect, url_for, flash, session, g
from src.forms import LoginForm, SignupForm, AccountUpdateForm
from werkzeug.security import check_password_hash, generate_password_hash

from src.models import Message, AdminUser
from src import db
from src.utils import utc2local


auth = Blueprint('auth', __name__, url_prefix='/auth')
admin = Blueprint('admin', __name__, url_prefix='/admin')


# view decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('auth.user_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# routes
@auth.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = AdminUser.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.password, form.password.data):
                session['user_id'] = user.id
                flash("Logged in successfully!", "success")
                return redirect(url_for("admin.dashboard_page"))
            else:
                flash("Sorry! couldn't login.", "danger")
                return redirect(".user_login")
        except:
            user = None
            flash("Oops! something went.", 'warning')
            return redirect(".user_login")

    return render_template("login.html", form=form)


@auth.route("/logout", methods=['GET'])
def user_logout():
    session.pop('user_id', None)
    flash("Looged out successfully!", 'info')
    return redirect(url_for(".user_login"))


@auth.route("/register", methods=['GET', 'POSt'])
def user_register():
    form = SignupForm()
    if form.validate_on_submit():
        hashPassword = generate_password_hash(form.password.data)
        user = AdminUser(name=form.name.data, email=form.email.data,
                         password=hashPassword, last_login=datetime.utcnow())
        try:
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully!", 'success')
            return redirect(url_for("admin.dashboard_page"))
        except:
            flash("Sorry! couldn't create account!", 'danger')
            return redirect(url_for(".user_register"))

    return render_template("signup.html", form=form)


@admin.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard_page():
    if request.method == 'GET':
        try:
            user = AdminUser.query.get(session['user_id'])
            messgs = Message.query.all()
            for messg in messgs:
                messg.sent_date = utc2local(
                    messg.sent_date).strftime("%b %d, %Y - %I:%M %p")
        except:
            messgs = None

        return render_template("admin-dashboard.html", messages=messgs, user = user)
    else:
        if request.args.get('delete'):
            id = int(request.args.get('id'))
            messg = Message.query.filter_by(id=id).first()
            db.session.delete(messg)
            db.session.commit()
            return redirect(url_for('.dashboard_page'))


@admin.route("/settings", methods=['GET', 'POST'])
def account_settings():
    user = AdminUser.query.get(session['user_id'])
    form = AccountUpdateForm()
    if form.validate_on_submit():
        pass
    return render_template("admin-settings.html",form = form, user = user)
