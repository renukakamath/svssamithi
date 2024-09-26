from flask import * 
from database import*
import uuid

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

from image_upload import*

admin=Blueprint('admin',__name__)





@admin.route('/wejkwkjfbdsfhewibchsjkajkhksakuwdhab')
def wejkwkjfbdsfhewibchsjkajkhksakuwdhab():
    
    
    data={}
    name=session['name']
    data['name']=name
    
    q="SELECT * FROM `registration` inner join login using (login_id) WHERE login_id IN (SELECT IF(sender_id = '1',receiver_id,sender_id) FROM chat WHERE sender_id='1' OR receiver_id='1')"
 
    res=select(q)
    data['res']=res
    return render_template('admin_view_message.html',data=data)



from cryptography.fernet import Fernet

@admin.route('/kfjgigkdnfdrboitrigjoeriv')
def kfjgigkdnfdrboitrigjoeriv():
    data = {}
    name = session['name']
    data['name'] = name

   
    q = "SELECT * FROM contactus"
  
    res = select(q)

    decrypted_feedbacks = []
    if res:
        for feedback in res:
         
            cipher_key = feedback['cipher_key']
            if cipher_key:
                cipher = Fernet(cipher_key.encode())
            
            
                decrypted_name = cipher.decrypt(feedback['name'].encode()).decode('utf-8')
                decrypted_email = cipher.decrypt(feedback['email'].encode()).decode('utf-8')
                decrypted_number = cipher.decrypt(feedback['number'].encode()).decode('utf-8')
                decrypted_message = cipher.decrypt(feedback['message'].encode()).decode('utf-8')

            
                feedback['name'] = decrypted_name
                feedback['email'] = decrypted_email
                feedback['number'] = decrypted_number
                feedback['message'] = decrypted_message
                
                decrypted_feedbacks.append(feedback)

        data['viewfeedback'] = decrypted_feedbacks

    return render_template('admin_viewcontact.html', data=data)




@admin.route('/bgggdggkjfjoeriwiewiuri',methods=['get','post'])
def bgggdggkjfjoeriwiewiuri():
    data={}
    name=session['name']
    data['name']=name
    
    did=request.args['did']
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into chat values(NULL,1,'%s','%s',now())"%(did,name)
        insert(q)
        return redirect(url_for("admin.bgggdggkjfjoeriwiewiuri",did=did))
    q="SELECT * FROM chat WHERE (sender_id='1' AND receiver_id='%s') OR (sender_id='%s' AND receiver_id=(1)) order by chat_id"%(did,did)


    res=select(q)
    data['ress']=res
    return render_template('admin_sendmessage.html',data=data)


from cryptography.fernet import Fernet


