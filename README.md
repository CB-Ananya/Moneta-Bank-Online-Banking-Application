## Moneta-Bank-Online-Banking-Application

# Synopsis
Scope of Moneta Bank project
The project aims to develop an online banking platform where following banking functions can be serviced through this computer application in Python and MySQL:
1.	Savings Bank Account (Deposits)
2.	Fixed Deposit Account (Deposits)
3.	Student Loan (Lending)



# To run the application: 
modules required:
1. mysql.connector
   	```bash
	pip3 install mysql.connector
	```
3. tkinter
   	```bash
    	pip3 install tk
    	```
4. PIL (pillow)
	```bash
 	pip3 install pillow
 	```
5. os
6. random
7. datetime

Firstly, create the mysql tables in MySQL Command Line Client using the commands in CreateTables.txt

In all python files:
mycon = sqltor.connect(...)
give your hostname, username, password and database name as values for the parameters

-> To start the application: run Main-Interface.py
   User interface proided by Main-Interface.py

# For records to be maintained consistent (interest calculation purposes):
   run:
	-> fd-daily-run.py
 
	-> sb-daily-run.py
 
	-> studloan-daily-run.py 
 
   files once every day 

   and
	-> fd-quarterly-run.py
 
 	-> sb-quarterly run.py 
  
   files every 3 months from the first day of running the main program.


For detailed walkthrough and other implementation details- Check out the project report
