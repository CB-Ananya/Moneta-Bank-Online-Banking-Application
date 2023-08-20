import mysql.connector as sqltor
from datetime import *
mycon= sqltor.connect(host='localhost', user='root', password='mysql', database='banking')

cursor1= mycon.cursor()
cursor2= mycon.cursor()
cursor3= mycon.cursor()

curdate = date.today()
curdate = curdate.strftime("%Y-%m-%d")

query1= "update fd set Principal=Principal+FDInterest where (datediff(%s,DateOfLatestQR)=91 and %s<=MaturityDate and FD_Status='RUNNING');"
cursor1.execute(query1, (curdate, curdate))
mycon.commit()
query2= "update fd set FDInterest=0 where (datediff(%s, DateOfLatestQR)=91 and %s<=MaturityDate and FD_Status='RUNNING');"
cursor2.execute(query2, (curdate, curdate))
mycon.commit()
query3= "update fd set DateOfLatestQR=curdate() where (datediff(%s, DateOfLatestQR)=91 and %s<=MaturityDate and FD_Status='RUNNING');"
cursor3.execute(query3, (curdate, curdate))
mycon.commit()
mycon.close()
