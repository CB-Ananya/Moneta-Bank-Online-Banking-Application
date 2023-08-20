# Importing Modules #
from tkinter import *
from datetime import *
from PIL import ImageTk, Image
import datetime as dt
import os
import random
import mysql.connector as sqltor

# mysql connection object #
mycon=sqltor.connect(host="localhost", user="root", password="mysql", database="banking")

# Cursor Objects #
cursor1= mycon.cursor()
cursor2= mycon.cursor()
cursor3= mycon.cursor()
cursor4= mycon.cursor()
cursor5= mycon.cursor()
cursor6= mycon.cursor()
cursor7= mycon.cursor()
cursor8= mycon.cursor()
cursor9= mycon.cursor()
cursor10= mycon.cursor()
cursor11= mycon.cursor()
cursor12= mycon.cursor()
cursor13= mycon.cursor()
cursor14= mycon.cursor()
cursor15= mycon.cursor()
cursor16= mycon.cursor()
cursor17= mycon.cursor()
cursor18= mycon.cursor()
cursor19= mycon.cursor()
cursor20= mycon.cursor()
cursor21= mycon.cursor()
cursor22= mycon.cursor()
cursor23= mycon.cursor()
cursor24= mycon.cursor()
cursor25= mycon.cursor()
cursor26= mycon.cursor()
cursor27= mycon.cursor()
cursor28= mycon.cursor()
cursor29= mycon.cursor()
cursor30= mycon.cursor()

master= Tk()
master.title('ONLINE BANK')
master.config(bg="#bbf5ae")

## leaving signup screen ##
def leave_signup():
    signup_screen.destroy()

## Finishing SignUp process through validation ##
def finish_signup():
    name = temp_name.get()
    gender= temp_gender.get()
    dob= temp_dob.get()
    password = temp_password.get()


    if name =="" or gender=="" or dob=="" or password=="" :
        notif.config(fg="red", text="ALL FIELDS REQUIRED * ")
        return
    if gender not in 'FMfm':
        notif.config(fg="red", text="INVALID INPUT IN GENDER FIELD")
        return
 
    try:
        dob_as_date_in_py = dt.datetime.strptime(dob, "%Y-%m-%d")
        dob_as_date_in_py = dob_as_date_in_py.date()
    except:
        notif.config(fg="red", text="INVALID INPUT IN DATE FIELD")
        return
    if len(password)<8:
        notif.config(fg="red", text="MINIMUM 8 CHARACTERS REQUIRED FOR PASSWORD")
        return
    if " " in password:
       notif.config(fg="red", text="PASSWORD CANNOT HAVE EMPTY SPACES")
       return
            


    def getcyphertext(rand_encrypt, inchar):
        # encrypt string using Caesar Cipher algorithm
        asciival = ord(inchar)
        tmpasciival = asciival - rand_encrypt
        if tmpasciival < 0:
            outval = (255 + tmpasciival)
        else:
            outval = tmpasciival
        return outval
    
    
    rand_encrypt = random.randint(1,127)
   
    # inputstring is password
    inputstring = password
    outputstring = ""
    for i in inputstring:
        cypherval = getcyphertext(rand_encrypt, i)
        outputstring = outputstring + chr(cypherval)

    

    password=outputstring

    ######## GENERATION OF CUSTOMER ID #######
    def gencustid():
        global customer_id
        customer_id= random.randint(100000000000,999999999999)
    gencustid()

    
    def check_customer_id_repeat():
        cursor14.execute("select CustID from login;")
        data14= cursor14.fetchall()
        for i in data14:
            for j in i:
                if customer_id==j:
                    gencustid()
                    check_customer_id_repeat()
        else:
            pass

    check_customer_id_repeat()
    

    Label(signup_screen, text="YOUR CUSTOMER ID IS: "+str(customer_id), font=('Calibri', 20)).grid(row=9, sticky=W)
    Label(signup_screen, text="*CUSTOMER ID IS THE KEY ATTRIBUTE YOU USE TO LOGIN AND IS USED TO LINK ALL YOUR ACCOUNTS IN MONETA BANK", font=('Calibri', 16)).grid(row=10, sticky=W)
    query1="insert into login values(%s, %s, %s, %s, %s, %s);"
    cursor1.execute(query1, (customer_id, name, gender, dob, password, rand_encrypt))
    mycon.commit()
    query2="insert into Type_acc values(%s, %s, %s, %s, %s);"
    cursor30.execute(query2, (customer_id, name,'N', 'N', 'N'))
    mycon.commit()
    notif.config(fg="red", text="")
    
    
    Label(signup_screen, text="ACCOUNT HAS BEEN CREATED", fg="green", width = 25, font=('Calibri', 26)).grid(row=8, sticky=N, pady=12)

    Button(signup_screen, text="CLOSE", command= leave_signup, font=('Calibri', 14), bg="#b2a6ed").grid(row=14, sticky=N, pady=12)
    
   
## signup process - receiving input ##
def signup():
    login_signup.destroy()
    global temp_name
    global temp_gender
    
    global temp_dob
    global temp_password
    global notif
    global signup_screen
    temp_name= StringVar()
    temp_gender= StringVar()
    
    temp_dob= StringVar()
    temp_password= StringVar()

    
    signup_screen= Toplevel(master)
    signup_screen.title('Sign Up')
    signup_screen.config(bg="#bbf5ae")
    
    #Labels
    Label(signup_screen, text="Please enter your details below to sign up", font=('Calibri', 14)).grid(row=0, column=0, sticky=N, pady=12)
    Label(signup_screen, text="Account holder Name", font=('Calibri', 14)).grid(row=1, column=0, sticky=W, pady=12)
    Label(signup_screen, text="Gender(F/M)", font=('Calibri', 14)).grid(row=2, column=0, sticky=W, pady=12)
    Label(signup_screen, text="Date Of Birth as YYYY-MM-DD", font=('Calibri', 14)).grid(row=3, column=0,  sticky=W, pady=10)
    Label(signup_screen, text="Please Enter a strong password:  *Minimum 8 characters required ", font=('Calibri', 14)).grid(row=4, column=0, sticky=W, pady=12)
    notif = Label(signup_screen, font=('Calibri', 14), bg="#bbf5ae")
    notif.grid(row=9, sticky=N, pady=12)

    #Entries
    Entry(signup_screen, textvariable=temp_name).grid(row=1, column=1)
    Entry(signup_screen, textvariable=temp_gender).grid(row=2, column=1)
    Entry(signup_screen, textvariable=temp_dob).grid(row=3, column=1)
    Entry(signup_screen, textvariable=temp_password, show="*").grid(row=4, column=1)

    #Buttons
    Button(signup_screen, text="Sign Up", command= finish_signup, font=('Calibri', 14), bg="#b2a6ed").grid(row=8, sticky=N, pady=12)


