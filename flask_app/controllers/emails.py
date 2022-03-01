from pydoc import render_doc

from flask import render_template
from flask_app import app
from flask_app.models.email import Email
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/email', methods=['POST'])
def create_email():
    if Email.validate_email(request.form):
        Email.save_email(request.form)
        print(request.form)
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def show_all_emails():
    return render_template('success.html', emails=Email.show_emails())

