from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from forms import ContactForm, SignupForm, InfoForm
from flask_mail import Message, Mail
import os
from werkzeug import secure_filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import shutil
import requests
import json
from collections import OrderedDict

mail = Mail()

app = Flask(__name__)

app.config['DEBUG'] = True
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'kasante.asante@gmail.com'
app.config["MAIL_PASSWORD"] = '120295ka'
app.config["UPLOAD_FOLDER"] = 'uploads/'
app.config["ALLOWED_EXTENSIONS"] = set(['txt', 'docx', 'pdf', 'jpg', 'png']); 

mail.init_app(app)

@app.route("/")
def index():
	return render_template('index.html')
@app.route("/index.html")
def front():
	return render_template('index.html')

@app.route("/about.html")
def about():
	return render_template('about.html')

@app.route("/fabrics.html")
def fabrics():
	return render_template('fabrics.html')

app.secret_key = 'development key'

@app.route("/whats_new.html", methods=["GET", "POST"])
def wnew():
	form = InfoForm()

	if request.method == "POST":
		if form.validate() == False:
			flash('All fields are required')
			return render_template("/whats_new.html", form=form)
		else:
			msg = Message("Interest in Sewing Classes", sender=form.email.data, recipients=['kasante.asante@gmail.com'])
			msg.body = """From: %s %s <%s> %s""" % (form.first_name.data, form.last_name.data, form.email.data, form.experience.data)
			mail.send(msg)
			return redirect("/signup.html", form = SignupForm())
 
	elif request.method == "GET":
		return render_template("/whats_new.html", form=form)
	#return render_template('whats_new.html')

@app.route("/pricing.html")
def pricing():
	return render_template('pricing.html')

@app.route("/signup.html", methods=["GET", "POST"])
def signup():
	form = SignupForm()
	#email not actually sent
	if request.method == "POST":
		#msg = Message("Interest in Sewing Classes", sender=form.email.data, recipients=['kasante.asante@gmail.com'])
		#msg.body = """From: %s %s\n<%s>\nExperience: %s""" % (form.first_name.data, form.last_name.data, form.email.data, form.experience.data)
		#mail.send(msg)
		return redirect("/whats_new.html", form=form)
 
	elif request.method == "GET":
		return render_template("/signup.html", form=form)


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
  form = ContactForm()
 
  if request.method == "POST":
  	if form.validate() == False:
		flash('All fields are required')
		return render_template("/contact.html", form=form)
	else:
	  	msg = Message("Contact from "+ form.first_name.data + " "+ form.last_name.data, sender=form.email.data, recipients=['kasante.asante@gmail.com'])
		msg.body = """From: %s %s <%s>\nOccasion: %s\nMessage: %s""" % (form.first_name.data, form.last_name.data,form.email.data, form.occasion.data,form.message.data)
		#form.attachment.save('uploads/'+form.attachment.data)
		#with app.open_resource(form.attachment.data) as fp:
		#file = os.path.abspath(form.attachment.data)
		#filename = secure_filename(file)
		#path = app.config["UPLOAD_FOLDER"]
		#shutil.copy(file, path)
		#msg.attach(file, file.read())
		mail.send(msg)
		return render_template("/contact.html", form=form)
 
  elif request.method == "GET":
    return render_template("/contact.html", form=form)



@app.route("/gallery.html")
def gallery():
	images = {}
	links = []

	r = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=2290774988.d227555.44c8e8c438634ddbb00531841909375a')
	json = r.json()
	i = 0
	while i < len(json["data"]):
		images[json["data"][i]["images"]["standard_resolution"]["url"]] = json["data"][i]["link"]
		links.append(json["data"][i]["link"])
		i += 1
		images = OrderedDict(sorted(images.items(), key=lambda t: t[-1], reverse=True))




	return render_template("gallery.html", images=images)



if __name__ == "__main__":
	app.run() 