## Creation of FD Account ##
def createfd():
    global fd_notif

    global temp_principal_fd
    global temp_tenure_fd

    temp_principal_fd=StringVar()
    temp_tenure_fd = StringVar()

    
    Create_fd= Toplevel(master)
    Create_fd.title('Creating Fixed Deposit Account')
    Create_fd.config(bg="#bbf5ae")
    fd_notif=Label(Create_fd, font=('Calibri', 14))
    fd_notif.grid(row=16, sticky=N, pady=12)
    #Getting rates from text files
    f1=open(r'FD.txt', 'r')
    #getting heading line
    firstline = f1.readline()
    g= f1.read()
    #Labels
    Label(Create_fd, text= "Welcome "+ login_name+" to create your own FIXED DEPOSIT ACCOUNT!", font=('Calibri', 14)).grid(row=0, sticky=W, pady=5)
    Label(Create_fd, text= "Here are the interest rates we offer for a wide range of tenures you choose as of "+str(date.today()), font=('Calibri', 14)).grid(row=1, sticky=W, pady=5)
    Label(Create_fd, text= firstline, font=('Calibri', 14)).grid(row=2, sticky=W, pady=5)
    Label(Create_fd, text= "--------------------------------------------------------------------------------------------------", font=('Calibri', 14)).grid(row=3, sticky=W, pady=5)
    Label(Create_fd, text=g, font=('Calibri', 14)).grid(row=4, sticky=W, pady=5)

    global display_breakfd_terms_initial

    def display_breakfd_text_atcreation():
        global display_breakfd_terms_initial
        display_breakfd_terms_initial = Toplevel(master)
        display_breakfd_terms_initial.title('PREMATURE WITHDRAWAL/BREAKING FD - TERMS AND CONDITIONS')
        display_breakfd_terms_initial.config(bg="#bbf5ae")
        f4 = open(r'BreakFD.txt')
        g4 = f4.read()
        Label(display_breakfd_terms_initial, text = g4, font=('Calibri', 14)).grid(row=0, sticky=W, pady=5)

        def close_display_breakfd_terms_initial():
            global display_breakfd_terms_initial
            display_breakfd_terms_initial.destroy()

        Button(display_breakfd_terms_initial, text="CLOSE", command = close_display_breakfd_terms_initial, font=('Calibri', 14), bg="#b2a6ed").grid(row=10, sticky=N, pady=5)
    
        
    Label(Create_fd, text = "CUSTOMERS HAVE THE CONVINIENCE OF PREAMTURE WITHDRAWAL AS WELL!!", font=('Calibri', 14)).grid(row=5, column=0, sticky=W, pady=5)   
    Label(Create_fd, text = "Click here to know Terms and Conditions for Premature Withdrawal", font=('Calibri', 14)).grid(row=6, column=0, sticky=W, pady=5)
    
    Button(Create_fd, text="PREMATURE WITHDRAWAL/ BREAKING FD - TERMS AND CONDITIONS", command= display_breakfd_text_atcreation, font=('Calibri', 14), bg="#b2a6ed").grid(row=6, column=1)

    Label(Create_fd, text="Enter the amount you would like to deposit (minimum deposit Rs.1000)", font=('Calibri', 14)).grid(row=7, column=0, sticky=W, pady=5)
    Entry(Create_fd, textvariable= temp_principal_fd).grid(row=7, column=1)
    Label(Create_fd, text="Enter the tenure you choose (in months)", font=('Calibri', 14)).grid(row=8, column=0, sticky=W, pady=5)
    Entry(Create_fd, textvariable= temp_tenure_fd).grid(row=8, column=1)

    fddeptime = date.today()
    DateOfOpenFD= fddeptime.strftime("%Y-%m-%d")
    

    def genfdacc():
        global FD_Acc_No
        FD_Acc_No= random.randint(100000000000,999999999999)
        
    def check_fd_accno_repeat():
        cursor14.execute("select FDAcc_No from fd")
        data14= cursor14.fetchall()
        for i in data14:
            for j in i:
                if FD_Acc_No==j:
                    genfdacc()
                    check_fd_accno_repeat()
        else:
            pass

    genfdacc()
    check_fd_accno_repeat()
    
    def openfd():
        try:
            FDTenure= int(temp_tenure_fd.get())
        except:
            fd_notif.config(bg="#bbf5ae", fg="red", text="INVALID TENURE INPUT")
            return
        try:
            FDPrincipal = int(temp_principal_fd.get())
        except:
            fd_notif.config(bg="#bbf5ae", fg="red", text="INVALID PRINCIPAL INPUT")
            return
        DateOfMaturityOfFD= fddeptime + timedelta(days=int((FDTenure*365/12)))
        if FDPrincipal<1000:
            fd_notif.config(bg="#bbf5ae", fg="red", text="MINIMUM DEPOSIT Rs.1000! REQUIRED")
            return

        cursor15.execute("select dob from login where CustID="+str(login_custid)+";")
        data15=cursor15.fetchone()
        for i in data15:
            dob=i
        
        if FDTenure<=6:
            FDIntRate=2.5
        elif FDTenure>6 and FDTenure<=12:
            FDIntRate=4.0
        elif FDTenure>12 and FDTenure<=24:
            FDIntRate=5.0
        elif FDTenure>24 and FDTenure<=36:
            FDIntRate=5.2
        elif FDTenure>36 and FDTenure<=60:
            FDIntRate=5.5
        elif FDTenure>60 and FDTenure<=84:
            FDIntRate=5.8
        elif FDTenure>84 and FDTenure<=120:
            FDIntRate=6.2
        else:
            fd_notif.config(bg="#bbf5ae", fg="red", text="INVALID TENURE INPUT")
            return
        Label(Create_fd, text="Rate of Interest applicable: "+ str(FDIntRate) +"%", font=('Calibri', 14)).grid(row=10, column=0, sticky=W, pady=5)
        query15="insert into FD values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor15.execute(query15, (login_custid, login_name, dob, DateOfOpenFD, FDPrincipal, FDPrincipal, FD_Acc_No, FDTenure, FDIntRate, 0, FDPrincipal*((1 + (FDIntRate/400)))**(FDTenure/3),  DateOfMaturityOfFD, DateOfOpenFD, 'RUNNING', -1))
        mycon.commit()
        fd_notif.config(fg="green", text="ACCOUNT CREATED AND AMOUNT SUCCESSFULLY DEPOSITED")
        Label(Create_fd, text="THE ACCOUNT NO. FOR THIS ACCOUNT IS: "+str(FD_Acc_No), font=('Calibri', 20), bg="#C0B2FF", fg="black").grid(row=13, sticky=W, pady=5)
        cursor15.execute("update type_acc set FD='Y' where CustID="+str(login_custid)+";")
        mycon.commit()
        def closeCreate_fd():
            Go_To_DB_after_fd_creation.destroy()
            account_dashboard.destroy()
            Create_fd.destroy()
            login_session()
        Go_To_DB_after_fd_creation = Toplevel(master)
        Go_To_DB_after_fd_creation.title('Go To Dashboard')
        Go_To_DB_after_fd_creation.config(bg="#bbf5ae")
        Button(Go_To_DB_after_fd_creation, text="CLOSE AND GO TO DASHBOARD", command=closeCreate_fd, font=('Calibri', 14), bg="#b2a6ed").grid(row=2, sticky=N)
            

    Button(Create_fd, text="Confirm and Open", command= openfd, font=('Calibri', 14), bg="#b2a6ed").grid(row=9, sticky=N, pady=12)



