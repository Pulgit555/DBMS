# How to run
+ Set up docker for MySQL
	+ Start a docker container
	+ run following commands in same folder `phase4` to load sql file:-
		+ `mysql -h 127.0.0.1 -u <YOUR_USERNAME> --port=5005 -p < phase4.sql`
		+ `mysql -h 127.0.0.1 -u <YOUR_USERNAME> --port=5005 -p < data.sql`
+  For setting up CLI in python by using :-  
	+ Download everything which is mentioned in requirements.txt file by 
		+ `pip install -r requirements.txt`  **or**  `pip3 install -r requirements.txt` (if you have 2 python setup)  
	+ Then run the main.py file by using :-
		+ `python main.py` **or** `python3 main.py`

# Introduction
Created the database for hotel management system and performed queries on the database using MySQL CLI with Python using PyMySQL library.

# Funtions Provided In Program
## Add
In add function we can add :-
1) Hotel
2) Booking
3) Staff
4) Recreational activity
5) Expenditure
6) Availed relation

## Delete
In delete function we can detele :-
1) Hotel
2) Booking
3) Staff
4) Recreational activity
5) Expenditure

## Update
In update function we can update :-
1) Hotel
2) Staff
3) Recreational activity
4) Staff salary

## View
In view function we can view :-
1) Hotels
2) Booking details
3) Guest details
4) Staff details
5) Monthly Expenditure
6) Reacretional Activities
7) Activities availed by guest

## Others
Some other functions which we can use :-
1) Getting booking details by name of guest for which booking was made. where Guest name is X Y.
2) List of all hotel having available room > 10.
3) Profit earned every Year by each hotel.
4) List of all staff member in a particular hotel.

*there are some extra function as sub-feature of previous mentioned functions*

*this is a group project created by Pulkit Gupta, Aaditya Sharma and Archit Jain.*
