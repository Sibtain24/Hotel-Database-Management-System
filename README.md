# Hotel-Management-System
Program developed by - Sibtain Raza

If you want to use our project, then first all you need is to follow the following steps:

1) First create a database in mySQL with name - "hotel_dbms".

You can copy this: create database hotel_dbms

2) Then using hotel_dbms create a table - " info " with the following fieldnames [Note: The spellings of all the field names must be same as following otherwise the program may not run correctly]

GuestNo, GuestName, Age, Gender, Address, ContactNo, RoomNo, CheckinDate and CheckoutDate.

Or copy the following text line by line and paste it:

create table info (GuestNo integer(4), GuestName varchar(30), Age integer(3), Gender varchar(6), Address varchar(80), ContactNo bigint(10), RoomNo integer(4), CheckinDate date, CheckoutDate date);

3) Find the following line in main.py file and change the Username(user) and Password(passwd) as your mySQL username & password:

mydb = mysql.connector.connect(host="localhost", user="root", passwd='root')

Now you can use our software and manage your customer details/database.

Also, when you run the project file it will ask for Password in the Software's Verification Window which is "admin@123" 
(You can change this password by finding and replacing "admin@123" in the code)