@admin.route('/jfoojrtngniejjiwnwgbiwijhfwe', methods=['GET', 'POST'])
def jfoojrtngniejjiwnwgbiwijhfwe():
    data = {}
    name = session['name']
    data['name'] = name

   
    q = "SELECT * FROM registration INNER JOIN login USING (login_id)"
 
    res = select(q)

    decrypted_users = []
    if res:
        for user in res:
          
            cipher_key = user['cipher_key']
            if cipher_key:
                cipher = Fernet(cipher_key.encode())
            
            
               
                
                decrypted_email = cipher.decrypt(user['email'].encode()).decode('utf-8')
                decrypted_name = cipher.decrypt(user['name'].encode()).decode('utf-8')
                decrypted_phone = cipher.decrypt(user['phone'].encode()).decode('utf-8')
                
           
                user['email'] = decrypted_email
                user['name'] = decrypted_name
                user['phone'] = decrypted_phone
                
                decrypted_users.append(user)

        data['viewuser'] = decrypted_users

    if "action" in request.args:
        action = request.args['action']
        lid = request.args['lid']
    else:
        action = None

    if action == 'accept':
       
        q = "UPDATE login SET usertype='customer' WHERE login_id='%s'" % (lid)
        update(q)

       
        q = "SELECT * FROM registration WHERE login_id='%s'" % (lid)
        res = select(q)
        if res:
            cipher_key = res[0]['cipher_key']
            cipher = Fernet(cipher_key.encode())

            encrypted_email = res[0]['email']
            decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')

            encrypted_first_name = res[0]['name']
            decrypted_first_name = cipher.decrypt(encrypted_first_name.encode()).decode('utf-8')

            email_message = f"Dear SREE VENKITESWARA SEVA SAMITHY User {decrypted_first_name}, Your Request Is Accepted"
  

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('renukakamath2@gmail.com', 'znwpqhzlelrsfudi')
            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText(email_message)
            msg['Subject'] = 'Confirmation'
            msg['To'] = decrypted_email
            msg['From'] = 'renukakamath2@gmail.com'

            try:
                gmail.send_message(msg)
                flash("EMAIL SENT SUCCESSFULLY")
            except Exception as e:
                print("COULDN'T SEND EMAIL", str(e))
            else:
                flash('User accepted and email sent.')

        return redirect(url_for('admin.jfoojrtngniejjiwnwgbiwijhfwe'))

    if action == 'reject':
       
        q = "UPDATE login SET usertype='block' WHERE login_id='%s'" % (lid)
        update(q)

       
        q = "SELECT * FROM registration WHERE login_id='%s'" % (lid)
        res = select(q)
        if res:
            cipher_key = res[0]['cipher_key']
            cipher = Fernet(cipher_key.encode())

            encrypted_email = res[0]['email']
            decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')

            encrypted_first_name = res[0]['name']
            decrypted_first_name = cipher.decrypt(encrypted_first_name.encode()).decode('utf-8')

            email_message = f"Dear SREE VENKITESWARA SEVA SAMITHY User {decrypted_first_name}, Your Request Is Rejected"
           

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('renukakamath2@gmail.com', 'znwpqhzlelrsfudi')
            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText(email_message)
            msg['Subject'] = 'Rejection Notice'
            msg['To'] = decrypted_email
            msg['From'] = 'renukakamath2@gmail.com'

            try:
                gmail.send_message(msg)
                flash("EMAIL SENT SUCCESSFULLY")
            except Exception as e:
                print("COULDN'T SEND EMAIL", str(e))
            else:
                flash('User rejected and email sent.')

        return redirect(url_for('admin.jfoojrtngniejjiwnwgbiwijhfwe'))

    return render_template('admin_home.html', data=data)



@admin.route('/kirorwkorrgjerngijrekrhhrtiri',methods=['post','get'])
def kirorwkorrgjerngijrekrhhrtiri():
    data={}
    name=session['name']
    data['name']=name
    if "submit" in request.form:
        u=request.form['title']
        p=request.form['details']
        img=request.files['image']
        image_url = upload_image(img)
        
        # img=request.files['image']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path) 
        q="insert into service values(null,'%s','%s','%s')" % (image_url,u,p)
        insert(q)
        flash("successfully")
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    
    if "action1" in request.args:
        action1=request.args['action1']
        
        sid=request.args['sid']
    else:
        action1=None;

 
    if action1=='delete1':
        q="delete from  service where service_id='%s'"%(sid)
        delete(q)
        flash("successfully")
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    if action1=='update1':
        q="select * from service where service_id='%s'"%(sid)
        res=select(q)
        data['serviceup']=res
    if "update" in request.form:
        u=request.form['title']
        p=request.form['details']
        
        # img=request.files['image']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path) 
        img=request.files['image']
        image_url = upload_image(img)
 
       
        q="update service set title='%s' ,details='%s', image='%s' where service_id='%s' "%(u,p,image_url,sid)
        update(q)
        flash('successfully')
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    q="select * from service"
    res=select(q)
    data['service']=res
    
    
    if "about" in request.form:
        
        p=request.form['details']
        
        # img=request.files['image']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path)
        img=request.files['temple_images']
        image_url = upload_image(img) 
        q="insert into about values(null,'%s','%s')" % (p,image_url)
        insert(q)
        flash("successfully")
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    
    if "action2" in request.args:
        action2=request.args['action2']
        
        aid=request.args['aid']
    else:
        action2=None;

 
    if action2=='delete2':
        q="delete from  about where about_id='%s'"%(aid)
        delete(q)
        flash("successfully")
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    if action2=='update2':
        q="select * from about where about_id='%s'"%(aid)
        res=select(q)
        data['aboutup']=res
    if "update1" in request.form:
        p=request.form['details']
        
        # img=request.files['image']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path) 
        img=request.files['temple_images']
        image_url = upload_image(img)
 
       
        q="update about set about='%s' ,pic='%s' where about_id='%s' "%(p,image_url,aid)
        update(q)
        flash('successfully')
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    
    q="select * from about"
    res=select(q)
    data['about']=res
    
    
    
    
    if "gallery" in request.form:
        
        p=request.form['type']
        
        # img=request.files['image']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path) 
        img=request.files['image']
        image_urls = upload_file(img)
        
        q="insert into gallery values(null,'%s','%s')" % (image_urls,p)
        insert(q)
        flash("successfully")
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    if "action3" in request.args:
        action3=request.args['action3']
        
        gid=request.args['gid']
    else:
        action3=None;

 
    if action3=='delete3':
        q="delete from  gallery where gallery_id='%s'"%(gid)
        delete(q)
        flash("successfully")
        return redirect(url_for('admin.kirorwkorrgjerngijrekrhhrtiri'))
    
    
    
    q="select * from gallery"
    res=select(q)
    data['gallery']=res
    
    
    return render_template('admin_addindex.html',data=data)

