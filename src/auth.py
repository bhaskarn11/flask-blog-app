from os import name
from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.forms import LoginForm, SignupForm
from werkzeug.security import check_password_hash, generate_password_hash, gen_salt

from src.models import Message, AdminUser
from src import db
from src.utils import utc2local


auth = Blueprint('auth', __name__ , url_prefix='/auth')
admin = Blueprint('admin', __name__ , url_prefix='/admin')


@auth.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        print("logged in")

    return render_template("login.html", form = form)


@auth.route("/register", methods=['GET', 'POSt'])
def user_register():
    form = SignupForm()
    if form.validate_on_submit():
        hashPassword = generate_password_hash(form.password.data)
        user = AdminUser(name=form.name.data, email= form.email.data, password=hashPassword)
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
def dashboard_page():
    if request.method == 'GET':
        try:
            messgs = Message.query.all()
            for messg in messgs:
                messg.sent_date = utc2local(messg.sent_date).strftime("%b %d, %Y - %I:%M %p")
        except:
            messg = None
        return render_template("admin-dashboard.html", messages=messgs)
    else:
        if request.args.get('delete'):
            id = int(request.args.get('id'))
            messg = Message.query.filter_by(id=id).first()
            db.session.delete(messg)
            db.session.commit()
            return redirect(url_for('.dashboard_page'))
            
