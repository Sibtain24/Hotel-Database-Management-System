# Hotel Database Management System
Project by - @Sibtain24

![Hotel DBMS](https://github.com/user-attachments/assets/84c1745c-93ca-4d6e-bf02-1b99e469cd5d)

This is a program made using Python and MySQL to manage the data of Customers Checking-in to a hotel. This program provides an user-friendly UI to the user and provides functionality to Add, Update, Delete, View and Search the details of all the Customers present in the MySQL database. This program uses Python's Tkinter module to create the Graphical User Interface (GUI) and uses MySQL Client app to store data in the backend. It is a fully functional program with a good UI. To use this program, refer to the instructions below:

# Instructions to use this Program or Application:

1) First of all make sure you have both Python and MySQL installed in your Computer. (Both applications can be downloaded from their respective Official Websites)

2) Next step is to download a module called mysql.connector. For that, open Windows Terminal and type this: `pip install mysql-connector-python`

3) Now, open the 'main.py' file in Python IDLE or Visual Studio Code. Find the following line in 'main.py' file and change the Username (user) and Password (passwd) to your MySQL Client app username & password:<br>
   `mydb = mysql.connector.connect(host="localhost", user="root", passwd='root')` <br> [ And save the file using "Ctrl + S" keyboard shortcut.]

4) If you want to connect an online MySQL Server, change the host name (host), username (user) and password (passwd) in the 'main.py' file and save the file using 'Ctrl + S' keyboard shortcut.

5) Then, open your MySQL Command Line Application and create a database in mySQL with name - "hotel_dbms". Or Copy and Paste this: `create database hotel_dbms;`

6) Then, Copy and Paste this: `use hotel_dbms;`

7) After that, Copy and Paste the following text: <br>
  `create table info (GuestNo integer(4), GuestName varchar(30), Age integer(3), Gender varchar(6), Address varchar(80), ContactNo bigint(10), RoomNo integer(4), CheckinDate date, CheckoutDate date);`

8) After following all the above steps, open the 'main.py' file to run the software program in your computer and to manage your customer details in MySQL database.

To know about how to manage data, refer to the "How-to" Guide below:

# How to Use the Program to Manage Database❓

1) As soon as you run the Program, an encryption windows will appear. Enter the Password and Click on Verify. The password is: `admin@123` (Password can be changed by changing the code in 'main.py' file and saving the file).

2) After you click on Verify, the main windows of the program will appear. On the Left side of the window you will see Entry Fields to Enter, Update and Delete the data of Customers. And on the Right side you will see the data you enter in a Tabular Format. Just above the Table, there is a 'Search Box', a 'Search Filter', a 'Search Button' and 'Show All Button'.

3) To Add Customer Details in the Database, fill in the Entry Fields and Click on the 'Add Button'. A Message will appear and the data will be added in the database, and details of all customers will appear on the table. (Note: The format to enter dates is 'yyyy-mm-dd')

4) You can change / correct the data using Update function. For that, Left Click on the data of the Customer displaying on the Table to select and then change that data you want to update in the Entry Field and Click on 'Update Button'.

5) To Delete a Customer's details from the data base, Click on the data of the Customer displaying on the Table to select and then Click on the 'Delete Button'.

6) A 'Clear All Button' is also present in below the entry fields. Its function is to Clear all the Entry fields at once.

7) Above the Table, there is a 'Search Filter'(Combo Box), where you can choose what type of data you want to search in the table, and you can enter what you want to search in the 'Search Box'. For Example, you selected 'Age' in the Search Filter, then you Entered '20' in the Search Box, and when you click on the Search Button, the data of all the Customers of Age-20 will display on the table. When you are done searching, Click on the 'Show All Button' to display all the data on the table.

***Thank You for using my Program. Feel free to give your valuable feedback.*** 😊
