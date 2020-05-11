from FormSender import app
from flask import render_template, redirect
from FormSender.controllers.mailSender import reportMail
from FormSender.models.form import FormContact
@app.route("/", methods = ["GET", "POST"])
def index(status = 0):
    form = FormContact()
    if form.validate_on_submit():
        status = reportMail(form.senderMail.data, form.senderPasswd.data,
         form.targetMail.data, form.subject.data, form.text.data)
        return render_template('contato.html', form = form, status = status)
    return render_template('contato.html', form = form, status = status)