## Display of existing FD Account ##
def displayfd():
    cursor16.execute("select * from fd where CustID="+str(login_custid)+";")
    data16=cursor16.fetchone()
    fd_display_custid = data16[0]
    fd_display_Name = data16[1]
    fd_display_DOB= data16[2]
    fd_display_DOO= data16[3]
    
    global fd_display_Princi
    fd_display_Princi_atopen=data16[4]
    fd_display_Princi_now= data16[5]
    fd_display_accountNo=data16[6]
    fd_display_tenure= data16[7]
    fd_display_roi= data16[8]
    fd_interest_tilldate= data16[9]
    fd_display_maturity_value= round(data16[10], 2)
    fd_display_maturity_date= data16[11]
    fd_display_date_of_latest_qr = data16[12]
    fd_display_status = data16[13]
    fd_display_if_broken_amount = data16[14]
    
    tod= date.today()
   
    fd_tenure_tilldate_indays = (tod-fd_display_DOO).days
    fd_tenure_tilldate_inmonths = fd_tenure_tilldate_indays//30
            
    global displayfd_screen
    try:
        displayfd_screen.destroy()
    except:
        pass
    displayfd_screen=Toplevel(master)
    displayfd_screen.title("Your Fixed Deposit--For an assured growth")
    displayfd_screen.config(bg="#bbf5ae")

    Label(displayfd_screen, text="WELCOME "+login_name, font=('Calibri', 14)).grid(row=0, column=0, sticky=W, pady=5)
    Label(displayfd_screen, text="ACCOUNT NUMBER:  ", font=('Calibri', 14)).grid(row=10, column=0, sticky=W, pady=5)
    Label(displayfd_screen, text=str(fd_display_accountNo), font=('Calibri', 14)).grid(row=10, column=2, sticky=W, pady=5)
    Label(displayfd_screen, text="Your Principal deposit: ", font=('Calibri', 14)).grid(row=11, column=0, sticky=W, pady=5)
    Label(displayfd_screen, text=str(fd_display_Princi_atopen), font=('Calibri', 14)).grid(row=11, column=2, sticky=W, pady=5)
    Label(displayfd_screen, text="Rate of Interest: ", font=('Calibri', 14)).grid(row=12, column=0, sticky=W, pady=5)
    Label(displayfd_screen, text=str(fd_display_roi)+"%", font=('Calibri', 14)).grid(row=12, column=2, sticky=W, pady=5)
    Label(displayfd_screen, text="You opened FD on: ", font=('Calibri', 14)).grid(row=13, column=0, sticky=W, pady=5)
    Label(displayfd_screen, text=str(fd_display_DOO), font=('Calibri', 14)).grid(row=13, column=2, sticky=W, pady=5)
    Label(displayfd_screen, text="Your FD Maturity Date: ", font=('Calibri', 14)).grid(row=14, column=0, sticky=W, pady=5)
    Label(displayfd_screen, text=str(fd_display_maturity_date), font=('Calibri', 14)).grid(row=14, column=2, sticky=W, pady=5)
    Label(displayfd_screen, text="Your FD Maturity Value: ", font=('Calibri', 14)).grid(row=15, column=0, sticky=W, pady=5)
    Label(displayfd_screen, text=str(fd_display_maturity_value), font=('Calibri', 14)).grid(row=15, column=2, sticky=W, pady=5)

    global fd_break_screen


    def break_fd():
        f3 = open(r'BreakFD.txt')
        g2= f3.read()
        fd_break_screen= Toplevel(master)
        fd_break_screen.title("Breaking Fixed Deposit Account before maturity")
        fd_break_screen.config(bg="#bbf5ae")
        Label(fd_break_screen, text="Your Principal Deposit: "+str(fd_display_Princi_atopen), font=('Calibri', 14)).grid(row=0, sticky=W, pady=5)
        Label(fd_break_screen, text="Your Amount at the end of your original tenure would be: "+str(fd_display_maturity_value), font=('Calibri', 14)).grid(row=1, sticky=W, pady=5)
        Label(fd_break_screen, text=g2, font=('Calibri', 14)).grid(row=2, sticky=W, pady=5)
        
        def calc_break_fd():
            aft_fd_break_screen= Toplevel(master)
            aft_fd_break_screen.title('Closure of Fixed Deposit before Maturity Date')
            aft_fd_break_screen.config(bg="#bbf5ae")
            
            Label(aft_fd_break_screen, text="Upon premature withdrawal of your Fixed Deposit Account, you can recieve an amount of: " + str(round(fd_display_Princi_atopen*((1 + ((fd_display_roi - 1.0)/400))**((4*fd_tenure_tilldate_inmonths)/12)),2)), font=('Calibri', 14)).grid(row=2)
            
            def del_from_fd_tables():
                cursor17.execute("update fd set FD_Status='BROKEN BEFORE MATURITY', If_broken_amount="+str(round(fd_display_Princi_atopen*((1 + ((fd_display_roi - 1.0)/400))**((4*fd_tenure_tilldate_inmonths)/12)),2))+" where CustID="+str(fd_display_custid)+";")
                mycon.commit()             
                aft_fd_break_screen.destroy()
                fd_break_screen.destroy()
                displayfd_screen.destroy()
                account_dashboard.destroy()
                login_session()

            Button(aft_fd_break_screen, text="CLOSE", command= del_from_fd_tables, font=('Calibri', 14), bg="#b2a6ed").grid(row=4, sticky=W, pady=5)
            
        Button(fd_break_screen, text="I have read all the Terms and Conditions, agree to the same, and would like to Break the Fixed Deposit Account", command= calc_break_fd, font=('Calibri', 14), bg="#b2a6ed").grid(row=5, sticky=W, pady=5)
        
        
    if date.today()< fd_display_maturity_date:
        if fd_display_status=='BROKEN BEFORE MATURITY':
            Label(displayfd_screen, text= "YOU HAVE BROKEN YOUR FIXED DEPOSIT AND ARE ELIGIBLE TO RECEIVE AN AMOUNT OF: "+str(fd_display_if_broken_amount), font=('Calibri', 14)).grid(row=16, column=0, sticky=W, pady=5)
        else:
            Button(displayfd_screen, text="Break FD", command = break_fd, font=('Calibri', 14), bg="#b2a6ed").grid(row=17, sticky=W, pady=5)
    if date.today()>=fd_display_maturity_date:
        Label(displayfd_screen, text="FIXED DEPOSIT HAS MATURED!", font=('Calibri', 14), fg='green').grid(row=17, sticky=W, pady=5)
        Label(displayfd_screen, text="KINDLY VISIT ANY LOCAL BRANCH OFFICE FOR RECEIPT OF THE AMOUNT UPON ACCOUNT CLOSURE.", font=('Calibri', 14), fg='green').grid(row=18, sticky=W, pady=5)

    def go_out_of_fd_to_dashboard():
        displayfd_screen.destroy()
        account_dashboard.destroy()
        login_session()

    Button(displayfd_screen, text="DASHBOARD", command= go_out_of_fd_to_dashboard, font=('Calibri', 14), bg="#b2a6ed", fg="black").grid(row=0, column= 100, sticky=E)
    

