from flask import Blueprint, request, render_template
from flask_wtf import form
from src.forms import LoginForm as loginform
from werkzeug.security import check_password_hash, generate_password_hash, gen_salt

auth = Blueprint('auth', __name__ , url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        print("logged in")

    return render_template("login.html")

@auth.route("/register", methods=['GET', 'POSt'])
def user_register():
    if request.method == 'POST':
        print("user registered")
    
    return render_template("signup.html")