@admin.route('/bbdbbrbjferjieirewijtiew')
def bbdbbrbjferjieirewijtiew():
    data = {}
    name=session['name']
    data['name']=name

   
    
    
    
    from cryptography.fernet import Fernet
    import uuid
    import os
    
    
  
    select_user_query = """
    SELECT user_id, fname, lname, email, phone, dob, age, gender, photo, occupation, address, birthstar, gothram, secret_key 
    FROM userdetails
    """

    users = select(select_user_query)

    if users:
        decrypted_users = []  

    for user_details in users:
        encrypted_email = user_details['email']
        encrypted_phone = user_details['phone']
        encrypted_address = user_details['address']
        encrypted_fname = user_details['fname']
        encrypted_lname = user_details['lname']
        encrypted_dob = user_details['dob']
        encrypted_age = user_details['age']
        encrypted_occupation = user_details['occupation']
        
        cipher_key = user_details['secret_key'] 
        if cipher_key:
            cipher = Fernet(cipher_key.encode())

          
            decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')
            decrypted_phone = cipher.decrypt(encrypted_phone.encode()).decode('utf-8')
            decrypted_address = cipher.decrypt(encrypted_address.encode()).decode('utf-8')
            decrypted_fname = cipher.decrypt(encrypted_fname.encode()).decode('utf-8')
            decrypted_lname = cipher.decrypt(encrypted_lname.encode()).decode('utf-8')
            decrypted_dob = cipher.decrypt(encrypted_dob.encode()).decode('utf-8')
            decrypted_age = cipher.decrypt(encrypted_age.encode()).decode('utf-8')
            decrypted_occupation = cipher.decrypt(encrypted_occupation.encode()).decode('utf-8')

           
            user_details['email'] = decrypted_email
            user_details['phone'] = decrypted_phone
            user_details['address'] = decrypted_address
            user_details['fname'] = decrypted_fname
            user_details['lname'] = decrypted_lname
            user_details['dob'] = decrypted_dob
            user_details['age'] = decrypted_age
            user_details['occupation'] = decrypted_occupation

          
            decrypted_users.append(user_details)
            data['viewuserdetails'] = decrypted_users
            
            
            
        user_family_details = {}

      
        for user in users:
            user_id = user['user_id']
            q = f"SELECT family_members.*, userdetails.* FROM family_members INNER JOIN userdetails USING (user_id) WHERE user_id='{user_id}'"
            family_members = select(q)
            
          
            decrypted_family_members = []
            for member in family_members:
                cipher_key = member['secret_key'] 
                if cipher_key:
                    cipher = Fernet(cipher_key.encode())
                    decrypted_name = cipher.decrypt(member['name'].encode()).decode('utf-8')
                    decrypted_occupation = cipher.decrypt(member['occu'].encode()).decode('utf-8')
                    decrypted_contact = cipher.decrypt(member['contact'].encode()).decode('utf-8')
                    decrypted_star = cipher.decrypt(member['st'].encode()).decode('utf-8')
                    decrypted_age = cipher.decrypt(member['ag'].encode()).decode('utf-8')
                    
                   
                    decrypted_family_members.append({
                        'name': decrypted_name,
                        'occu': decrypted_occupation,
                        'contact': decrypted_contact,
                        'st': decrypted_star,
                        'ag': decrypted_age
                    })
                
               
                user_family_details[user_id] = decrypted_family_members

          
            data['viewfamily_members'] = user_family_details
            
            
        

            
        
   
    return render_template('admin_viewuserdetails.html', data=data)






