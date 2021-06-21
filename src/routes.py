from src import app
from src.models import Message
from flask import render_template, send_from_directory, request, redirect, flash
from src import db
from datetime import datetime
from src.utils import utc2local

@app.errorhandler(500)
def internal_error(error):
    return render_template("error-page.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error-page.html")


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/")
@app.route("/home")
@app.route("/index")
def home_page():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        messg = Message(name=request.form['name'], email=request.form['email'], sent_date=datetime.utcnow(), message=request.form['message'])
        try:
            db.session.add(messg)
            db.session.commit()
            flash('Message Sent successfully!', 'success')
            return redirect('contact')
        except:
            flash('Sorry! there was an error.','danger')
            return redirect("/contact")
    return render_template("contact.html")


@app.route("/admin/dashboard", methods=['GET', 'POST'])
def admin_dashboard_page():
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
            return redirect('/admin/dashboard')


@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    return "Admin logged in successfull!"