## Creating SB Account ##
def createsb():
    
    global temp_principal_sb
    global sb_notif
    temp_principal_sb=StringVar()
    
    Create_sb= Toplevel(master)
    Create_sb.title('Creating Savings Bank account')
    Create_sb.config(bg="#bbf5ae")
    sb_notif=Label(Create_sb, font=('Calibri', 14))
    sb_notif.grid(row=9, sticky=N, pady=12)
    #Labels
    Label(Create_sb, text="Welcome "+login_name+" to create your own SAVINGS BANK ACCOUNT!", font=('Calibri',14)).grid(row=0, sticky=N, pady=5)
    Label(Create_sb, text="Interest Rate offered: \n 3.3%", font=('Calibri', 14)).grid(row=1, sticky=W, pady=5)
    Label(Create_sb, text="Enter the amount you would like to deposit: (Minimum INR Rs.500)", font=('Calibri', 14)).grid(row=2, sticky=W, pady=5)
    #Entries
    Entry(Create_sb, textvariable=temp_principal_sb).grid(row=2, column=20)
    sbdeptime= date.today()
    DateOfOpenSB= sbdeptime.strftime("%y-%m-%d")

    #Generating Account Number
    
    def gensbacc():
        global SB_Acc_No
        SB_Acc_No= random.randint(100000000000,999999999999)
    def check_sb_accno_repeat():
        cursor8.execute("select Acc_No from sb")
        data8= cursor8.fetchall()
        for i in data8:
            for j in i:
                if SB_Acc_No==j:
                    gensbacc()
                    check_sb_accno_repeat()
        else:
            pass

    gensbacc()
    check_sb_accno_repeat()

    def opensb():
        SbPrincipal=int(temp_principal_sb.get())
        if SbPrincipal<500:
            sb_notif.config(fg="red", text="MINIMUM BALANCE Rs.500 REQUIRED!!")
            return
        #Amount= Principal
        cursor5.execute("select dob from login where CustID="+str(login_custid)+";")
        data5=cursor5.fetchone()
        for i in data5:
            dob=i
        query6="insert into SB values(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor6.execute(query6, (login_custid, login_name, dob, DateOfOpenSB, SbPrincipal, SB_Acc_No,0, DateOfOpenSB))
        mycon.commit()
        sb_notif.config(fg="green", text="ACCOUNT CREATED AND AMOUNT SUCCESSFULLY DEPOSITED")
        Label(Create_sb, text="THE ACCOUNT NO. FOR THIS ACCOUNT IS: "+str(SB_Acc_No), font=('Calibri', 14)).grid(row=6, sticky=W, pady=5)
        cursor7.execute("update type_acc set SB='Y' where CustID="+str(login_custid)+";")
        mycon.commit()
        def closeCreate_sb():
            Go_To_DB_after_sb_creation.destroy()
            account_dashboard.destroy()
            Create_sb.destroy()
            login_session()
        Go_To_DB_after_sb_creation = Toplevel(master)
        Go_To_DB_after_sb_creation.title('Go To Dashboard')
        Go_To_DB_after_sb_creation.config(bg="#bbf5ae")
        Button(Go_To_DB_after_sb_creation, text="CLOSE AND GO TO DASHBOARD", command=closeCreate_sb, font=('Calibri', 14), bg="#b2a6ed").grid(row=2, sticky=N)
            
    #Buttons
    Button(Create_sb, text="Confirm and Open", command= opensb, font=('Calibri', 14), bg="#b2a6ed").grid(row=4, sticky=W, pady=5)
    
    
