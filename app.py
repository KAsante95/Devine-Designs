from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from forms import ContactForm, SignupForm, InfoForm
from flask.ext.mail import Message, Mail
import os
from werkzeug import secure_filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import shutil

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
	img_files = "IMG_0001.JPG           IMG_0002.JPG \
IMG_0003.JPG		IMG_0046.jpeg \
IMG_0047.JPG        IMG_0053.jpg       IMG_0029.JPG \
IMG_0025.jpg		IMG_0048.JPG \
IMG_00042.JPG		IMG_0026.jpeg \
IMG_0051.jpg		IMG_0050.JPG        IMG_0005.JPG \
IMG_00062.JPG		IMG_0045.jpeg		IMG_0052.JPG"
	img = "IMG_0054.JPG        IMG_0008.PNG        IMG_0024.jpeg \
	IMG_0009.jpg    IMG_0017.JPG        IMG_0016.JPG        IMG_0036.JPG       IMG_0014.JPG"
	im = "IMG_0013.jpg		IMG_0011.JPG \
IMG_0038.JPG  IMG_00072.JPG \
IMG_0032.jpeg \
IMG_0039.JPG       IMG_0041.JPG \
IMG_0034.JPG		 \
IMG_0019.jpeg	   IMG_0020.jpeg \
IMG_0040.JPG \
IMG_0037.JPG"
	i = "IMG_0018.jpeg      IMG_2622.JPG    IMG_0015.JPG		IMG_0012.JPG		 \
IMG_0033.jpeg	   IMG_0042.JPG \
IMG_0044.jpeg"
	images = img_files.split()
	imgs = img.split()
	ims = im.split()
	igs = i.split()
	return render_template("gallery.html", images=images, imgs=imgs, ims = ims, igs = igs)



if __name__ == "__main__":
	app.run() 