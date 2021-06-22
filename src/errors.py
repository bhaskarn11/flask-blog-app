from flask import Blueprint, render_template

errors = Blueprint('errors', __name__ )

@errors.app_errorhandler(500)
def internal_error(error):
    return render_template("error-page.html"), 500

@errors.app_errorhandler(404)
def page_not_found(error):
    return render_template("error-page.html"), 404

@errors.app_errorhandler(401)
def unauthorized_error():
    return "<h1> unauthorized access </h1>", 401