#!C:\python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,cgitb
import os,sys
import MySQLdb
import smssender
form=cgi.FieldStorage()
name=form.getvalue('name')
#print name
fname=form.getvalue('fname')
#print fname
gender=form.getvalue('gender')
#print gender
address=form.getvalue('address')
#print address
contactno=form.getvalue('contactno')
#print contact no
emailaddress=form.getvalue('emailaddress')
#print emailaddress
password=form.getvalue('password')
#print password
db=MySQLdb.connect("127.0.0.1","root","","biet",3306)            #hostname,username,password,databasename,portno  default portno for mysql is 3306
cur=db.cursor()
query="insert into register values(%s,%s,%s,%s,%s,%s,%s)"
args=name,fname,gender,address,contactno,emailaddress,password
cur.execute(query,args)
db.commit()
db.close()
smssender.sendsms(contactno,'Thanks for registration.We will contact you soon. -Team HR')
print "<script>alert('Registration Successfull');window.location.href='registration.py';</script>"