## Displaying details of existing SB Account ##  
def displaysb():
    
    cursor9.execute("select * from sb where CustID="+str(login_custid)+";")
    data9=cursor9.fetchone()
    Name = data9[1]
    DOB= data9[2]
    DOO= data9[3]
    global sb_display_Princi
    sb_display_Princi=data9[4]
    SBAccountNo=data9[5]
    sb_interest_tilldate= data9[6]
    tod= date.today()
    

    def show_prin_aft_wd():
        wdmoney_sb = int(sbwdmoney.get())
        global sb_display_Princi
        if sb_display_Princi-wdmoney_sb<500.0:
            Label(sb_withdrawal,text= "You have to retain a minimum balance of INR Rs.500 in your account!", font=('Calibri', 14), fg="red").grid(row=3, sticky=W, pady=5)
        else:
            sb_withdrawal.destroy()
            successfulwithdrawal=Toplevel(master)
            successfulwithdrawal.title("Withdrawal Successful")
            successfulwithdrawal.config(bg="#bbf5ae")
            Label(successfulwithdrawal, text="Amount Rs."+str(wdmoney_sb)+" successfully withdrawn", font=('Calibri', 14)).grid(row=2)
            Label(successfulwithdrawal, text="New Amount is: Rs."+str(sb_display_Princi-wdmoney_sb), font=('Calibri', 14)).grid(row=3, sticky=W, pady=5)
            sb_display_Princi = sb_display_Princi-wdmoney_sb
            cursor12.execute("update sb set Principal="+str(sb_display_Princi)+" where CustID="+str(login_custid)+";")
            mycon.commit()
            def close_show_prin_after_wd():
                successfulwithdrawal.destroy()
                displaysb_screen.destroy()
                account_dashboard.destroy()
                global login_session
                login_session()
            Button(successfulwithdrawal, text="CLOSE AND GO TO DASHBOARD", command= close_show_prin_after_wd, font=('Calibri', 14), bg="#b2a6ed").grid(row=14, sticky=W, pady=5)

    def sbwithdrawal():
        global sb_withdrawal
        global sbwdmoney
        
        sbwdmoney= StringVar()
        sb_withdrawal= Toplevel(master)
        sb_withdrawal.title('Withdrawal from Savings Bank Account')
        sb_withdrawal.config(bg="#bbf5ae")
        Label(sb_withdrawal, text="Enter the amount you would like to withdraw", font=('Calibri', 14)).grid(row=0, column=0, sticky=N, pady=5)
        Entry(sb_withdrawal, textvariable= sbwdmoney).grid(row=0, column=1)
        Button(sb_withdrawal, text= "Confirm and Withdraw", command= show_prin_aft_wd, font=('Calibri', 14), bg="#b2a6ed").grid(row=1, sticky=W)

    def show_prin_aft_deposit():
        depmoney_sb = int(sbdepmoney.get())
        global sb_display_Princi
        sb_deposit.destroy()
        
        successfuldeposit=Toplevel(master)
        successfuldeposit.title("Deposit Successful")
        successfuldeposit.config(bg="#bbf5ae")
        Label(successfuldeposit, text="Amount Rs."+str(depmoney_sb)+" successfully deposited", font=('Calibri', 14)).grid(row=2)
        Label(successfuldeposit, text="New Amount is: " + str(sb_display_Princi+depmoney_sb), font=('Calibri', 14)).grid(row=3, sticky=W, pady=5)
        sb_display_Princi=sb_display_Princi+ depmoney_sb
        cursor13.execute("update sb set Principal="+str(sb_display_Princi)+" where CustID="+str(login_custid)+";")
        mycon.commit()
        def close_show_prin_aft_deposit():
            successfuldeposit.destroy()
            displaysb_screen.destroy()
            account_dashboard.destroy()
            login_session()
        Button(successfuldeposit, text="CLOSE AND GO TO DASHBOARD", command= close_show_prin_aft_deposit, font=('Calibri', 14), bg="#b2a6ed").grid(row=14, sticky=W, pady=5)

    def sbdeposit():
        global sb_deposit
        global sbdepmoney

        sbdepmoney= StringVar()
        sb_deposit= Toplevel(master)
        sb_deposit.title('Deposit into Savings Bank Account')
        sb_deposit.config(bg="#bbf5ae")
        Label(sb_deposit, text="Enter the amount you would like to deposit", font=('Calibri', 14)).grid(row=0, column=0, sticky=W, pady=5)
        Entry(sb_deposit, textvariable= sbdepmoney).grid(row=0, column=1)
        Button(sb_deposit, text="Confirm and Deposit", command= show_prin_aft_deposit, font=('Calibri', 14), bg="#b2a6ed").grid(row=1, sticky=W)


    def go_out_of_sb_to_dashboard():
        displaysb_screen.destroy()
        account_dashboard.destroy()
        login_session()
        
    
        
    global displaysb_screen
    try:
        displaysb_screen.destroy()
    except:
        pass
    displaysb_screen=Toplevel(master)
    displaysb_screen.title("Your Valuable Savings")
    displaysb_screen.config(bg="#bbf5ae")
    global sb_withdrawal #sb_withdrawal is screen name # sbwithdrawal is function name
    global sb_deposit
    Label(displaysb_screen, text="WELCOME "+login_name, font=('Calibri',14)).grid(row=0, column=0, sticky=W, pady=5)
    Label(displaysb_screen, text="Account Number: "+str(SBAccountNo), font=('Calibri',14)).grid(row=9, sticky=W, pady=5)
    Label(displaysb_screen, text="Your Amount is: "+str(sb_display_Princi), font=('Calibri', 14)).grid(row=10, sticky=W, pady=5)
    Button(displaysb_screen, text="Withdrawal", command = sbwithdrawal, font=('Calibri', 14), bg="#b2a6ed").grid(row=11, sticky=W, pady=5)
    Button(displaysb_screen, text="Deposit", command=sbdeposit, font=('Calibri', 14), bg="#b2a6ed").grid(row=12, sticky=W, pady=5)
    Button(displaysb_screen, text="DASHBOARD", command = go_out_of_sb_to_dashboard, font=('Calibri', 14), bg="#b2a6ed", fg="black").grid(row=0, column=100, sticky=E)