@admin.route('/bill1')
def bill1():
    data={}
    from cryptography.fernet import Fernet
    import uuid
    import os
    
    user_id=request.args['user_id']
    select_user_query = """
    SELECT user_id,fname, lname, email, phone, dob, age, gender, photo, occupation, address, birthstar, gothram, secret_key 
    FROM userdetails  where user_id='%s'
   
    """%(user_id)
    
    users = select(select_user_query)
    
    
    if users:
        user_details = users[0]
        encrypted_email = user_details['email']
        encrypted_phone = user_details['phone']
        encrypted_address = user_details ['address']
        encrypted_fname = user_details['fname']
        encrypted_lname = user_details['lname']
        encrypted_dob = user_details ['dob']
        encrypted_age = user_details['age']
        encrypted_occupation = user_details['occupation']
        
        cipher_key = user_details['secret_key'] 
        if cipher_key:
            cipher = Fernet(cipher_key.encode())

        
            decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')
            decrypted_phone = cipher.decrypt(encrypted_phone.encode()).decode('utf-8')

            decrypted_address = cipher.decrypt(encrypted_address.encode()).decode('utf-8')
            
            decrypted_fname = cipher.decrypt(encrypted_fname.encode()).decode('utf-8')
            decrypted_lname = cipher.decrypt(encrypted_lname.encode()).decode('utf-8')

            decrypted_dob = cipher.decrypt(encrypted_dob.encode()).decode('utf-8')
            decrypted_age = cipher.decrypt(encrypted_age.encode()).decode('utf-8')
            decrypted_occupation = cipher.decrypt(encrypted_occupation.encode()).decode('utf-8')
            
           
            
            user_details['email'] = decrypted_email
            user_details['phone'] = decrypted_phone
            user_details['address'] = decrypted_address
            user_details['fname'] = decrypted_fname
            user_details['lname'] = decrypted_lname
            user_details['dob'] = decrypted_dob
            user_details['age'] = decrypted_age
            user_details['occupation'] = decrypted_occupation
            
            data['viewuserdetails'] = users
    
        user_family_details = {}

        for user in users:
            user_id = user['user_id']
            q = f"SELECT family_members.*, userdetails.* FROM family_members INNER JOIN userdetails USING (user_id) WHERE user_id='{user_id}'"
            family_members = select(q)
    
            
          
            decrypted_family_members = []
            for member in family_members:
                cipher_key = member['secret_key']  
                if cipher_key:
                    cipher = Fernet(cipher_key.encode())
                    decrypted_name = cipher.decrypt(member['name'].encode()).decode('utf-8')
                    decrypted_occupation = cipher.decrypt(member['occu'].encode()).decode('utf-8')
                    decrypted_contact = cipher.decrypt(member['contact'].encode()).decode('utf-8')
                    decrypted_star = cipher.decrypt(member['st'].encode()).decode('utf-8')
                    decrypted_age = cipher.decrypt(member['ag'].encode()).decode('utf-8')
                    
                
                    decrypted_family_members.append({
                        'name': decrypted_name,
                        'occu': decrypted_occupation,
                        'contact': decrypted_contact,
                        'st': decrypted_star,
                        'ag': decrypted_age
                    })
                
                
                user_family_details[user_id] = decrypted_family_members

            
            data['viewfamily_members'] = decrypted_family_members

    
    return render_template('bill1.html',data=data)



