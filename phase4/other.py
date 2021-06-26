import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
from datetime import datetime

def print_query(query, con, cur):
    try:
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        if len(result) != 0:
            header = result[0].keys()
            rows =  [x.values() for x in result]
            print(tabulate(rows, header, tablefmt = 'grid'))
        else:
            print("Not found!")
    except Exception as e:
        print("Error!")
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to go to main menu")

def other_a(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Get Booking details by name of the Guest")
    print("Any other key to go back")
    while(1):
        attributes = {}
        ch = input("Enter choice -> ")
        if ch == '1':
            First_n = input('Enter the first name of guest: ')
            Last_n = input('Enter the last name of guest: ')
            fun = "SELECT Booking.Booking_Id, Hotel_Id,Status,Email,Contact_Number,Payment_Mode,Booking_Type,First_Name,Last_Name FROM Booking , Guest WHERE Booking.Booking_Id = Guest.Booking_Id AND First_Name = '"+First_n+"' AND Last_Name = '"+Last_n+"';"
            try:
                cur.execute(fun)
                con.commit()
                result = cur.fetchall()
                tfilter=result[0]["Booking_Type"]
                if len(tfilter) != 0:
                    if(tfilter=='R'):
                        query = "SELECT Booking.Booking_Id,Hotel_Id,Guest.First_Name,Guest.Last_Name,Status,Email,Contact_Number,Payment_Mode,Booking_Type,Number_of_Members,Number_of_Rooms,Room_Charges,Check_in,Check_out FROM Booking,Room_Booking,Guest WHERE Booking.Booking_Id=Room_Booking.Booking_Id  AND Booking.Booking_Id = Guest.Booking_Id AND First_Name = '"+First_n+"' AND Last_Name = '"+Last_n+"';"
                        print_query(query, con, cur)
                    elif (tfilter=='E'):
                        query = "SELECT Booking.Booking_Id,Hotel_Id,Guest.First_Name,Guest.Last_Name,Status,Email,Contact_Number,Payment_Mode,Booking_Type,Hall_Number,Hall_Charges,Number_of_Guest, Organised_By,Event_Starts_On,Event_Till,Duration FROM Booking,Event_Booking,Guest WHERE Booking.Booking_Id=Event_Booking.Booking_Id  AND Booking.Booking_Id = Guest.Booking_Id AND First_Name = '"+First_n+"' AND Last_Name = '"+Last_n+"';"
                        print_query(query, con, cur)
                    else :
                        print("Error!")

                else:
                    print("Error!")
            except Exception as exception:
                print("Error: Finding the Booking details")
                con.rollback()
                input("Press any key to continue.")
                return
            
        else:
            break

def other_b(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Get all hotels having available room > 10")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if ch == '1':
            fun = "SELECT Hotel_Id,Hotel_Name,Number_of_Room_available,Area,City,State FROM Hotel WHERE Number_of_Room_available > 10;"
            try:
                cur.execute(fun)
                con.commit()
                result = cur.fetchall()
                if len(result) != 0:
                    header = result[0].keys()
                    rows =  [x.values() for x in result]
                    print(tabulate(rows, header, tablefmt = 'grid'))
                else:
                    print("Not found!")
            except Exception as exception:
                print("Error: Finding the hotels")
                con.rollback()
                input("Press any key to continue.")
                return
        else:
            break

def other_c(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Profit Earned by a particular hotel in a particular year ")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if ch == '1':
            a = input('Enter the hotel id for the hotel: ')
            if not a.isnumeric():
                print("Please enter a correct hotel id for the hotel")
                print("Press any key to continue. ")
                return
            b = input('Enter the year for profit: ')
            if len(b) == 0:
                print("Please enter the year for the profit")
                print("Press any key to continue. ")
                return
            fun = "SELECT SUM(Total_Profit) FROM Expenditure,Ex_Profit WHERE Hotel_Id = "+a+" AND Year = "+b+" AND Expenditure.Income = Ex_Profit.Income AND Expenditure.Staff_Salary = Ex_Profit.Staff_Salary AND Expenditure.Extra_Expenses = Ex_Profit.Extra_Expenses;"
            try:
                cur.execute(fun)
                con.commit()
                result = cur.fetchall()
                if len(result) != 0:
                    header = result[0].keys()
                    rows =  [x.values() for x in result]
                    print(tabulate(rows, header, tablefmt = 'grid'))
                else:
                    print("Not found!")
            except Exception as exception:
                print("Error: Finding the Staff members")
                con.rollback()
                input("Press any key to continue.")
                return
        else:
            break

def other_d(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. List all staff member in a particular hotel")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if ch == '1':
            a = input('Enter the hotel id for the hotel: ')
            if not a.isnumeric():
                print("Please enter a correct hotel id for the hotel")
                print("Press any key to continue. ")
                return
            fun = "SELECT Staff.Employee_Id,Staff.Hotel_Id,Supervisor_Id,First_Name,Last_Name,Date_of_Birth,Contact_Number,Staff.Job_Type,Address,Salary FROM Staff,Staff_address,Staff_Salary WHERE Staff.Employee_Id=Staff_address.Employee_Id AND Staff.Job_Type=Staff_Salary.Job_Type AND Staff.Hotel_Id="+a+";"
            try:
                cur.execute(fun)
                con.commit()
                result = cur.fetchall()
                if len(result) != 0:
                    header = result[0].keys()
                    rows =  [x.values() for x in result]
                    print(tabulate(rows, header, tablefmt = 'grid'))
                else:
                    print("Not found!")
            except Exception as exception:
                print("Error: Finding the Staff members")
                con.rollback()
                input("Press any key to continue.")
                return
        else:
            break