## Applying for new student Loan ##
def createstudloan():
    Create_studloan=Toplevel(master)
    Create_studloan.title("Apply for Student Loan")
    Create_studloan.config(bg="#bbf5ae")
    Create_studloan_notif= Label(Create_studloan, font=('Calibri', 14), bg="#bbf5ae")
    Create_studloan_notif.grid(row=20, sticky=N)
    f4= open(r'studloan.txt')                               ###### Rates of Interest for student loan are displayed from text file ######
    studloanasked = StringVar()
    studloantenureasked = StringVar()
    g4= f4.read()
    
    Label(Create_studloan, text=g4, font=('Calibri', 14)).grid(row=0, column=0, sticky=W, pady=5)
    Label(Create_studloan, text= "Enter the amount you would like to apply a loan for from the given ranges", font=('Calibri', 14)).grid(row=16, column=0, sticky=W, pady=5)
    Label(Create_studloan, text= "Enter the Tenure (in years)", font=('Calibri', 14)).grid(row=17, column=0, sticky=W, pady=5)
    Entry(Create_studloan, textvariable= studloanasked).grid(row=16, column=1)
    Entry(Create_studloan, textvariable= studloantenureasked).grid(row=17, column=1)

    global studloanasked_innum
    global studloantenureasked_innum


    def get_createstudloan_var():
        global studloanasked_innum
        global studloantenureasked_innum
        try:
            studloanasked_innum=0
            studloanasked_innum = int(studloanasked.get())
            if (studloanasked_innum>10000000) or (studloanasked_innum<50001):
                Create_studloan_notif.config(fg="red", text="INVALID INPUT")
                return
        except:
            Create_studloan_notif.config(fg="red", text="INVALID INPUT")
        else:
            Create_studloan_notif.config(fg="red", text="")
            
        try:
            studloantenureasked_innum=0
            studloantenureasked_innum = int(studloantenureasked.get())
            if (studloantenureasked_innum) > 7 or (studloantenureasked_innum<1):
                Create_studloan_notif.config(fg="red", text="INVALID INPUT")
                return
            
        except:
            Create_studloan_notif.config(fg="red", text="INVALID INPUT")
        else:
            Create_studloan_notif.config(fg="red", text="")
            global studloan_roi
            def sanction_studloan(): 
                if studloanasked_innum>= 50001 and studloanasked_innum<=100000:
                    global studloan_roi
                    studloan_roi= 7.3
                elif studloanasked_innum>= 100001 and studloanasked_innum<=500000:
                    studloan_roi= 7.0
                elif studloanasked_innum>= 500001 and studloanasked_innum<=1500000:
                    studloan_roi= 6.7
                elif studloanasked_innum>= 1500001 and studloanasked_innum<=4000000:
                    studloan_roi= 6.5
                elif studloanasked_innum>= 4000001 and studloanasked_innum<=10000000:
                    studloan_roi= 6.1

            sanction_studloan()
            


            def genstudloanacc():
                global StudLoan_Acc_No
                StudLoan_Acc_No= random.randint(100000000000,999999999999)
                
            def check_studloan_accno_repeat():
                cursor19.execute("select Loan_Acc_No from studloan")
                data19= cursor18.fetchall()
                for i in data19:
                    for j in i:
                        if StudLoan_Acc_No==j:
                            genstudloanacc()
                            check_studloan_accno_repeat()
                        else:
                            pass

            genstudloanacc()
            check_studloan_accno_repeat()
            date_of_loan_sanction = date.today()
            loan_princi= studloanasked_innum
            loan_tenure = studloantenureasked_innum
            loan_roi = studloan_roi
            
            ########## EMI Calculation Formula ##########
            loan_emi = (loan_princi*(loan_roi*0.01/12)*((1 + (loan_roi*0.01/12))**(studloantenureasked_innum*12)))/((((1 + (loan_roi*0.01/12))**(studloantenureasked_innum*12)) - 1))
            ########## EMI Calculation Formula ##########
            
            loan_tot_int= (loan_emi*12*studloantenureasked_innum)- studloanasked_innum
            loan_tot_topay = loan_emi*12*studloantenureasked_innum
            loan_status="NOT STARTED"
            

            query20= "insert into studloan values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

            cursor20.execute(query20, (login_custid, login_name, StudLoan_Acc_No, date_of_loan_sanction, loan_princi, loan_tenure, loan_roi, loan_emi, loan_tot_topay, 0, loan_tot_topay, 0, 0, 0, loan_status))
            mycon.commit()
            cursor21.execute("update type_acc set studloan='Y' where CustID="+str(login_custid)+";")
            mycon.commit()

            Label(Create_studloan, text= "YOUR LOAN HAS BEEN SUNCTIONED! BEST WISHES!", font=('Calibri', 14), fg="green").grid(row=19, column=0, sticky=W, pady=5)

            Label(Create_studloan, text= "LOAN ACCOUNT NUMBER: "+ str(StudLoan_Acc_No), font=('Calibri', 20), bg="#C0B2FF", fg="black").grid(row=21, column=0, sticky=W, pady=5)

            def close_get_loan():
                Create_studloan.destroy()
                account_dashboard.destroy()
                login_session()

            Button(Create_studloan, text="CLOSE AND GO TO DASHBOARD", command = close_get_loan, font=('Calibri', 14), bg="#b2a6ed").grid(row=23)
                  
            
    Button(Create_studloan, text="SUBMIT", command = get_createstudloan_var, font=('Calibri', 14), bg="#b2a6ed").grid(row=21)
    