@admin.route('/hsyeyueyhjgbeuroiuowiqqonjwfnqw',methods=['post','get'])
def hsyeyueyhjgbeuroiuowiqqonjwfnqw():
    data={}
    name=session['name']
    data['name']=name
    
    q="select * from  music"
    res=select(q)
    data['viewmusic']=res
    
    if "submit" in request.form:
        n=request.form['musicTitle']
        e=request.form['youtubeLink']
        l=request.form['musiclyrics']
        img1=request.files['audioFile']
        upload_audio1 = upload_audio(img1)
      
        # img1=request.files['audioFile']
        # path1="static/"+str(uuid.uuid4())+img1.filename
        # img1.save(path1)
        
        
     
        # pdf_file = request.files['pdfFile']
        
      
        # Pass the file to the upload_pdf function
        # file_url1 = upload_pdf(pdf_file)
 
        
        
 
        # img2=request.files['pdfFile']
        # path2="static/"+str(uuid.uuid4())+img2.filename
        # img2.save(path2) 
        q="insert into music values(null,'%s','%s','%s','0','%s')" % (n,e,upload_audio1,l)
        insert(q)
        flash("successfully")
        
        return redirect(url_for('admin.hsyeyueyhjgbeuroiuowiqqonjwfnqw'))
    
    
    if "action" in request.args:
        action=request.args['action']
        
        mid=request.args['mid']
    else:
        action=None;

 
    if action=='delete':
        q="delete from  music where music_id='%s'"%(mid)
        delete(q)
        flash("successfully")
        return redirect(url_for('admin.hsyeyueyhjgbeuroiuowiqqonjwfnqw'))
    if action=='update':
        q="select * from music where music_id='%s'"%(mid)
        res=select(q)
        data['musicup']=res
    if "update" in request.form:
        n=request.form['musicTitle']
        e=request.form['youtubeLink']
        l=request.form['musiclyrics']
        img1=request.files['audioFile']
        upload_audio1 = upload_audio(img1)
      
        # img1=request.files['audioFile']
        # path1="static/"+str(uuid.uuid4())+img1.filename
        # img1.save(path1)
        
        
     
        # pdf_file = request.files['pdfFile']
        
      
        # Pass the file to the upload_pdf function
        # file_url1 = upload_pdf(pdf_file)
    
 
        # img2=request.files['pdfFile']
        # path2="static/"+str(uuid.uuid4())+img2.filename
        # img2.save(path2) 
        q="update music set title='%s' ,audio_file='%s', youtube_link='%s',music='%s' where music_id='%s' "%(n,upload_audio1,e,l,mid)
        update(q)
        flash('successfully')
        return redirect(url_for('admin.hsyeyueyhjgbeuroiuowiqqonjwfnqw'))
    
    
    return render_template('admin_addmusic.html',data=data)


from cryptography.fernet import Fernet
import uuid


