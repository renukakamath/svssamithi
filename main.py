from flask import * 
from public import public
from admin import admin
from customer import customer


import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail



app=Flask(__name__)




app.secret_key='key'


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(customer,url_prefix='/customer')


mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'renukakamath2@gmail.com'
app.config['MAIL_PASSWORD'] = 'znwpqhzlelrsfudi'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


if __name__ == '__main__':
  app.run(debug=True)
  
# test