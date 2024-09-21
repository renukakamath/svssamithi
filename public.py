from flask import *
from database import*

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail



public=Blueprint('public',__name__)

@public.route('/',methods=['post','get'])
def index():
    data={}
    from cryptography.fernet import Fernet
    if "submit" in request.form:
       
        u = request.form['name']
        p = request.form['email']
        n = request.form['number']
        m = request.form['message']
        
        
        cipher_key = Fernet.generate_key()  
        cipher = Fernet(cipher_key)
        
       
        encrypted_name = cipher.encrypt(u.encode()).decode('utf-8')
        encrypted_email = cipher.encrypt(p.encode()).decode('utf-8')
        encrypted_number = cipher.encrypt(n.encode()).decode('utf-8')
        encrypted_message = cipher.encrypt(m.encode()).decode('utf-8')
        
      
        q = "INSERT INTO contactus VALUES (null, '%s', '%s', '%s', '%s','%s')" % (encrypted_name, encrypted_email, encrypted_number, encrypted_message,cipher_key.decode('utf-8'))
        insert(q)
        
       
        flash("Message Sent Successfully")
        
       
        return redirect(url_for('public.index'))

  

    
    
    q="( SELECT * FROM `gallery` WHERE `type` = 'Video' ORDER BY `gallery_id` DESC LIMIT 3 )UNION ALL( SELECT * FROM `gallery` WHERE `type` = 'Image' ORDER BY `gallery_id` DESC LIMIT 3)ORDER BY `gallery` DESC"
    res=select(q)

    data['galleryss']=res
   
    
    q="SELECT * FROM `event` ORDER BY  event_id desc  LIMIT 4;"

    res=select(q)
    data['viewevent']=res
    
    q="SELECT * FROM `about` ORDER BY `about_id` DESC LIMIT 1;"
    res=select(q)
    data['about']=res
    
    q="SELECT * FROM `service` ORDER BY `service_id` DESC LIMIT 5"
    res=select(q)
    data['service']=res
    return render_template('index.html',data=data)





@public.route('/gallery',methods=['post','get'])
def gallery():
    data={}
   
    
    
    q="select * from gallery "
    res=select(q)
   
    data['galleryss']=res
  
    
   
    return render_template('gallery.html',data=data)

from cryptography.fernet import Fernet
from cryptography.fernet import Fernet

@public.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if "submit" in request.form:
            u = request.form['uname']
            p = request.form['pwd']

         
            q = "SELECT * FROM registration INNER JOIN login USING (login_id) WHERE username='%s'" % (u)
            res = select(q)

            if res:
                
                cipher_key = res[0]['cipher_key']
                stored_encrypted_password = res[0]['password']
                usertype = res[0]['usertype']
                login_id = res[0]['login_id']

               
                cipher = Fernet(cipher_key.encode())

                try:
                    
                    decrypted_stored_password = cipher.decrypt(stored_encrypted_password.encode()).decode('utf-8')
                except Exception as e:
                    flash('Error decrypting the password')
                    return redirect(url_for('public.login'))

              
                if (decrypted_stored_password == p):
                   
                    session['login_id'] = login_id
                    lid = session['login_id']

                   
                    if usertype == "admin":
                        session['name'] = res[0]['username']
                        return redirect(url_for('admin.jfoojrtngniejjiwnwgbiwijhfwe')) 
                    elif usertype == "pending":
                        flash("Login After Admin is approved")
                    elif usertype == "customer":
                       
                        q = "SELECT * FROM registration INNER JOIN login USING (login_id) WHERE login_id='%s'" % (lid)
                        reg_res = select(q)
                        if reg_res:
                            session['name'] = reg_res[0]['username']
                        return redirect(url_for('customer.cisieruigviuwyfiwfyuw'))  
                else:
                   
                    flash('Invalid username or password')
            else:
              
                flash('Invalid username or password')

    return render_template('login.html')



from cryptography.fernet import Fernet