@admin.route('/kaoiwiwuwgfgeugdqyquyqqbdbjwhw', methods=['post', 'get'])
def kaoiwiwuwgfgeugdqyquyqqbdbjwhw():
    data = {}
    name = session['name']
    data['name'] = name
    
    
    
    
    
    from cryptography.fernet import Fernet
    import uuid
    import os
    
    
    
    
    
  
    select_user_query = """
    SELECT job, name, phone, email, place, photo,staff_id,cipher_key 
    FROM staff
    """


    users = select(select_user_query)

    if users:
        decrypted_users = [] 

    for user_details in users:
        encrypted_job = user_details['job']
        encrypted_name = user_details['name']
        encrypted_phone = user_details['phone']
        encrypted_email = user_details['email']
        encrypted_place = user_details['place']
       
       
        cipher_key = user_details['cipher_key']  
        if cipher_key:
            cipher = Fernet(cipher_key.encode())

            decrypted_job = cipher.decrypt(encrypted_job.encode()).decode('utf-8')
            decrypted_name = cipher.decrypt(encrypted_name.encode()).decode('utf-8')
            decrypted_phone = cipher.decrypt(encrypted_phone.encode()).decode('utf-8')
            decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')
            decrypted_place = cipher.decrypt(encrypted_place.encode()).decode('utf-8')
            
  


            user_details['job'] = decrypted_job
            user_details['name'] = decrypted_name
            user_details['phone'] = decrypted_phone
            user_details['email'] = decrypted_email
            user_details['place'] = decrypted_place
           

     
            decrypted_users.append(user_details)
            data['viewstaff'] = decrypted_users


    cipher_key = Fernet.generate_key() 
    cipher = Fernet(cipher_key)

    

    if "submit" in request.form:
        n = request.form['name']
        p = request.form['place']
        e = request.form['email']
        ph = request.form['phone']
        j = request.form['job']
        img=request.files['imgg']
        image_url = upload_image(img)

        # img = request.files['imgg']
        # path = "static/" + str(uuid.uuid4()) + img.filename
        # img.save(path)


        encrypted_name = cipher.encrypt(n.encode()).decode('utf-8')
        encrypted_place = cipher.encrypt(p.encode()).decode('utf-8')
        encrypted_email = cipher.encrypt(e.encode()).decode('utf-8')
        encrypted_phone = cipher.encrypt(ph.encode()).decode('utf-8')
        encrypted_job = cipher.encrypt(j.encode()).decode('utf-8')

        q = "INSERT INTO staff (job, name, phone, email, place, photo, cipher_key) VALUES ('%s', '%s', '%s', '%s','%s', '%s', '%s')"%(encrypted_job, encrypted_name, encrypted_phone, encrypted_email, encrypted_place, image_url,cipher_key.decode('utf-8'))
        insert(q)
        flash("Staff member added successfully")
        return redirect(url_for('admin.kaoiwiwuwgfgeugdqyquyqqbdbjwhw'))

 
    action = request.args.get('action')
    sid = request.args.get('sid')

    if action == 'delete' and sid:
        q = "DELETE FROM staff WHERE staff_id = %s" % (sid)
        delete(q)
        flash("Staff member deleted successfully")
        return redirect(url_for('admin.kaoiwiwuwgfgeugdqyquyqqbdbjwhw'))

    if action == 'update' and sid:
        q = "SELECT * FROM staff WHERE staff_id = %s" % (sid)
        res = select(q)
        

        if res:
            decrypted_users = []  
        
        cipher_key = user_details['cipher_key'] 
        if cipher_key:
            cipher = Fernet(cipher_key.encode())

            decrypted_job = cipher.decrypt(encrypted_job.encode()).decode('utf-8')
            decrypted_name = cipher.decrypt(encrypted_name.encode()).decode('utf-8')
            decrypted_phone = cipher.decrypt(encrypted_phone.encode()).decode('utf-8')
            decrypted_email = cipher.decrypt(encrypted_email.encode()).decode('utf-8')
            decrypted_place = cipher.decrypt(encrypted_place.encode()).decode('utf-8')
            
  

          
            user_details['job'] = decrypted_job
            user_details['name'] = decrypted_name
            user_details['phone'] = decrypted_phone
            user_details['email'] = decrypted_email
            user_details['place'] = decrypted_place
           

          
            decrypted_users.append(user_details)
            data['personup'] = decrypted_users


    if "update" in request.form:
        n = request.form['name']
        p = request.form['place']
        e = request.form['email']
        ph = request.form['phone']
        j = request.form['job']
        img=request.files['imgg']
        image_url = upload_image(img)
        

        # img = request.files['imgg']
        # path = "static/" + str(uuid.uuid4()) + img.filename
        # img.save(path)

       
        encrypted_name = cipher.encrypt(n.encode()).decode('utf-8')
        encrypted_place = cipher.encrypt(p.encode()).decode('utf-8')
        encrypted_email = cipher.encrypt(e.encode()).decode('utf-8')
        encrypted_phone = cipher.encrypt(ph.encode()).decode('utf-8')
        encrypted_job = cipher.encrypt(j.encode()).decode('utf-8')

      
        q = """
        UPDATE staff 
        SET name = '%s', place = '%s', email =' %s', phone =' %s', job = '%s', photo = '%s'
        WHERE staff_id ='%s'
        """%(encrypted_name, encrypted_place, encrypted_email, encrypted_phone, encrypted_job, image_url, sid)
        update(q)
        flash("Staff member updated successfully")
        return redirect(url_for('admin.kaoiwiwuwgfgeugdqyquyqqbdbjwhw'))

    return render_template('admin_addstaff.html', data=data)

