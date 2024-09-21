
from flask import * 
from database import*



import uuid



customer=Blueprint('customer',__name__)

@customer.route('/cisieruigviuwyfiwfyuw')
def cisieruigviuwyfiwfyuw():
    data={}
    name=session['name']
    data['name']=name
    q="SELECT * FROM `temple` "

    res=select(q)
    data['templeview']=res
    
    lid=session['login_id']
    
    q = """
    SELECT COUNT(*) AS unread_count
    FROM chat
    WHERE chat_id = (
    SELECT MAX(chat_id)
    FROM chat
    WHERE (receiver_id='%s' AND sender_id='1')
    );
        """ % (lid)

    res = select(q)

    unread_count = res[0]['unread_count'] 
    data['unread_count'] = unread_count
    
    
    
    return render_template('customer_home.html',data=data)



@customer.route('/stayfgeuhriwegwiurewoiohvwuiofi')
def stayfgeuhriwegwiurewoiohvwuiofi():
    data={}
    name=session['name']
    data['name']=name
    
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
    
    return render_template('customer_viewstaff.html',data=data)



@customer.route('/mudurywuffwygfwuyrewuriew')
def mudurywuffwygfwuyrewuriew():
    data={}
    name=session['name']
    data['name']=name
    q="SELECT * FROM `music` "

    res=select(q)
    data['viewmusic']=res
    
    return render_template('customer_viewmusic.html',data=data)
@customer.route('/dejhejgjhgrwjhfgwhfjwurwyriuwyirw',methods=['post','get'])
def dejhejgjhgrwjhfgwhfjwurwyriuwyirw():
    data={}
    name=session['name']
    data['name']=name
    
 
    
    from cryptography.fernet import Fernet
    import uuid


    from cryptography.fernet import Fernet

 
    key = Fernet.generate_key()
 
    cipher = Fernet(key)
    d_key = key.decode()
   
 


    
    if "submit" in request.form:
        
 
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        dob = request.form.get('dob')
        age = request.form.get('age')
        gender = request.form.get('gender')
        occupation = request.form.get('occupation')
        address = request.form.get('address')
        birthstar = request.form.get('birthstar')
        gothram = request.form.get('gothram')
        
      
        photo = request.files.get('photo')
        path = "static/" + str(uuid.uuid4()) + photo.filename
        photo.save(path)

       
        
        encrypted_fname = cipher.encrypt(fname.encode()).decode('utf-8')
        encrypted_lname = cipher.encrypt(lname.encode()).decode('utf-8')
        encrypted_dob = cipher.encrypt(dob.encode()).decode('utf-8')
        encrypted_age = cipher.encrypt(age.encode()).decode('utf-8')
        encrypted_occupation = cipher.encrypt(occupation.encode()).decode('utf-8')
        encrypted_email = cipher.encrypt(email.encode()).decode('utf-8')
        encrypted_phone = cipher.encrypt(phone.encode()).decode('utf-8')
        encrypted_address = cipher.encrypt(address.encode()).decode('utf-8')
        
     
        insert_user_query = """
        INSERT INTO userdetails (login_id, fname, lname, email, phone, dob, age, gender, photo, occupation, address, birthstar, gothram, secret_key)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
        """%(session['login_id'], encrypted_fname, encrypted_lname, 
            encrypted_email, encrypted_phone, 
            encrypted_dob, encrypted_age, gender, path, encrypted_occupation, 
            encrypted_address, birthstar, gothram,d_key)
        user_id=insert(insert_user_query)
     
        
       
       
        
  
        family_member_names = request.form.getlist('family_member_name[]')
        family_member_star = request.form.getlist('family_member_star[]')
        family_member_occupations = request.form.getlist('family_member_occupation[]')
        family_member_contacts = request.form.getlist('family_member_contact[]')
        family_member_age = request.form.getlist('family_member_age[]')
        
        sql_base = "INSERT INTO family_members (user_id, name, occu, contact, ag, st) VALUES "
        values = []

        for i in range(len(family_member_names)):
            encrypted_name = cipher.encrypt(family_member_names[i].encode()).decode('utf-8')
            encrypted_occupation = cipher.encrypt(family_member_occupations[i].encode()).decode('utf-8')
            encrypted_contact = cipher.encrypt(family_member_contacts[i].encode()).decode('utf-8')
            encrypted_star = cipher.encrypt(family_member_star[i].encode()).decode('utf-8')
            encrypted_age = cipher.encrypt(family_member_age[i].encode()).decode('utf-8')
            
            values.append(f"({user_id}, '{encrypted_name}', '{encrypted_occupation}', '{encrypted_contact}', '{encrypted_age}', '{encrypted_star}' )")

        sql_values = ", ".join(values)
        sql = sql_base + sql_values + ";"
        insert(sql)
        
        flash("Successfully added!")
        return redirect(url_for('customer.dejhejgjhgrwjhfgwhfjwurwyriuwyirw'))




      
    
    return render_template('customer_managedetails.html',data=data)

