# Hotel Database Management System
Project by - @Sibtain24

![Hotel DBMS](https://github.com/user-attachments/assets/84c1745c-93ca-4d6e-bf02-1b99e469cd5d)

This is a program made using Python and MySQL to manage the data of Customers Checking-in to a hotel. This program provides an user-friendly UI to the user and provides functionality to Add, Update, Delete, View and Search the details of all the Customers present in the MySQL database. This program uses Python's Tkinter module to create the Graphical User Interface (GUI) and uses MySQL Client app to store data in the backend. It is a fully functional program with a good UI. To use this program, refer to the instructions below:

# Instructions to use this Program or Application

1) First of all make sure you have both Python and MySQL installed in your Computer. (Both applications can be downloaded from their respective Official Websites)
   
2) Then, open your MySQL Command Line Application and create a database in mySQL with name - "hotel_dbms". Or Copy and Paste this: `create database hotel_dbms`

3) Then, Copy and Paste this: `use hotel_dbms`

4) After that, Copy and Paste the following text: <br>
  `create table info (GuestNo integer(4), GuestName varchar(30), Age integer(3), Gender varchar(6), Address varchar(80), ContactNo bigint(10), RoomNo integer(4), CheckinDate date, CheckoutDate date);`

5) Find the following line in 'main.py' file and change the Username (user) and Password (passwd) to your MySQL Client app username & password:<br>
   `mydb = mysql.connector.connect(host="localhost", user="root", passwd='root')`

6) After following all the above steps, open the 'main.py' file to run the software program in your computer and to manage your customer details in MySQL database.

Note: When you run the program file, it will ask for Password in the Software's Verification Window. Enter this password: `admin@123` and click on verify button.
(You can change this password by finding and replacing the text-"admin@123" in the 'main.py' file)
