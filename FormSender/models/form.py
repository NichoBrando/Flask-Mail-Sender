from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class FormContact(FlaskForm):
    senderMail = StringField('Email', validators = [DataRequired()])
    senderPasswd = PasswordField('Password', validators = [DataRequired()])
    subject = SelectField('Subject', choices = [('', ''),
     ('Report','Report Message'),
     ('Gratefulness', 'Gratefulness Message'),
     ('Friendly', 'Friendly Message')],
     validators = [DataRequired()])
    targetMail = StringField('To', validators = [DataRequired()])
    text = TextAreaField('message', validators = [DataRequired()])
