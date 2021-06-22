from src import app
from src.models import Message
from flask import render_template, send_from_directory, request, redirect, flash, url_for
from src import db
from datetime import datetime
from src.forms import ContactForm


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/home")
@app.route("/index")
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    form = ContactForm()

    if form.validate_on_submit():
        messg = Message(name=form.name.data, email=form.email.data, sent_date=datetime.utcnow(), message=form.message.data)
        try:
            db.session.add(messg)
            db.session.commit()
            flash('Message Sent successfully!', 'success')
            return redirect(url_for('contact_page'))
        except:
            flash('Sorry! there was an error.','danger')
            return redirect(url_for("contact_page"))
    
    return render_template("contact.html", form = form )


@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    return "Admin logged in successfull!"