@customer.route('/jhsgrjyryewubciuehfiwufiuowefiwwui',methods=['post','get'])
def jhsgrjyryewubciuehfiwufiuowefiwwui():
    data={}
    name=session['name']
    data['name']=name
    
    
    
    
    from cryptography.fernet import Fernet
    import uuid
    import os
    
    
  
    select_user_query = """
    SELECT fname, lname, email, phone, dob, age, gender, photo, occupation, address, birthstar, gothram, secret_key,user_id
    FROM userdetails
    WHERE login_id = %s
    """%(session['login_id'])
    
    res = select(select_user_query)
    
    
    if res:
        user_details = res[0]
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
          
            
            data['viewuserdetails'] = res
    

    from cryptography.fernet import Fernet
    

  
    q = "SELECT family_members.*, userdetails.* FROM family_members INNER JOIN userdetails USING (user_id) WHERE userdetails.login_id='%s'" % session['login_id']
    res1 = select(q)


    decrypted_family_members = []
    if res1:
        for member in res1:
            cipher_key = member['secret_key']
            if cipher_key:
                cipher = Fernet(cipher_key.encode())
                decrypted_name = cipher.decrypt(member['name'].encode()).decode('utf-8')
                decrypted_occupation = cipher.decrypt(member['occu'].encode()).decode('utf-8')
                decrypted_contact = cipher.decrypt(member['contact'].encode()).decode('utf-8')
                decrypted_star = cipher.decrypt(member['st'].encode()).decode('utf-8')
                decrypted_age = cipher.decrypt(member['ag'].encode()).decode('utf-8')
                
                member['name'] = decrypted_name
                member['occu'] = decrypted_occupation
                member['contact'] = decrypted_contact
                member['st'] = decrypted_star
                member['ag'] = decrypted_age
                
                decrypted_family_members.append(member)
        
        data['viewfamily_members'] = decrypted_family_members


    action = request.args.get('action')
    fid = request.args.get('fid')
    
    if action == 'delete' and fid:
        q = "DELETE FROM family_members WHERE family_id='%s'" % fid
        delete(q)
        flash("Family member deleted successfully")
        return redirect(url_for('customer.jhsgrjyryewubciuehfiwufiuowefiwwui'))

    action1 = request.args.get('action1')
    uid = request.args.get('uid')

    if action1 == 'delete' and uid:
        q = "DELETE FROM userdetails WHERE user_id='%s'" % uid
        delete(q)
        flash("User details deleted successfully")
        return redirect(url_for('customer.jhsgrjyryewubciuehfiwufiuowefiwwui'))



    

       
    
    return render_template('customer_viewuserdetails.html',data=data)



@customer.route('/tejekrhkwgbwkejghoiwjgoiewnvoeiwjf',methods=['post','get'])
def tejekrhkwgbwkejghoiwjgoiewnvoeiwjf():
    data={}
    name=session['name']
    data['name']=name

    
    
    q="select * from  temple"
    res=select(q)
    data['viewtemple']=res
    

    
    return render_template('customer_viewtemple.html',data=data)


@customer.route('/ebhvjfdhgiehgrbveurfhr',methods=['post','get'])
def ebhvjfdhgiehgrbveurfhr():
    data={}
    name=session['name']
    data['name']=name
    
    tid=request.args['tid']

    
    
    q="select * from  event  where temple_id='%s'"%(tid)
    res=select(q)
    data['viewevent']=res
    

    
    return render_template('customer_viewevent.html',data=data)


@customer.route('/cjhdshudsifiuvidwuhiueriwuerewbuiu',methods=['get','post'])
def cjhdshudsifiuvidwuhiueriwuerewbuiu():
    data={}
    data={}
    name=session['name']
    data['name']=name
    lid=session['login_id']
   
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into chat values(NULL,'%s',1,'%s',now())"%(lid,name)
        insert(q)
        
        return redirect(url_for("customer.cjhdshudsifiuvidwuhiueriwuerewbuiu"))
    q="SELECT * FROM chat WHERE (sender_id='%s' AND receiver_id='1') OR (sender_id='1' AND receiver_id=('%s')) order by chat_id"%(lid,lid)
 
    print(q)
    res=select(q)
    data['ress']=res
    return render_template('user_chat.html',data=data,lid=lid)


