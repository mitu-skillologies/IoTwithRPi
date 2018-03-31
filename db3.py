import MySQLdb
db=MySQLdb.connect("localhost","root","root","college")
cursor=db.cursor()
name=raw_input("Enter name")
roll=input("enter roll")
marks=input("enter marks")
sql="insert INTO student VALUES(%d,'%s',%f)"%(roll,name,marks)
try:
	cursor.execute(sql)
	db.commit()
except:
	print "error"
	db.rollback()
db.close()
