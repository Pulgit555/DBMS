# How to run
+ Set up docker for MySQL
	+ Start a docker container
	+ run following commands in same folder `P*` to load sql file:-
		+ `mysql -h 127.0.0.1 -u <YOUR_USERNAME> --port=5005 -p < phase4.sql`
		+ `mysql -h 127.0.0.1 -u <YOUR_USERNAME> --port=5005 -p < data.sql`
+  For setting up CLI in python by using :-  
	+ Download everything which is mentioned in requirements.txt file by 
		+ `pip install -r requirements.txt`  **or**  `pip3 install -r requirements.txt` (if you have 2 python setup)  
	+ Then run the main.py file by using :-
		+ `python main.py` **or** `python3 main.py`

# Introduction
This is program for MySQL-CLI with python using PyMySQL which is made for a hotel chain management company as our Data and Application course project. We have tried to cover all fields as we can which are present in a database for Hotel management.

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

### Repititve Tasks
Due to the repition of a particular format in functions of similar kind; we implemented only some of them just to fulfil this projects needs and extended some function due to increase in deadline :relaxed:

# Creaters

|Archit Jain   | Aaditya Sharma  | Pulkit Gupta |
|--------------|-----------------|--------------|
|  2019101053  |    2019113009   |  2019101078|
+ ======================================================================== 
+ .            HERE WE MARK THE END OF OUR GROUP PROJECT
+ ========================================================================


