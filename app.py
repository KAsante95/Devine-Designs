from flask import Flask
from flask import render_template
from forms import ContactForm
from forms import SignupForm
from flask import request
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.config['DEBUG'] = True
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'kasante.asante@gmail.com'
app.config["MAIL_PASSWORD"] = '120295ka'

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

@app.route("/whats_new.html")
def wnew():
	return render_template('whats_new.html')

@app.route("/pricing.html")
def pricing():
	return render_template('pricing.html')

@app.route("/signup.html")
def signup():
	form = SignupForm()
	if request.method == "POST":
		msg = Message("Interest in Sewing Classes", sender='kasante.asante@gmail.com', recipients=['kasante.asante@gmail.com'])
		msg.body = """From: %s %s <%s> %s""" % (form.first_name.data, form.last_name.data, form.email.data, form.experience.data)
		mail.send(msg)
		return render_template("https://www.paypal.com/cgi-bin/webscr")
 
	elif request.method == "GET":
		return render_template("/signup.html", form=form)


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
  form = ContactForm()
 
  if request.method == "POST":
  	msg = Message(form.first_name.data, sender='', recipients=['devine.designs6@gmail.com'])
	msg.body = """From: %s <%s> %s""" % (form.first_name.data, form.email.data, form.message.data)
	mail.send(msg)
	return render_template("/contact.html", form=form)
 
  elif request.method == "GET":
    return render_template("/contact.html", form=form)



if __name__ == "__main__":
	app.run() 