## Displaying details of existing Loan ##
def display_studloan():
    cursor21.execute("select Loan_status from studloan where CustID="+str(login_custid)+";")
    data21= cursor21.fetchone()
    for statii in data21:
        curr_loan_status= statii
    cursor22.execute("select * from studloan where CustID="+str(login_custid)+";")
    data22= cursor22.fetchone()
 
    loan_display_custid= data22[0]
    loan_display_name = data22[1]
    loan_display_accno = data22[2]
    loan_display_dos = data22[3].strftime("%Y-%m-%d")
    loan_display_princi = data22[4]
    loan_display_tenure = data22[5]
    loan_display_roi = data22[6]
    loan_display_emi = data22[7] 
    #below 5 values are known if status not started
    loan_display_totamt = data22[8]
    loan_display_sofarpaid = data22[9]
    loan_display_rem_balance = data22[10]
    loan_display_Installments_done = data22[11]
    loan_display_Installments_expected = data22[12]
    loan_display_defaults = data22[13]
    loan_display_status = data22[14]
    
    try:
        display_studloan_details.destroy()
    except:
        pass

    display_studloan_details= Toplevel(master)
    display_studloan_details.title("Student Loan Details: ")
    display_studloan_details.config(bg="#bbf5ae")
    
    Label(display_studloan_details, text="WELCOME "+login_name, font=('Calibri', 14)).grid(row=0, sticky=W, pady=5)
    Label(display_studloan_details, text="YOUR STUDENT LOAN STATUS (REPAYMENT): ", font=('Calibri', 14)).grid(row=1, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text=loan_display_status, font=('Calibri', 14)).grid(row=1, column=2, sticky=W, pady=5)
    Label(display_studloan_details, text="ACCOUNT NUMBER: ", font=('Calibri', 14)).grid(row=2, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text=str(loan_display_accno), font=('Calibri', 14)).grid(row=2, column=2, sticky=W, pady=5)
    Label(display_studloan_details, text="DATE OF SANCTION OF LOAN: ", font=('Calibri', 14)).grid(row=3, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text=loan_display_dos, font=('Calibri', 14)).grid(row=3, column=2, sticky=W, pady=5)
    Label(display_studloan_details, text="LOAN AMOUNT BORROWED: ", font=('Calibri', 14)).grid(row=4, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text="Rs."+str(loan_display_princi), font=('Calibri', 14)).grid(row=4, column=2, sticky=W, pady=5)
    Label(display_studloan_details, text="TENURE OF REPAYMENT: ", font=('Calibri', 14)).grid(row=5, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text=str(loan_display_tenure)+" years ("+str(loan_display_tenure*12)+" monthly installments)", font=('Calibri', 14)).grid(row=5, column=2, sticky=W, pady=5)
    Label(display_studloan_details, text="RATE OF INTEREST: ", font=('Calibri', 14)).grid(row=6, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text=str(loan_display_roi)+"%", font=('Calibri', 14)).grid(row=6, column=2, sticky=W, pady=5)
    Label(display_studloan_details, text="EMI (PER MONTH): ", font=('Calibri', 14)).grid(row=7, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text="Rs."+str(loan_display_emi), font=('Calibri', 14)).grid(row=7, column=2, sticky=W, pady=5)
    Label(display_studloan_details, text="TOTAL REPAYMENT AMOUNT: ", font=('Calibri', 14)).grid(row=8, column=0, sticky=W, pady=5)
    Label(display_studloan_details, text="Rs."+str(loan_display_totamt), font=('Calibri', 14)).grid(row=8, column=2, sticky=W, pady=5)
    
    if statii=="STARTED AND RUNNING":
        Label(display_studloan_details, text="AMOUNT PAID: ", font=('Calibri', 14)).grid(row=9, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text="Rs."+str(loan_display_sofarpaid), font=('Calibri', 14)).grid(row=9, column=2, sticky=W, pady=5)
        Label(display_studloan_details, text="REMAINING BALANCE: ", font=('Calibri', 14)).grid(row=10, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text="Rs."+str(loan_display_rem_balance), font=('Calibri', 14)).grid(row=10, column=2, sticky=W, pady=5)
        Label(display_studloan_details, text="NO. OF INSTALLMENTS EXPECTED TILL DATE: ", font=('Calibri', 14)).grid(row=11, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text=str(loan_display_Installments_expected), font=('Calibri', 14)).grid(row=11, column=2, sticky=W, pady=5)
        Label(display_studloan_details, text="NO. OF INSTALLMENTS PAID TILL DATE: ", font=('Calibri', 14)).grid(row=12, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text=str(loan_display_Installments_done), font=('Calibri', 14)).grid(row=12, column=2, sticky=W, pady=5)
        Label(display_studloan_details, text="NO. OF INSTALLMENTS DEFAULTED: ", font=('Calibri', 14)).grid(row=13, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text=str(loan_display_defaults), font=('Calibri', 14)).grid(row=13, column=2, sticky=W, pady=5)
        
        def payemi():
            emipayment = Toplevel(master)
            emipayment.title("EMI PAYMENT")
            emipayment.config(bg="#bbf5ae")
            Label(emipayment, text="WELCOME: "+login_name, font=('Calibri', 14)).grid(row=0, sticky=W, pady=5)
        
            Label(emipayment, text="PAY EMI Rs."+str(loan_display_emi), font=('Calibri', 14)).grid(row=1, column=0,sticky=W, pady=5)
            
            
            def confirm_emi_payment():
                cursor22.execute("update studloan set Loan_paid= Loan_paid+"+str(loan_display_emi)+" where CustID="+ str(login_custid)+";")
                mycon.commit()
                cursor23.execute("update studloan set Loan_Balance= Loan_Balance - "+str(loan_display_emi)+" where CustID="+ str(login_custid)+";")
                mycon.commit()
                cursor24.execute("update studloan set Loan_InsD= Loan_InsD + 1 where CustID="+ str(login_custid)+";")
                mycon.commit()
                cursor25.execute("update studloan set Loan_defaults = Loan_defaults - 1 where (CustID="+ str(login_custid)+" and Loan_defaults>=1);")
                mycon.commit()
                if loan_display_tenure*12==(loan_display_Installments_done+1):
                    cursor26.execute("update studloan set Loan_status='REPAID' where CustID="+str(login_custid)+";")
                    mycon.commit()
                Label(emipayment, text="AMOUNT SUCCESSFULLY PAID", font=('Calibri', 20), fg="green").grid(row=2, sticky=W, pady=5)

                def close_emi_payment():
                    emipayment.destroy()
                    display_studloan_details.destroy()
                    display_studloan()


                Button(emipayment, text="CLOSE AND GO TO STUDENT LOAN DETAILS", command=close_emi_payment, font=('Calibri', 14), bg="#b2a6ed").grid(row=3, sticky=N, pady=10)
                
            Button(emipayment, text="CONFIRM", command= confirm_emi_payment, font=('Calibri', 12), bg="#b2a6ed").grid(row=2, sticky=N, pady=5)

        if loan_display_Installments_done < (12*loan_display_tenure):
            Button(display_studloan_details, text="PAY EMI", command=payemi, font=('Calibiri', 14), bg="#b2a6ed").grid(row=15, sticky=N, pady=5)

    elif statii=="REPAID":
        Label(display_studloan_details, text="AMOUNT PAID: ", font=('Calibri', 14)).grid(row=9, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text="Rs."+str(loan_display_sofarpaid), font=('Calibri', 14)).grid(row=9, column=2, sticky=W, pady=5)
        Label(display_studloan_details, text="REMAINING BALANCE: ", font=('Calibri', 14)).grid(row=10, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text="Rs."+str(loan_display_rem_balance), font=('Calibri', 14)).grid(row=10, column=2, sticky=W, pady=5)
        Label(display_studloan_details, text="LOAN HAS BEEN FULLY REPAI5D!", font=('Calibri bold', 18), fg="green").grid(row=11, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text="KINDLY VISIT ANY LOCAL BRANCH OFFICE OF MONETA BANK", font=('Calibri', 14)).grid(row=12, column=0, sticky=W, pady=5)
        Label(display_studloan_details, text="FOR RECEIPT OF DOCUMENTS REGARDING COMPLETION OF LOAN REPAYMENT", font=('Calibri', 14)).grid(row=13, column=0, sticky=W, pady=5)
        

    def go_out_of_studloan_to_dashboard():
        display_studloan_details.destroy()
        account_dashboard.destroy()
        login_session()

    Button(display_studloan_details, text="DASHBOARD", command=go_out_of_studloan_to_dashboard, font=('Calibri', 14), bg="#b2a6ed", fg="black").grid(row=0, column=100, sticky=E)
            
    

