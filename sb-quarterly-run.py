import mysql.connector as sqltor
mycon= sqltor.connect(host='localhost', user='root', password='mysql', database='banking')

cursor1= mycon.cursor()
cursor2= mycon.cursor()
cursor3= mycon.cursor()

cursor1.execute("update sb set Principal = Principal + Interest where datediff(curdate(),DateOfLatestQR)=91;")
mycon.commit()
cursor2.execute("update sb set Interest=0 where datediff(curdate(),DateOfLatestQR)=91;")
mycon.commit()
cursor3.execute("update sb set DateOfLatestQR = curdate() where datediff(curdate(), DateOfLatestQR)=91;")
mycon.commit()
mycon.close()
