from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
 
class ContactForm(Form):
  first_name = TextField("First Name: ")
  last_name = TextField("Last Name: ")
  email = TextField("Email: ")
  occasion = SelectField("Occasion: ", choices = [("Wedding", "Wedding"), ("Prom", "Prom"), ("Party", "Party"), ("Church", "Church"), ("Casual", "Casual")])
  message = TextAreaField("Message: ")
  submit = SubmitField("Send")

class SignupForm(Form):
  first_name = TextField("First Name: ")
  last_name = TextField("Last Name: ")
  email = TextField("Email: ")
  experience = SelectField("Experience: ", choices = [("A lot of Experience", "A Lot of Experience"), ("Some Experince", "Some Experince"), ("Little Experience", "Little Experience"), ("No Experience", "No Experience")])