@public.route('/signup', methods=['POST', 'GET'])    
def signup():
    if "submit" in request.form:
       
        f = request.form['fname']
        e = request.form['email']
        n = request.form['phone']
        u = request.form['uname']
        pa = request.form['pwd']

      
        q = "SELECT login_id, password, cipher_key FROM registration inner join login using (login_id) WHERE username='%s'" % (u)
        res = select(q)
   
     
        
        if res:
            
            
            cipher_key = res[0]['cipher_key']
            cipher = Fernet(cipher_key.encode())
            stored_password = res[0]['password']
     

            encrypted_password = cipher.encrypt(pa.encode()).decode('utf-8')
          

         
           
                
           
            flash('User already exists with this username and password')
            return redirect(url_for('public.signup'))

       
        else:
          
            cipher_key = Fernet.generate_key()
            cipher = Fernet(cipher_key)
            
           
            encrypted_email = cipher.encrypt(e.encode()).decode('utf-8')
            encrypted_phone = cipher.encrypt(n.encode()).decode('utf-8')
            encrypted_password = cipher.encrypt(pa.encode()).decode('utf-8')
            encrypted_fname = cipher.encrypt(f.encode()).decode('utf-8')
            
           
            q = "insert into login values(null, '%s', '%s', 'pending')" % (u, encrypted_password)
            id = insert(q)

           
            q = "insert into registration values(null, '%s', '%s', '%s', '%s', '%s')" % (
                id, encrypted_fname, encrypted_email, encrypted_phone, cipher_key.decode('utf-8')
            )
            insert(q)

            flash('Successfully registered')
            return redirect(url_for('public.login'))

    return render_template('signup.html')



from cryptography.fernet import Fernet

@public.route('/forgotpassword', methods=['POST', 'GET'])
def forgotpassword():
    data = {}
    
    if "submit" in request.form:
        email = request.form['email']
        uname = request.form['uname']

        
        q = "SELECT * FROM registration INNER JOIN login USING (login_id) WHERE username='%s'" % (uname)
        res = select(q)

        if res:
          
            encrypted_email = res[0]['email']
            cipher_key = res[0]['cipher_key']

          
            cipher = Fernet(cipher_key.encode())

           
            decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')

           
            if decrypted_email == email:
                return redirect(url_for('public.reset_password', email=email, username=uname))
            else:
                flash("Invalid email or username")
        else:
            flash("Invalid email or username")
            return redirect(url_for('public.login'))
    
    return render_template('forgotpassword.html')


from cryptography.fernet import Fernet


@public.route('/reset_password', methods=['POST', 'GET'])
def reset_password():
    data = {}
    email = request.args['email']
    data['email'] = email
    username = request.args['username']
    data['username'] = username

    if "submit" in request.form:
        email = request.form['email']
        pwd_confirm = request.form['pwd_confirm']
        uname = request.form['uname']

       
        q = "SELECT * from registration INNER JOIN login USING (login_id) WHERE username='%s'" % (uname)
        res = select(q)
    
        if res:
           
            cipher_key = res[0]['cipher_key']
            cipher = Fernet(cipher_key.encode())
            encrypted_email = res[0]['email']

           
            encrypted_password = cipher.encrypt(pwd_confirm.encode()).decode('utf-8')
            

           
            q = "UPDATE login SET password='%s' WHERE username='%s'" % (encrypted_password, uname)
            update(q)
           

          
            q = "SELECT * FROM registration inner join login using (login_id) WHERE email='%s'" % (encrypted_email)
            res = select(q)
        

            if res:
               
                encrypted_email = res[0]['email']
                decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')
                

                first_name = res[0]['name']
                first_name = cipher.decrypt(first_name.encode()).decode('utf-8')
                pwd_confirm = res[0]['password']
                pwd_confirm = cipher.decrypt(pwd_confirm.encode()).decode('utf-8')

          
                pwd_message = f"Dear SREE VENKITESWARA SEVA SAMITHY User {first_name}, Your New Password Is {pwd_confirm}"
             

                try:
                   
                    gmail = smtplib.SMTP('smtp.gmail.com', 587)
                    gmail.ehlo()
                    gmail.starttls()
                    gmail.login('renukakamath2@gmail.com', 'znwpqhzlelrsfudi')
                except Exception as e:
                    print("Couldn't setup email!!" + str(e))

              
                msg = MIMEText(pwd_message)
                msg['Subject'] = 'Password Reset Confirmation'
                msg['To'] = decrypted_email
                msg['From'] = 'renukakamath2@gmail.com'

                try:
                   
                    gmail.send_message(msg)
                    flash("EMAIL SENT SUCCESSFULLY")
                except Exception as e:
                    print("COULDN'T SEND EMAIL", str(e))
                else:
                    flash('Password reset successfully and email sent.')

        return redirect(url_for('public.login'))

    return render_template('reset_password.html', data=data)
