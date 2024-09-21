import mysql.connector

user="sql12732573"
password="sJYTsEzKZ3"
database="sql12732573"
port = 3306


def select(q):
	con=mysql.connector.connect(user=user,password=password,host="sql12.freesqldatabase.com",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	result=cur.fetchall()
	cur.close()
	con.close()
	return result

def insert(q):
	con=mysql.connector.connect(user=user,password=password,host="sql12.freesqldatabase.com",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.lastrowid
	cur.close()
	con.close()
	return result

def update(q):
	con=mysql.connector.connect(user=user,password=password,host="sql12.freesqldatabase.com",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.rowcount
	cur.close()
	con.close()

def delete(q):
	con=mysql.connector.connect(user=user,password=password,host="sql12.freesqldatabase.com",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	result=cur.rowcount
	cur.close()
	con.close()