from image_upload import upload_image
@admin.route('/poeioiejgueyejbvegfeuwiwhqwqhdhqwgd',methods=['post','get'])
def poeioiejgueyejbvegfeuwiwhqwqhdhqwgd():
    
    data={}
    name=session['name']
    data['name']=name
    if "submit" in request.form:
        u=request.form['temple_name']
        p=request.form['temple_details']
        
        img=request.files['temple_images']
        image_url = upload_image(img)

        q="insert into temple values(null,'%s','%s','%s')" % (u,p,image_url)
        insert(q)
        flash("successfully")
        
        return redirect(url_for('admin.poeioiejgueyejbvegfeuwiwhqwqhdhqwgd'))
 
    q="select * from  temple"
    res=select(q)
    data['viewtemple']=res
    
    
    if "action" in request.args:
        action=request.args['action']
        
        fid=request.args['uid']
    else:
        action=None;

 
    if action=='delete':
        q="delete from  temple where temple_id='%s'"%(fid)
        delete(q)
        flash("successfully")
        return redirect(url_for('admin.poeioiejgueyejbvegfeuwiwhqwqhdhqwgd'))
    if action=='update':
        q="select * from temple where temple_id='%s'"%(fid)
        res=select(q)
        data['templeup']=res
    if "update" in request.form:
        u=request.form['temple_name']
        p=request.form['temple_details']
        img=request.files['temple_images']
        image_url = upload_image(img)
        
        # img=request.files['temple_images']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path)
        q="update temple set temple_name='%s' ,details='%s', image='%s' where temple_id='%s' "%(u,p,image_url,fid)
        update(q)
        flash('successfully')
        return redirect(url_for('admin.poeioiejgueyejbvegfeuwiwhqwqhdhqwgd'))
    
    return render_template('admin_Addtemple.html',data=data)




@admin.route('/evehjeheighitjueitgnjehgih',methods=['post','get'])
def evehjeheighitjueitgnjehgih():
    data={}
    name=session['name']
    data['name']=name
    tid=request.args['tid']
    if "submit" in request.form:
        u=request.form['eventTitle']
        p=request.form['eventDetails']
        d=request.form['date']
        img=request.files['eventImage']
        image_url = upload_image(img)
        
        # img=request.files['eventImage']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path) 
        q="insert into event values(null,'%s','%s','%s','%s','%s')" % (tid,u,p,image_url,d)
        insert(q)
        flash("successfully")
        
        return redirect(url_for('admin.evehjeheighitjueitgnjehgih',tid=tid))
    
    
    q="select * from  event  where temple_id='%s'"%(tid)
    res=select(q)
    data['viewevent']=res 
    
    
    if "action" in request.args:
        action=request.args['action']
        
        tid=request.args['tid']
        eid=request.args['eid']
    else:
        action=None;

 
    if action=='delete':
        q="delete from event where event_id='%s'"%(eid)
        delete(q)
        flash("successfully")
        return redirect(url_for('admin.evehjeheighitjueitgnjehgih',tid=tid))
    

    if action=='update':
        q="select * from event where event_id='%s'"%(eid)
        res=select(q)
        data['eventup']=res
    if "update" in request.form:
        u=request.form['eventTitle']
        p=request.form['eventDetails']
        d=request.form['date']
        img=request.files['eventImage']
        image_url = upload_image(img)
        
        # img=request.files['eventImage']
        # path="static/"+str(uuid.uuid4())+img.filename
        # img.save(path)
        q="update event set title='%s' ,details='%s', photo='%s' ,date='%s' where event_id='%s' "%(u,p,image_url,d,eid)
        update(q)
        flash('successfully')
        return redirect(url_for('admin.evehjeheighitjueitgnjehgih',tid=tid))
        

    
    return render_template('admin_addevent.html',data=data)


