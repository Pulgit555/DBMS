import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
import datetime
DBS = os.getenv("DB_NAME")
from delete import *
from add import *
from view import *
from update import *
from other import *


def add_catlog():
    while(1):
        tmp = sp.call('clear', shell=True)
        print("1. Add a Hotel")
        print("2. Add a Booking")
        print("3. Add a Staff")
        print("4. Add a Recreational Activity")
        print("5. Add a Expenditure")
        print("6. Add a Aviled relation")
        print("Any other key to go back to main menu")
        a = input("Enter choice table to add-> ")
        if(a == '1'): 
            add_Hotel(cur,con)
        elif(a == '2'):
            add_Booking(cur,con)
        elif(a == '3'):
            add_Staff(cur,con)
        elif(a == '4'):
            add_Re_Activity(cur,con)
        elif(a == '5'):
            add_Expenditure(cur,con)
        elif(a == '6'):
            add_Avail(cur,con)
        else : 
            break
    
def delete_catlog():
    while(1):
        tmp = sp.call('clear', shell=True)
        print("1. Delete from the table Hotel")
        print("2. Delete from the table Booking")
        print("3. Delete from the table Staff")
        print("4. Delete from the table Recreational Activity")
        print("5. Delete from the table Expenditure")
        print("Any other key to go back to main menu")
        a = input("Enter table number to delete from-> ")
        if(a == '1'): 
            delete_Hotel(cur,con)
        elif(a == '2'):
            delete_Booking(cur,con)
        elif(a == '3'):
            delete_Staff(cur,con)
        elif(a == '4'):
            delete_Re_Activity(cur,con)
        elif(a == '5'):
            delete_Expenditure(cur,con)
        else : 
            break

    
def update_catlog():
    while(1):
        tmp = sp.call('clear', shell=True)
        print("1. Update delails of a Hotel")
        # print("2. Update delails of a Booking")
        # print("3. Update delails of a Guest")
        print("2. Update delails of a Staff")
        print("3. Update delails of a Recreational Activity")
        print("4. Update salary of staff ")
        # print("7. Update delails of a Availed")
        # print("8. Update delails of final charges")
        print("Any other key to go back to main menu")
        a = input("Enter choice table to add-> ")
        if(a == '1'): 
            update_Hotel(cur,con)
        elif(a == '2'):
            update_Staff(cur,con)
        elif(a == '3'):
            update_Re_Activity(cur,con)
        elif(a == '4'):
            update_sal(cur,con)
        else:
            break



def view_catlog():
    while(1):
        tmp = sp.call('clear', shell=True)
        print("1. View all Hotels")
        print("2. View all Booking details")
        print("3. View all Guest details")
        print("4. View all Staff details")
        print("5. View monthly Expenditure")
        print("6. View all Reacretional Activities")
        print("7. View all activities availed by guest")
        print("Any other key to go back to main menu")
        a = input("Enter choice dis-> ")
        if(a == '1'): 
            view_Hotel(cur,con)
        elif(a == '2'):
            view_Booking(cur,con)
        elif(a == '3'):
            view_Guest(cur,con)
        elif(a == '4'):
            view_Staff(cur,con)
        elif(a == '5'):
            view_Expenditure(cur,con)
        elif(a == '6'):
            view_Re_Activity(cur,con)
        elif(a == '7'):
            view_Availed(cur,con)
        else:
            break

def other_catlog():
    while(1):
        tmp = sp.call('clear', shell=True)
        print("1. Getting booking details by name of guest for which booking was made. where Guest name is X Y")
        print("2. List of all hotel having available room > 10")
        print("3. Profit earned every Year by each hotel")
        print("4. List of all staff member in a particular hotel")
        print("Any other key to go back to main menu")
        a = input("Enter choice dis-> ")
        if(a == '1'):
            other_a(cur,con)
        elif(a == '2'):
            other_b(cur,con)
        elif(a == '3'):
            other_c(cur,con)
        elif(a == '4'):
            other_d(cur,con)
        else:
            break


def main_catlog(x):
    if(x == '1'): 
        add_catlog()
    elif(x == '2'):
        delete_catlog()
    elif(x == '3'):
        update_catlog()
    elif(x == '4'):
        view_catlog()
    elif(x == '5'):
        other_catlog()
    else:
        print("Error: Invalid Option")


while (1):
    tmp = sp.call('clear', shell=True)
    print("Please enter your credentials")
    username = input("Username: ")
    password = input("Password: ")
  
    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db=DBS,
                              port=5005,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Add")
                print("2. Delete")
                print("3. Update")
                print("4. View")
                print("5. Others")
                print("6. Logout")
                print("7. Exit")
                x = input("Enter choice -> ")
                tmp = sp.call('clear',shell=True)
                
                if x == '6':
                    break
                elif x == '7':
                    print("====================================================================")
                    print("                             BYE!!!                                 ")
                    print("====================================================================")
                    input("                  Press any key to confirm exit                     ")
                    raise SystemExit
                else:
                    main_catlog(x)
                    # input("Press any key to continue.")


    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
