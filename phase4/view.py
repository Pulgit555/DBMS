import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate

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
        print("Failed to extract from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")

 
def view_Hotel(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. View all Hotel")
    print("2. View contact of Hotel by name")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if (ch == '1'):
            query = "SELECT Hotel_Id,Hotel_Name,Number_of_Room_available,Area,City,State FROM Hotel;"
            print_query(query,con,cur)
        elif (ch == '2'):
            h_name = input("Hotel name: ")
            query = "SELECT Hotel.Hotel_Id,Hotel_Name,Contact_Number FROM Hotel,Hotel_contact WHERE Hotel.Hotel_Id=Hotel_contact.Hotel_Id AND Hotel_Name = '" + h_name +"';"
            print_query(query, con, cur)
        
        else:
            break

def view_Booking(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. View all Bookings")
    print("2. View all Booking in a hotel by hotel id")
    print("3. View Booking by id")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if (ch == '1'):
            query = "SELECT * FROM Booking;"
            print_query(query, con, cur)
            
        elif (ch == '2'):
            h_id = input("Hotel Id : ")
            query = "SELECT * FROM Booking WHERE Hotel_Id = " + h_id +";"
            print_query(query, con, cur)
            
        elif (ch == '3'):
            b_id = input("Booking Id: ")
            query = "SELECT * FROM Booking WHERE Booking_Id = " + b_id +";"
            try:
                cur.execute(query)
                con.commit()
                result = cur.fetchall()
                tfilter=result[0]["Booking_Type"]

                if len(tfilter) != 0:
                    if(tfilter=='R'):
                        query = "SELECT Booking.Booking_Id,Hotel_Id,Status,Email,Contact_Number,Payment_Mode,Booking_Type,Number_of_Members,Number_of_Rooms,Room_Charges,Check_in,Check_out FROM Booking,Room_Booking WHERE Booking.Booking_Id=Room_Booking.Booking_Id  AND Booking.Booking_Id = " + b_id +";"
                        print_query(query, con, cur)
                    elif (tfilter=='E'):
                        query = "SELECT Booking.Booking_Id,Hotel_Id,Status,Email,Contact_Number,Payment_Mode,Booking_Type,Hall_Number,Hall_Charges,Number_of_Guest, Organised_By,Event_Starts_On,Event_Till,Duration FROM Booking,Event_Booking WHERE Booking.Booking_Id=Event_Booking.Booking_Id  AND Booking.Booking_Id = " + b_id +";"
                        print_query(query, con, cur)
                    else :
                        print("Error!")

                else:
                    print("Error!")
            except Exception as e:
                print("Error!")
                con.rollback()
                print("Failed to delete from database")
                print(">>>>>>>>>>>>>", e)
                input("Press any key to go to main menu")
            
        else:
            break

def view_Guest(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. View all Guest")
    print("2. View all Guest with a bokking id")
    print("3. Guest by name")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if (ch == '1'):
            query = "SELECT * FROM Guest;"
            print_query(query, con, cur)
            
        elif (ch == '2'):
            s_id = input("Guest's Booking Id : ")
            query = "SELECT * FROM Guest WHERE Booking_Id = " + s_id +";"
            print_query(query, con, cur)
            
        elif (ch == '3'):
            f_id = input("Guest's First name : ")
            l_id = input("Guest's Last name : ")
            query = "SELECT * FROM Guest WHERE First_name = '" + f_id +  "' AND Last_name = '" + l_id +"' ;"
            print_query(query, con, cur)
            
        else:
            break

def view_Staff(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. View all Staff")
    print("2. View all Staff in a hotel by hotel_id")
    print("3. View Staff by id")
    print("4. View Staff by name")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if (ch == '1'):
            query = "SELECT * FROM Staff;"
            print_query(query, con, cur)
            
        elif (ch == '2'):
            h_id = input("Hotel Id : ")
            query = "SELECT Staff.Employee_Id,Staff.Hotel_Id,Supervisor_Id,First_Name,Last_Name,Date_of_Birth,Contact_Number,Staff.Job_Type,Address,Salary FROM Staff,Staff_address,Staff_Salary WHERE Staff.Employee_Id=Staff_address.Employee_Id AND Staff.Job_Type=Staff_Salary.Job_Type AND Staff.Hotel_Id="+h_id+";"
            print_query(query, con, cur)
           
        elif (ch == '3'):
            s_id = input("Staff's Id : ")
            query = "SELECT Staff.Employee_Id,Staff.Hotel_Id,Supervisor_Id,First_Name,Last_Name,Date_of_Birth,Contact_Number,Staff.Job_Type,Address,Salary FROM Staff,Staff_address,Staff_Salary WHERE Staff.Employee_Id=Staff_address.Employee_Id AND Staff.Job_Type=Staff_Salary.Job_Type AND Staff.Employee_Id = " + s_id +";"
            print_query(query, con, cur)
            
        elif (ch == '4'):
            f_id = input("Staff's First name : ")
            l_id = input("Staff's Last name : ")
            query = "SELECT Staff.Employee_Id,Staff.Hotel_Id,Supervisor_Id,First_Name,Last_Name,Date_of_Birth,Contact_Number,Staff.Job_Type,Address,Salary FROM Staff,Staff_address,Staff_Salary WHERE Staff.Employee_Id=Staff_address.Employee_Id AND Staff.Job_Type=Staff_Salary.Job_Type AND Staff.First_name = '" + f_id + "' AND Staff.Last_name = '" + l_id +"' ;"
            print_query(query, con, cur)
           
        else:
            break

def view_Expenditure(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. View all expenditure")
    print("2. View expenditure for all hotel by month")
    print("3. View all expenditure for a hotel by its id")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if (ch == '1'):
            query = "SELECT * FROM Expenditure ;"
            print_query(query, con, cur)
        elif (ch == '2'):
            m = input("Enter month (MM) -> ")
            y = input("Enter month (YYYY) -> ")
            query = "SELECT * FROM Expenditure WHERE Month = "+m+" AND Year = "+y+";"
            print_query(query, con, cur)

        elif (ch == '3'):
            h_id = input("Hotel id: ")
            query = "SELECT * FROM Expenditure WHERE Hotel_Id = " + h_id +";"
            print_query(query, con, cur)
        else:
            break

def view_Re_Activity(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. View all Activities")
    print("2. View Activities by name")
    print("3. View Activities in hotel having hotel id")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if (ch == '1'):
            query = "SELECT * FROM Recreational_Activity;"
            # query = "SELECT Recreational_Activity.Hotel_Id, Recreational_Activity.Guest_Id,Recreational_Activity.Activity_Name,Price FROM Recreational_Activity,Activity_price WHERE Recreational_Activity.Hotel_Id=Activity_price.Hotel_Id AND Recreational_Activity.Activity_Name=Activity_price.Activity_Name;"
            print_query(query, con, cur)
        elif (ch == '2'):
            h_id = input("Activity name: ")
            # query = "SELECT Recreational_Activity.Hotel_Id, Recreational_Activity.Guest_Id,Recreational_Activity.Activity_Name,Price FROM Recreational_Activity,Activity_price WHERE Recreational_Activity.Hotel_Id=Activity_price.Hotel_Id AND Recreational_Activity.Activity_Name=Activity_price.Activity_Name AND Activity_price.Activity_name = '" + h_id +"' ;"
            query = "SELECT * FROM Recreational_Activity WHERE Activity_name = '" + h_id +"' ;"
            print_query(query, con, cur)
        elif (ch == '3'):
            h_id = input("Hotel id: ")
            # query = "SELECT Recreational_Activity.Hotel_Id, Recreational_Activity.Guest_Id,Recreational_Activity.Activity_Name,Price FROM Recreational_Activity,Activity_price WHERE Recreational_Activity.Hotel_Id=Activity_price.Hotel_Id AND Recreational_Activity.Activity_Name=Activity_price.Activity_Name AND Recreational_Activity.Hotel_Id = " + h_id +";"
            query = "SELECT * FROM Recreational_Activity WHERE Hotel_Id = '" + h_id +"' ;"
            print_query(query, con, cur)
        else:
            break

     

def view_Availed(cur,con):
    tmp = sp.call('clear', shell=True)
    print("1. View all Availed relarions")
    print("2. View Activities availed by Booking id")
    print("Any other key to go back")
    while(1):
        ch = input("Enter choice -> ")
        if (ch == '1'):
            query = "SELECT * FROM Availed;"
            print_query(query, con, cur)
        elif (ch == '2'):
            h_id = input("Booking Id : ")
            query = "SELECT * FROM Availed WHERE Booking_Id = " + h_id +";"
            print_query(query, con, cur)
        else:
            break