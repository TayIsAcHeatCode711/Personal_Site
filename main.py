
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from wtforms.widgets import TextArea
from wtforms_bootstrap5 import renderers
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired
import requests
from hidden import key

app = Flask(__name__)
app.config['SECRET_KEY'] = key

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contacts",methods=['GET','POST'])
def contacts():
    mycontacts=MyForm()
    return render_template('contacts.html',form=mycontacts)
@app.route("/resume")
def resume():
    return render_template('resume.html')
@app.route("/about_me")
def about_me():
    return render_template('about_me.html')

class MyForm(FlaskForm):
    fname = (StringField('First Name', validators=[DataRequired()]))
    lname = (StringField('Last Name', validators=[DataRequired()]))
    phone = (StringField('Phone', validators=[DataRequired()]))
    email = (StringField('Email', validators=[DataRequired()]))
    message = (StringField('Leave me a message!', validators=[DataRequired()]))
    submit = (SubmitField('Submit', validators=[DataRequired()]))
if __name__ == '__main__':
    app.run(debug=True)
