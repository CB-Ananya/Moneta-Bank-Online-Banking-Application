import mysql.connector as sqltor
mycon= sqltor.connect(host='localhost', user='root', password='mysql', database='banking')

cursor1= mycon.cursor()
cursor2=mycon.cursor()
cursor1.execute("select * from fd where curdate()<=MaturityDate and FD_Status='RUNNING';")
data1= cursor1.fetchall()

for i in data1:
    if i[7]<=6:
        cursor2.execute("update fd set FDInterest= FDInterest + ((Principal*3.8)/(100*365)) where CustID="+ str(i[0])+";")
    elif i[7]>6 and i[7]<=12:
        cursor2.execute("update fd set FDInterest= FDInterest + ((Principal*4.0)/(100*365)) where CustID="+ str(i[0])+";")
    elif i[7]>12 and i[7]<=24:
        cursor2.execute("update fd set FDInterest= FDInterest + ((Principal*5.0)/(100*365)) where CustID="+ str(i[0])+";")
    elif i[7]>24 and i[7]<=36:
        cursor2.execute("update fd set FDInterest= FDInterest + ((Principal*5.2)/(100*365)) where CustID="+ str(i[0])+";")
    elif i[7]>36 and i[7]<=60:
        cursor2.execute("update fd set FDInterest= FDInterest + ((Principal*5.5)/(100*365)) where CustID="+ str(i[0])+";")
    elif i[7]>60 and i[7]<=84:
        cursor2.execute("update fd set FDInterest= FDInterest + ((Principal*5.8)/(100*365)) where CustID="+ str(i[0])+";")
    elif i[7]>84 and i[7]<=120:
        cursor2.execute("update fd set FDInterest= FDInterest + ((Principal*6.2)/(100*365)) where CustID="+ str(i[0])+";")
    else:
        pass

cursor3.execute("update fd set FD_Status= 'COMPLETED' where curdate()<=MaturityDate and FD_Status!='BROKEN BEFORE MATURITY';"
mycon.commit()
mycon.close()
    
