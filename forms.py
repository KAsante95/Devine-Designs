from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, FileField
from flask_wtf import FlaskForm
 
class ContactForm(FlaskForm):
  first_name = TextField("First Name: ", [validators.DataRequired()])
  last_name = TextField("Last Name: ", [validators.DataRequired()])
  email = TextField("Email: ", [validators.DataRequired(), validators.Email()])
  occasion = SelectField("Occasion: ", choices = [("Wedding", "Wedding"), ("Prom", "Prom"), ("Party", "Party"), ("Church", "Church"), ("Casual", "Casual")])
  message = TextAreaField("Message: ", [validators.DataRequired()])
  attachment = FileField("Attachment(s): ")
  submit = SubmitField("Send")

class InfoForm(FlaskForm):
  first_name = TextField("First Name: ", [validators.DataRequired()])
  last_name = TextField("Last Name: ", [validators.DataRequired()])
  email = TextField("Email: ", [validators.DataRequired(), validators.Email()])
  experience = SelectField("Experience: ", choices = [("A lot of Experience", "A Lot of Experience"), ("Some Experince", "Some Experince"), ("Little Experience", "Little Experience"), ("No Experience", "No Experience")])
  submit = SubmitField("Sign Up")

class SignupForm(FlaskForm):
  message = TextAreaField("Message: ", [validators.DataRequired()])
  class_lvl = SelectField("Class Selection: ", choices = [("beginner", "Beginner Classes - $640"),("intermediate", "Intermediate Classes - $800")])



