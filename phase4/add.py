import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import datetime
import re
regex = '^[a-z0-9]+[\
._]?[a-z0-9]+[@]\
w+[.]\
w{2,3}$'
def attributes_keys(d):
    s = ''
    for key in d.keys():
        s = s + key + ', '
    
    if s[-2:] == ', ':
        return s[:-2]
    return s

def add_Hotel(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Add a new Hotel")
    print("Any other key to go back")
    while(1):
        attributes = {}
        ch = input("Enter choice -> ")
        if (ch == '1'):
            print('Enter the details of new hotel:')
            attributes['Hotel_Id'] = input('Enter the Hotel\'s ID: ')
            if len(attributes['Hotel_Id']) == 0:
                print('Error : Please enter the Hotel_Id of hotel')
                input('Press any key to continue.')
                return
            attributes['Hotel_Name'] = input('Name: ')
            if len(attributes['Hotel_Name']) == 0:
                print('Error : Please Enter the hotel name')
                input('Press any key to continue.')
                return
            attributes['Number_of_Room_available'] = input('Number of Rooms available: ')
            if not attributes['Number_of_Room_available'].isnumeric():
                print('Please enter a number of rooms correctly')
                input('Press any key to continue.')
                return
            attributes['Area'] = input('Area: ')
            if len(attributes['Area']) == 0:
                print('Error : Please enter the Area of hotel')
                input('Press any key to continue.')
                return
            attributes['City'] = input('City: ')
            if len(attributes['City']) == 0:
                print('Error : Please enter the City of hotel')
                input('Press any key to continue.')
                return
            attributes['State'] = input('State: ')
            if len(attributes['State']) == 0:
                print('Error : Please enter the State of hotel')
                input('Press any key to continue.')
                return
            add = f'INSERT INTO HOTELMANAGEMENT.Hotel({attributes_keys(attributes)}) VALUES({attributes["Hotel_Id"]},"{attributes["Hotel_Name"]}",{attributes["Number_of_Room_available"]},"{attributes["Area"]}","{attributes["City"]}","{attributes["State"]}"); '
            try:
                cur.execute(add)
                con.commit()
                print('New Hotel details have been successfully added to the database')
                input('Press any key to continue')
            except Exception as exception:
                print('Failed to insert hotel into the database.')
                con.rollback()
                print(exception)
                input('Press any key to continue.')
                return 
            # Hotel_Id = attributes['Hotel_Id']
            # no_of_contact_no = input('Enter number of contacts you want to add: ')
            # i=1
            # while(no_of_contact_no > 0):
            #     contacts = {}
            #     print('ContactNo.')
            #     contacts['a'] = input(i)
            #     if not contacts['a'].isnumeric() or not len(contacts['a']) == 10 or not contacts['a'] == '':
            #         print('Please enter a valid conact number')
            #         print('Enter again this number correctly')
            #     else:
            #         no_of_contact_no = no_of_contact_no - 1
            #         i = i + 1
            #         add = f'INSERT INTO HOTELMANAGEMENT.Hotel_contact VALUES({Hotel_Id},"{contacts["a"]}"); '
            #         try:
            #             cur.execute(add)
            #             con.commit()
            #             print('New Hotel details have been successfully added to the database')
            #             input('Press any key to continue')
            #         except Exception as exception:
            #             print('Failed to insert Contact into the database.')
            #             con.rollback()
            #             print(exception)
            #             input('Press any key to continue.')
            #             return 
            break
        else:
            break

def add_Booking(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Add a new booking")
    print("Any other key to go back")
    while(1):
        attributes = {}
        ch = input("Enter choice -> ")
        if (ch == '1'):
            attributes['Booking_Id'] = input('Enter the booking id for the booking : ')
            if len(attributes['Booking_Id']) == 0 or not attributes['Booking_Id'].isnumeric():
                print('Error : Please enter booking id for the booking ')
                input('Press any key to continue.')
                return
            attributes['Hotel_Id'] = input('Enter the Hotel\'s ID: ')
            if len(attributes['Hotel_Id']) == 0:
                print('Error : Please enter the Hotel_Id of hotel')
                input('Press any key to continue.')
                return
            attributes['Status'] = input('Enter the status of booking: ')
            if len(attributes['Status']) == 0:
                print('Error : Please enter the Status of booking')
                input('Press any key to continue.')
                return
            attributes['Email'] = input('Enter the email for booking: ')
            if len(attributes['Email']) == 0 or re.search(regex,attributes['Email']) == 0:
                print('Error : Please enter vaild Email id for booking')
                input('Press any key to continue.')
                return
            attributes['Contact_Number'] = input('Enter the contact number for booking: ')
            if not len(attributes['Contact_Number']) == 10 or not attributes['Contact_Number'].isnumeric():
                print('Error : Please enter the a valid contact number for booking')
                input('Press any key to continue.')
                return
            attributes['Payment_Mode'] = input('Enter the payment mode for booking: ')
            if len(attributes['Payment_Mode']) == 0:
                print('Error : Please enter the payment mode for booking')
                input('Press any key to continue.')
                return
            attributes['Booking_Type'] = input('Enter the booking type (E-Event booking and R-Room booking) for booking: ')
            if len(attributes['Booking_Type']) == 0 or (not attributes['Booking_Type'] == 'E' and not attributes['Booking_Type'] == 'R'):
                print('Error : Please enter the booking type for booking')
                input('Press any key to continue.')
                return
            add = f'INSERT INTO HOTELMANAGEMENT.Booking({attributes_keys(attributes)}) VALUES({attributes["Booking_Id"]},{attributes["Hotel_Id"]},"{attributes["Status"]}","{attributes["Email"]}","{attributes["Contact_Number"]}","{attributes["Payment_Mode"]}","{attributes["Booking_Type"]}"); '
            try:
                cur.execute(add)
                con.commit()
                print('New Booking details have been successfully added to the database')
                input('Press any key to continue')
            except Exception as exception:
                print('Failed to insert a new Booking into the database.')
                con.rollback()
                print(exception)
                input('Press any key to continue.')
                return
            Booking_Id = attributes['Booking_Id']
            attributes_E = {}
            attributes_R = {}
            attributes_F = {}
            n_guest=0
            if attributes['Booking_Type'] == 'E':
                attributes_E['Hall_Number'] = input('Enter the hall number for event: ')
                if len(attributes_E['Hall_Number']) == 0:
                    print('Error : Please enter the correct hall number for event')
                    input('Press any key to continue.')
                    return
                attributes_E['Hall_Charges'] = input('Enter the hall charges for event: ')
                if len(attributes_E['Hall_Charges']) == 0 or not attributes_E['Hall_Charges'].isnumeric():
                    print('Error : Please enter the valid hall charges for event')
                    input('Press any key to continue.')
                    return
                attributes_E['Number_of_Guest'] = input('Enter the number of guests for event: ')
                if len(attributes_E['Number_of_Guest']) == 0 or not attributes_E['Number_of_Guest'].isnumeric():
                    print('Error : Please enter the correct number of guests for event')
                    input('Press any key to continue.')
                    return
                attributes_E['Organised_By'] = input('Enter the organiser for event: ')
                if len(attributes_E['Organised_By']) == 0:
                    print('Error : Please enter the organiser for event')
                    input('Press any key to continue.')
                    return
                attributes_E['Event_Starts_On'] = input('Enter the start date and time for event as YYYY-MM-DD HH:MM : ')
                if len(attributes_E['Event_Starts_On']) == 0:
                    print('Error : Please enter the start date and time for event')
                    input('Press any key to continue.')
                    return
                attributes_E['Event_Till'] = input('Enter the end date and time for event as YYYY-MM-DD HH:MM : ')
                if len(attributes_E['Event_Till']) == 0:
                    print('Error : Please enter the end date and time for event')
                    input('Press any key to continue.')
                    return
                attributes_E['Duration'] = input('Enter the Duration of the event: ')
                if len(attributes_E['Duration']) == 0 or not attributes_E['Duration'].isnumeric():
                    print('Error : Please enter the valid Duration for event')
                    input('Press any key to continue.')
                    return
                n_guest = attributes_E['Number_of_Guest']
                add = f'INSERT INTO HOTELMANAGEMENT.Event_Booking VALUES({Booking_Id},"{attributes_E["Hall_Number"]}",{attributes_E["Hall_Charges"]},{attributes_E["Number_of_Guest"]},"{attributes_E["Organised_By"]}","{attributes_E["Event_Starts_On"]}","{attributes_E["Event_Till"]}",{attributes_E["Duration"]}); '
                try:
                    cur.execute(add)
                    con.commit()
                    print('New Booking details have been successfully added to the database')
                    input('Press any key to continue')
                except Exception as exception:
                    print('Failed to insert a new Event Booking into the database.')
                    con.rollback()
                    print(exception)
                    input('Press any key to continue.')
                    return
                # attributes_F['Hall_Charges'] = attributes_E['Hall_Charges']
                # attributes_F['Event_Starts_On'] = attributes_E['Event_Starts_On']
                # attributes_F['Event_Till'] = attributes_E['Event_Till']
                # attributes_F['Duration'] = attributes_E['Duration']
                # attributes_F['Final_charges'] = attributes_F['Hall_Charges']*attributes['Duration']
                # add = f'INSERT INTO HOTELMANAGEMENT.B_Final_Charge({attributes_keys(attributes_F)}) VALUES({attributes_F["Hall_Charges"]},"{attributes_F["Event_Starts_On"]}","{attributes_F["Event_Till"]}",{attributes_F["Duration"]},{attributes_F["Final_charges"]}); '
                # try:
                #     cur.execute(add)
                #     con.commit()
                #     print('New Final charges details have been successfully added to the database')
                #     input('Press any key to continue')
                # except Exception as exception:
                #     print('Failed to insert a new charges details in booking into the database.')
                #     con.rollback()
                #     print(exception)
                #     input('Press any key to continue.')
                #     return
            else:
                attributes_R['Number_of_Members'] = input('Enter the number of guests for room boking: ')
                if len(attributes_R['Number_of_Members']) == 0 or not attributes_R['Number_of_Members'].isnumeric():
                    print('Error : Please enter the correct number of guests for room')
                    input('Press any key to continue.')
                    return
                attributes_R['Number_of_Rooms'] = input('Enter the number of rooms needed: ')
                if len(attributes_R['Number_of_Rooms']) == 0 or not attributes_R['Number_of_Rooms'].isnumeric():
                    print('Error : Please enter the valid number of rooms needed')
                    input('Press any key to continue.')
                    return
                attributes_R['Room_Charges'] = input('Enter the charges for Room: ')
                if len(attributes_R['Room_Charges']) == 0 or not attributes_R['Room_Charges'].isnumeric():
                    print('Error : Please enter the correct charges for Room')
                    input('Press any key to continue.')
                    return
                attributes_R['Check_in'] = input('Enter the check in date YYYY-MM-DD for room: ')
                if len(attributes_R['Check_in']) == 0:
                    print('Error : Please enter the check in date for room')
                    input('Press any key to continue.')
                    return
                attributes_R['Check_out'] = input('Enter the check out date YYYY-MM-DD for room: ')
                if len(attributes_R['Check_out']) == 0:
                    print('Error : Please enter the check out date for room')
                    input('Press any key to continue.')
                    return
                n_guest = attributes_R['Number_of_Members']
                add = f'INSERT INTO HOTELMANAGEMENT.Room_Booking VALUES({Booking_Id},{attributes_R["Number_of_Members"]},{attributes_R["Number_of_Rooms"]},{attributes_R["Room_Charges"]},"{attributes_R["Check_in"]}","{attributes_R["Check_out"]}"); '
                try:
                    cur.execute(add)
                    con.commit()
                    print('New Booking details have been successfully added to the database')
                    input('Press any key to continue')
                except Exception as exception:
                    print('Failed to insert a new Room Booking into the database.')
                    con.rollback()
                    print(exception)
                    input('Press any key to continue.')
                    return
                # attributes_F['Number_of_Rooms'] = attributes_R['Number_of_Rooms']
                # attributes_F['Room_Charges'] = attributes_R['Room_Charges']
                # attributes_F['Check_in'] = attributes_R['Check_in']
                # attributes_F['Check_out'] = attributes_R['Check_out']
                # attributes_F['Final_charges'] = attributes_F['Number_of_Rooms']*attributes_F['Room_Charges']*(attributes_F['Check_out']-attributes_F['Check_in'])
                # add = f'INSERT INTO HOTELMANAGEMENT.B_Final_Charge({attributes_keys(attributes_F)}) VALUES({attributes_F["Number_of_Rooms"]},{attributes_F["Room_Charges"]},"{attributes_F["Check_in"]}","{attributes_F["Check_out"]}",{attributes_F["Final_charges"]}); '
                # try:
                #     cur.execute(add)
                #     con.commit()
                #     print('New Final charges details have been successfully added to the database')
                #     input('Press any key to continue')
                # except Exception as exception:
                #     print('Failed to insert a new charges details in booking into the database.')
                #     con.rollback()
                #     print(exception)
                #     input('Press any key to continue.')
                #     return
            # while n_guest > 0:
            #     attributes_G = {}
            #     attributes_G['Guest_Id'] = input('Enter the guest id for the guest : ')
            #     if len(attributes_G['Guest_Id']) == 0 or not attributes_G['Guest_Id'].isnumeric():
            #         print('Error : Please enter guest id for the guest')
            #         input('Press any key to continue.')
            #         return
            #     attributes_G['Booking_Id'] = Booking_Id
            #     attributes_G['Age'] = input('Enter the Age of guest: ')
            #     if len(attributes_G['Age']) == 0 or not attributes_G['Age'].isnumeric():
            #         print('Error : Please enter the valid age of guest')
            #         input('Press any key to continue.')
            #         return
            #     attributes_G['First_Name'] = input('Enter the First Name of guest: ')
            #     if len(attributes_G['First_Name']) == 0:
            #         print('Error : Please enter the First name of guest')
            #         input('Press any key to continue.')
            #         return
            #     attributes_G['Last_Name'] = input('Enter the Last Name of guest: ')
            #     if len(attributes_G['Last_Name']) == 0:
            #         print('Error : Please enter the Last name of guest')
            #         input('Press any key to continue.')
            #         return
            #     attributes_G['Gender'] = input('Enter the gender(M/F/O) of guest: ')
            #     if len(attributes_G['Gender']) == 0 or (not attributes_G['Gender'] == 'M' and not attributes_G['Gender'] == 'F' and not attributes_G['Gender'] == 'O'):
            #         print('Error : Please enter correctly gender of guest')
            #         input('Press any key to continue.')
            #         return
            #     add = f'INSERT INTO HOTELMANAGEMENT.Guest({attributes_keys(attributes_G)}) VALUES({attributes_G["Guest_Id"]},{attributes_G["Booking_Id"]},{attributes_G["Age"]},"{attributes_G["First_Name"]}","{attributes_G["Last_Name"]}","{attributes_G["Gender"]}"); '
            #     try:
            #         cur.execute(add)
            #         con.commit()
            #         print('New guest details have been successfully added to the database')
            #         input('Press any key to continue')
            #     except Exception as exception:
            #         print('Failed to insert a new Guest into the database.')
            #         con.rollback()
            #         print(exception)
            #         input('Press any key to continue.')
            #         return
            break
        else:
            break
    

def add_Staff(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Add a new Staff")
    print("Any other key to go back")
    while(1):
        attributes = {}
        ch = input("Enter choice -> ")
        if (ch == '1'):
            attributes['Employee_Id'] = input('Enter the Employee Id of the staff member : ')
            if len(attributes['Employee_Id']) == 0 or not attributes['Employee_Id'].isnumeric():
                print('Error : Please enter the Employee Id of the staff member')
                input('Press any key to continue.')
                return
            attributes['Supervisor_Id'] = input('Enter the supervisor id for the staff member: ')
            if len(attributes['Supervisor_Id']) == 0 or not attributes['Supervisor_Id'].isnumeric():
                print('Error : Please enter supervisor id of staff member')
                input('Press any key to continue.')
                return
            attributes['Hotel_Id'] = input('Enter the hotel id for the hotel in which staff member works: ')
            if len(attributes['Hotel_Id']) == 0 or not attributes['Hotel_Id'].isnumeric():
                print('Error : Please enter hotel id for the hotel of staff member')
                input('Press any key to continue.')
                return
            attributes['First_Name'] = input('Enter the first name of the staff member: ')
            if len(attributes['First_Name']) == 0:
                print('Error : Please enter the first name of staff member')
                input('Press any key to continue.')
                return
            attributes['Last_Name'] = input('Enter the last name of the staff member: ')
            if len(attributes['Last_Name']) == 0:
                print('Error : Please enter the last name of staff member')
                input('Press any key to continue.')
                return
            attributes['Date_of_Birth'] = input('Enter the Date of Birth (YYYY-MM-DD)of the staff member: ')
            if len(attributes['Date_of_Birth']) == 0:
                print('Error : Please enter the DOB of staff member')
                input('Press any key to continue.')
                return
            attributes['Contact_Number'] = input('Enter the contact number for Staff: ')
            if not len(attributes['Contact_Number']) == 10 or not attributes['Contact_Number'].isnumeric():
                print('Error : Please enter the a valid contact number for Staff')
                input('Press any key to continue.')
                return
            attributes['Job_Type'] = input('Enter the job type for Staff: ')
            if len(attributes['Job_Type']) == 0:
                print('Error : Please enter the a valid job type for Staff')
                input('Press any key to continue.')
                return
            add = f'INSERT INTO HOTELMANAGEMENT.Staff({attributes_keys(attributes)}) VALUES({attributes["Employee_Id"]},{attributes["Supervisor_Id"]},{attributes["Hotel_Id"]},"{attributes["First_Name"]}","{attributes["Last_Name"]}","{attributes["Date_of_Birth"]}","{attributes["Contact_Number"]}","{attributes["Job_Type"]}"); '
            try:
                cur.execute(add)
                con.commit()
                print('New Staff member details have been successfully added to the database')
                input('Press any key to continue')
            except Exception as exception:
                print('Failed to insert a new staff member into the database.')
                con.rollback()
                print(exception)
                input('Press any key to continue.')
                return
            # Employee_Id = attributes['Employee_Id']
            # no_of_addresses = input('How many addresses for staff You want to add')
            # if not no_of_addresses.isnumeric() or no_of_addresses == 0:
            #     print('Error : Please enter valid Number')
            #     input('Press any key to continue.')
            #     return
            # i=1
            # while(no_of_addresses > 0):
            #     addresses['add']
            #     print(Address)
            #     addresses['add'] = input(i)
            #     if len(addresses['add']) == 0:
            #         print('Please enter a valid address')
            #         print('Enter again this address again correctly')
            #     else:
            #         no_of_addresses = no_of_addresses - 1
            #         i = i + 1
            #         add = f'INSERT INTO HOTELMANAGEMENT.Staff_address VALUES({Employee_Id},"{addresses["add"]}"); '
            #         try:
            #             cur.execute(add)
            #             con.commit()
            #             print('New Staff addresses details have been successfully added to the database')
            #             input('Press any key to continue')
            #         except Exception as exception:
            #             print('Failed to insert address of staff into the database.')
            #             con.rollback()
            #             print(exception)
            #             input('Press any key to continue.')
            #             return 
            # Hotel_Id = attributes['Hotel_Id']
            # Job_Type = attributes['Job_Type']
            # attributes['Salary'] = input('Enter the Salary for this staff member: ')
            # if len(attributes['Salary']) == 0 or not attributes['Salary'].isnumeric():
            #     print('Error : Please enter a valid salary for the staff member')
            #     input('Press any key to continue.')
            #     return
            # add = f'INSERT INTO HOTELMANAGEMENT.Staff_Salary VALUES({Hotel_Id},"{Job_Type}",{attributes["Salary"]}); '
            # try:
            #     cur.execute(add)
            #     con.commit()
            #     print('New Staff member details have been successfully added to the database')
            #     input('Press any key to continue')
            # except Exception as exception:
            #     print('Failed to insert into the database.')
            #     con.rollback()
            #     print(exception)
            #     input('Press any key to continue.')
            #     return 
            break
        else:
            break

def add_Re_Activity(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Add a new Recreational activity")
    print("Any other key to go back")
    while(1):
        attributes = {}
        ch = input("Enter choice -> ")
        if (ch == '1'):
            attributes['Hotel_Id'] = input('Enter the hotel id for the hotel in which Recreational activity is to be used: ')
            if len(attributes['Hotel_Id']) == 0 or not attributes['Hotel_Id'].isnumeric():
                print('Error : Please enter hotel id for the hotel of the Recreational activity')
                input('Press any key to continue.')
                return
            attributes['Guest_Id'] = input('Enter the guest who is going to use the activity: ')
            if len(attributes['Guest_Id']) == 0 or not attributes['Guest_Id'].isnumeric():
                print('Error : Please enter guest id for the guest who is going to use the activity')
                input('Press any key to continue.')
                return
            attributes['Activity_Name'] = input('Enter the activity name: ')
            if len(attributes['Activity_Name']) == 0:
                print('Error : Please enter activity name')
                input('Press any key to continue.')
                return
            add = f'INSERT INTO HOTELMANAGEMENT.Recreational_Activity VALUES({attributes["Hotel_Id"]},{attributes["Guest_Id"]},"{attributes["Activity_Name"]}"); '
            try:
                cur.execute(add)
                con.commit()
                print('Recreational Activity details have been successfully added to the database')
                input('Press any key to continue')
            except Exception as exception:
                print('Failed to insert the activity detail into the database.')
                con.rollback()
                print(exception)
                input('Press any key to continue.')
                return 
            # attributes['Price'] = input('Enter the price for Recreational activity: ')
            # if len(attributes['Price']) == 0 or not attributes['Price'].isnumeric():
            #     print('Error : Please enter valid price for the activity')
            #     input('Press any key to continue.')
            #     return
            # add = f'INSERT INTO HOTELMANAGEMENT.Activity_price VALUES({attributes["Hotel_Id"]},"{attributes["Activity_Name"]}",{attributes["Price"]}); '
            # try:
            #     cur.execute(add)
            #     con.commit()
            #     print('Recreational Activity details have been successfully added to the database')
            #     input('Press any key to continue')
            # except Exception as exception:
            #     print('Failed to insert the activity detail into the database.')
            #     con.rollback()
            #     print(exception)
            #     input('Press any key to continue.')
            #     return 
            break
        else:
            break
   
def add_Expenditure(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Add a new Expenditure details")
    print("Any other key to go back")
    while(1):
        attributes = {}
        ch = input("Enter choice -> ")
        if (ch == '1'):
            attributes['Hotel_Id'] = input('Enter the hotel id for the hotel for which Expenditure is to be stored: ')
            if len(attributes['Hotel_Id']) == 0 or not attributes['Hotel_Id'].isnumeric():
                print('Error : Please enter hotel id for the hotel of the Expenditure')
                input('Press any key to continue.')
                return
            attributes['Month'] = input('Enter the month of the Expenditure(MM) is to be stored: ')
            if len(attributes['Month']) == 0 or not attributes['Month'].isnumeric():
                print('Error : Please enter the month of the Expenditure')
                input('Press any key to continue.')
                return
            attributes['Year'] = input('Enter the year of the Expenditure(YYYY) is to be stored: ')
            if len(attributes['Year']) == 0 or not attributes['Year'].isnumeric():
                print('Error : Please enter the year of the Expenditure')
                input('Press any key to continue.')
                return
            attributes['Income'] = input('Enter the income of the hotel: ')
            if len(attributes['Income']) == 0 or not attributes['Income'].isnumeric():
                print('Error : Please enter the income of the hotel')
                input('Press any key to continue.')
                return
            attributes['Staff_Salary'] = input('Enter the salary of the staff members: ')
            if len(attributes['Staff_Salary']) == 0 or not attributes['Staff_Salary'].isnumeric():
                print('Error : Please enter the salary of the staff members')
                input('Press any key to continue.')
                return
            attributes['Extra_Expenses'] = input('Enter the Extra Expenses of the hotel: ')
            if len(attributes['Extra_Expenses']) == 0 or not attributes['Extra_Expenses'].isnumeric():
                print('Error : Please enter the Extra Expenses of the hotel')
                input('Press any key to continue.')
                return
            add = f'INSERT INTO HOTELMANAGEMENT.Expenditure VALUES({attributes["Hotel_Id"]},"{attributes["Month"]}","{attributes["Year"]}",{attributes["Income"]},{attributes["Staff_Salary"]},{attributes["Extra_Expenses"]}); '
            try:
                cur.execute(add)
                con.commit()
                print('Expenditure details have been successfully added to the database')
                input('Press any key to continue')
            except Exception as exception:
                print('Failed to insert a new Expenditure into the database.')
                con.rollback()
                print(exception)
                input('Press any key to continue.')
                return
            # attributes['Total_Profit'] = attributes['Income'] - attributes['Staff_Salary'] - attributes['Extra_Expenses']
            # add = f'INSERT INTO HOTELMANAGEMENT.Ex_Profit VALUES({attributes["Income"]},{attributes["Staff_Salary"]},{attributes["Extra_Expenses"]},{attributes["Total_Profit"]}); '
            # try:
            #     cur.execute(add)
            #     con.commit()
            #     print('Expenditure details have been successfully added to the database')
            #     input('Press any key to continue')
            # except Exception as exception:
            #     print('Failed to insert a new Expenditure into the database.')
            #     con.rollback()
            #     print(exception)
            #     input('Press any key to continue.')
            #     return
            break
        else:
            break

def add_Avail(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. Add a new availed details")
    print("Any other key to go back")
    while(1):
        attributes = {}
        ch = input("Enter choice -> ")
        if (ch == '1'):
            attributes['Guest_Id'] = input('Enter the guest who is going to book the activity : ')
            if len(attributes['Guest_Id']) == 0 or not attributes['Guest_Id'].isnumeric():
                print('Error : Please enter guest id for the guest who is going to book the activity')
                input('Press any key to continue.')
                return
            attributes['Booking_Id'] = input('Enter the booking id for the booking of guest : ')
            if len(attributes['Booking_Id']) == 0 or not attributes['Booking_Id'].isnumeric():
                print('Error : Please enter booking id for the booking of guest ')
                input('Press any key to continue.')
                return
            attributes['Employee_Id'] = input('Enter the Employee Id who is going to manage the activity : ')
            if len(attributes['Employee_Id']) == 0 or not attributes['Employee_Id'].isnumeric():
                print('Error : Please enter the Employee Id who is going to manage the activity')
                input('Press any key to continue.')
                return
            attributes['Activity_Name'] = input('Enter the activity name: ')
            if len(attributes['Activity_Name']) == 0:
                print('Error : Please enter activity name')
                input('Press any key to continue.')
                return
            add = f'INSERT INTO Availed({attributes_keys(attributes)}) VALUES({attributes["Guest_Id"]},{attributes["Booking_Id"]},{attributes["Employee_Id"]},"{attributes["Activity_Name"]}");'
            try:
                cur.execute(add)
                con.commit()
                print('Availed details have been successfully added to the database')
                input('Press any key to continue')
            except Exception as exception:
                print('Failed to insert a new availed information into the database.')
                con.rollback()
                print(exception)
                input('Press any key to continue.')
                return
            break
        else:
            break
