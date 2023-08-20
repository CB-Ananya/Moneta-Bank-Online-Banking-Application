import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user='root', password='mysql', database='banking')
cursor1= mycon.cursor()
cursor1.execute("update sb set Interest= Interest + (Principal*3.3)/(365*100);")
mycon.commit()
mycon.close()