## Logging in after validation ##    
def login_session():
    global account_dashboard
    cursor2.execute("select CustID from login;")
    data= cursor2.fetchall()
    List_of_all_custids=[]
    for i in data:
        for j in i:
            List_of_all_custids.append(j)
    global login_custid
    global login_name

    login_custid = (temp_login_custid.get())
    
    login_password= temp_login_password.get()

    if login_custid=="" or login_password=="":
        login_notif.config(fg="red", text="ALL FIELDS REQUIRED")
        return
    try:
        login_custid= int(temp_login_custid.get())
    except:
        login_notif.config(bg="#bbf5ae", fg="red", text="INVALID CUSTOMERID FORMAT")

    for each_custid in List_of_all_custids:
        if each_custid==login_custid:
            acc=True
            break
    else:
        login_notif.config(fg="red", text="ACCOUNT DOES NOT EXIST")
        return
    if acc==True:
        cursor3.execute("select Name, Password, RandomNumber from login where CustID="+str(login_custid)+";")
        data3= cursor3.fetchone()
        pw= False
       
        for i in range(1):
 ########## DECRYPTION USING CAESAR CIPHER ALGORITHM ##########
            def getdecyphertext(rand_decypher, inchar): 
                asciival = ord(inchar)
                tmpasciival = asciival + rand_decypher

                if tmpasciival > 255:
                    outval = (tmpasciival - 255)
                else:
                    outval = tmpasciival

                return outval

            
            global login_name
            login_name= data3[0]
            
            encrypted_password = data3[1]
            rand_decypher = data3[2]

            decyphertext = ""
            for j in encrypted_password:
                decypherval = getdecyphertext(rand_decypher, j)
                decyphertext = decyphertext + chr(decypherval)

            if decyphertext== login_password:
                pw=True
                break
        else:
            login_notif.config(fg="red", text="PASSWORD INCORRECT")
            return
        if pw==True:
            try:
                login_screen.destroy()
            except:
                pass
            account_dashboard = Toplevel(master)
            account_dashboard.title('Dashboard')
            account_dashboard.config(bg="#bbf5ae")
            
            
            #Labels
            Label(account_dashboard, text= "CUSTOMER ID: "+str(login_custid), font=('Calibri', 14)).grid(row=0, column=0, sticky=W)
            Label(account_dashboard, text= "Account Dashboard", font=('Calibri', 14)).grid(row=0, sticky=N, pady=10)
            Label(account_dashboard, text= "WELCOME "+login_name.capitalize(), font=('Calibri', 14)).grid(row=1, sticky=N, pady=5)
            def logout():
                account_dashboard.destroy()
                loginsignup()
            Button(account_dashboard, text= "LOGOUT", command=logout, font=('Calibri', 14), bg="#b2a6ed", fg="black").grid(row=0, column=10, pady=5)
            #Buttons
            cursor4.execute("select FD, SB, StudLoan from Type_acc where CustID="+str(login_custid)+";")
            data4= cursor4.fetchone()
            #first checking status of sb acoount
            if data4[1]=='N':
                Button(account_dashboard, text="CREATE A SAVINGS BANK ACCOUNT", command=createsb, width=100, font=('Calibri', 14), bg="#b2a6ed").grid(row=3, sticky=N, pady=5)
           
            else:
                if data4[1]=='Y':
                    Button(account_dashboard, text="DISPLAY/ADD TO/WITHDRAW FROM SAVINGS", command=displaysb, width=100, font=('Calibri', 14), bg="#b2a6ed").grid(row=3, sticky=N, pady=5)
                if data4[0]=='N':
                    Button(account_dashboard, text="CREATE A FIXED DEPOSIT ACCOUNT", command=createfd, width=100, font=('Calibri', 14), bg="#b2a6ed").grid(row=4, sticky=N, pady=5)
                if data4[0]=='Y':
                    Button(account_dashboard, text="DISPLAY FIXED DEPOSIT ACCOUNT DETAILS", command=displayfd, width=100, font=('Calibri', 14), bg="#b2a6ed").grid(row=4, sticky=N, pady=5)
                if data4[2]=='N':
                    Button(account_dashboard, text="APPLY FOR A STUDENT LOAN", command= createstudloan, width=100, font=('Calibri', 14), bg="#b2a6ed").grid(row=5, sticky=N, pady=5)
                if data4[2]=='Y':
                    Button(account_dashboard, text="VIEW STUDENT LOAN DETAILS/ PAY EMI", command= display_studloan, width=100, font=('Calibri', 14), bg="#b2a6ed").grid(row=5, sticky=N, pady=5)
                    

## Login Screen ##        
def login():
    login_signup.destroy()
    #Variables
    global temp_login_custid
    global temp_login_password
    global login_notif
    global login_screen
    global login_custid
    temp_login_custid = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    login_screen.config(bg="#bbf5ae")
    #Labels
    Label(login_screen, text="Login to your account", font=('Calibri', 14)).grid(row=0, sticky=W)
    Label(login_screen, text="CustomerID", font=('Calibri', 14)).grid(row=1, sticky=W)
    Label(login_screen, text="Password", font=('Calibri', 14)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri', 14), bg="#bbf5ae")
    login_notif.grid(row=4, sticky=N)
    #Entry
    Entry(login_screen, textvariable= temp_login_custid).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable= temp_login_password, show="*").grid(row=2, column=1, padx=5)
    #Buttons
    global login_session
    Button(login_screen, text = "Login", command= login_session, width=17, font=('Calibri', 14), bg="#b2a6ed").grid(row=3, sticky=W, pady=5)

img= Image.open('onlb.png')
img= img.resize((500,350))
img= ImageTk.PhotoImage(img)

img2= Image.open('moneta_logo.png')
img2= img2.resize((100,67))
img2= ImageTk.PhotoImage(img2)


Label(master, image=img2).grid(row=0, column=0, sticky=N)
Label(master, text = "MONETA BANK", font=('Calibri',30), bg="#bbf5ae").grid(row=3, sticky=N)
Label(master, text= "Where your money is safe and growing", font=('Calibri',16, 'italic'), bg="#bbf5ae").grid(row=4, sticky=N)
Label(master, image=img).grid(row=5, sticky=N, pady=15)

## Main Screen for Login/SignUP ##
def loginsignup():
    global login_signup
    login_signup = Toplevel(master)
    login_signup.title('SignUp-Login Page')
    login_signup.config(bg="#bbf5ae")
    Label(login_signup, text = "MONETA BANK", font=('Calibri',30), bg="#bbf5ae").grid(row=0, sticky=N, pady=10)
    Label(login_signup, text= "Where your money is safe and growing", font=('Calibri',16, 'italic'), bg="#bbf5ae").grid(row=1, sticky=N)
    Label(login_signup, image=img).grid(row=2, sticky=N, pady=15)
    Button(login_signup, text= "Sign Up", font=('Calibri',14), width=20, command=signup, bg="#b2a6ed").grid(row=3, sticky=N)
    Button(login_signup, text="Login", font=('Calibri', 14), width=20, command=login, bg="#b2a6ed").grid(row=4, sticky=N, pady=12)

Button(master, text="Click to Login/SignUp Page", font=('Calibri', 14), bg="#b2a6ed", width=20, command=loginsignup).grid(row=6, sticky=N)

master.mainloop()






















