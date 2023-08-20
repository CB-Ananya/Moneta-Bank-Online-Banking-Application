from datetime import *
import mysql.connector as sqltor

mycon= sqltor.connect(host='localhost', user='root', password='mysql', database='banking')

cursor1= mycon.cursor()
cursor2=mycon.cursor()
cursor3=mycon.cursor()
cursor4=mycon.cursor()
cursor5=mycon.cursor()
cursor6=mycon.cursor()
cursor7=mycon.cursor()
cursor8=mycon.cursor()
cursor9=mycon.cursor()

cursor1.execute("select * from studloan;")
data1= cursor1.fetchall()
#print(data1)
for i in data1:
    CustID= i[0]
    Name=i[1]
    acc_no = i[2]
    dos= i[3]
    princi = i[4]
    tenure = i[5]
    roi=i[6]
    each_emi = i[7]
    tot_topay = i[8]
    paid= i[9]
    balance_topay = i[10]
    ins_done = i[11]
    ins_expected = i[12]
    defaults = i[13]
    status = i[14]

    tod= date.today()
    ndays = (tod-dos).days
    dor_starts = dos + timedelta(days=365)
  
    if ndays>=365 and status=="NOT STARTED":
        cursor2.execute("update studloan set Loan_status='STARTED AND RUNNING' where Name='"+Name+"';")
        mycon.commit()
        if (tod-dor_starts).days%30==0 and (tod-dor_starts).days!=0:
            cursor3.execute("update studloan set Loan_InsEx = Loan_InsEx + 1 where Name='"+Name+"';")
            
            mycon.commit()
            cursor4.execute("update studloan set Loan_defaults = Loan_defaults + 1 where Name='"+Name+"' and Loan_InsD<=Loan_InsEx;")
            mycon.commit()

    if status=="STARTED AND RUNNING":
        if (tod-dor_starts).days%30==0 and (tod-dor_starts).days!=0:
            cursor5.execute("update studloan set Loan_InsEx = Loan_InsEx + 1 where Name='"+Name+"';")
            
            mycon.commit()
            cursor6.execute("update studloan set Loan_defaults = Loan_defaults + 1 where Name='"+Name+"' and Loan_InsD<=Loan_InsEx;")
            mycon.commit()

            
        if ins_done==tenure*12 and paid==tot_topay:
            cursor7.execute("update studloan set Loan_status = 'REPAYED' where Name='"+Name+"';")
            mycon.commit()
            
            
mycon.close()
