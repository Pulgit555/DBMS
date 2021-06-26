import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import datetime


def exe_query(query, con, cur):
    try:
        cur.execute(query)
        con.commit()
        print("Updated details")
    except Exception as e:
        print("Error!")
        con.rollback()
        print("Failed to update from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to go to main menu")



def update_Hotel(cur,con):
    attr={}
    h_id=int(input("Enter hotel id -> "))
    hotel_atr = ["Hotel_Name","Number_of_Room_available","Area","City","Contact Number"]
    print("Enter the number beside the attribute you want to update")
    i = 0
    while i < len(hotel_atr):
        i += 1
        print(str(i) + ". " + hotel_atr[i-1])
    print(" ")
    
    ch = input("Enter choice -> ")

    if(ch=='1'):
        name = input('New Hotel Name: ')
        if len(name) > 0:
            attr['name'] = name
        else :
            print("Input can not be empty")
            return
        query = "UPDATE Hotel set Hotel_Name = '%s' where Hotel_Id = %d;" % (
            attr["name"], h_id)

    elif(ch=='2'):
        name = input('Room Available: ')
        if len(name) != 0 and name.isnumeric():
            query = "UPDATE Hotel set Number_of_Room_available = '%s' where Hotel_Id = %d;" % (name, h_id)
        else :
            print("Install can not be empty")
            return
        
    elif (ch=='3'):
        name = input('New Area: ')
        if len(name) > 0:
            attr['name'] = name
        else :
            print("Input can not be empty")
            return      
        query = "UPDATE Hotel set Area = '%s' where Hotel_Id = %d;" % (attr["name"], h_id)
      
    elif (ch=='4'):
        name = input('New City: ')
        if len(name) > 0:
            attr['name'] = name
        else :
            print("Input can not be empty")
            return
        query = "UPDATE Hotel set City = '%s' where Hotel_Id = %d;" % (attr["name"], h_id)
     
    elif (ch=='5'):
        num = input('New number: ')
        nom = input('Old number: ')
        if(len(num)==10 and len(nom)==10 and num.isnumeric() and nom.isnumeric() ):
            query = "UPDATE Hotel_contact SET Contact_Number = '%s' WHERE Hotel_Id = %d AND Contact_Number = '%s';" %(num,h_id,nom)
        else:
            print("Input can not be empty")
            return
    
    else : 
        return
    try:
        cur.execute(query)
        con.commit()
        print("Updated details")
        input('Press any key to continue. ')
    except Exception as e:
        print("Failed to update")
        con.rollback()
        print(e)
        input('Press any key to continue. ')
        return


# def update_Booking(cur,con):
#     attr={}
#     h_id=input("Enter Booking id -> ")
#     hotel_atr = ["Hotel Id","Contact_Number","Payment_Mode","Booking_Type"]
#     print("Enter the number beside the attribute you want to update")
#     i = 0
#     while i < len(hotel_atr):
#         i += 1
#         print(str(i) + ". " + hotel_atr[i-1])
#     ch = int(input("Enter choice> "))
# def update_Guest():
  


def update_Staff(cur,con):
    attr={}
    h_id=input("Enter Staff id -> ")
    if(len(h_id)!=0):
        hotel_atr = ["Supervisor Id","Contact","Job Type","Address","Salary"]
        print("Enter the number beside the attribute you want to update")
        i = 0
        while i < len(hotel_atr):
            i += 1
            print(str(i) + ". " + hotel_atr[i-1])
        ch = input("Enter choice -> ")

        if(ch=='1'):
            name = input('New Supervisor Id: ')
            if len(name) > 0 and name.isnumeric():
                query = "UPDATE Staff set Supervisor_Id="+name+" where Employee_Id = "+h_id+";" 
            else :
                print("Input can not be empty")
                return

        elif(ch=='2'):
            name = input('New contact number: ')
            if (len(name)==10 and name.isnumeric()): 
                query = "UPDATE Staff set Contact_Number = '"+name+"' where Employee_Id = "+h_id+";"
            else :
                print("Input can not be empty")
                return


        elif(ch=='3'):
            name = input('New Job type: ')
            if len(name) > 0:
                query = "UPDATE Staff set Job_Type = '"+name+"' where Employee_Id ="+h_id+";" 
            else :
                print("Input can not be empty")
                return

        elif(ch=='4'):
            num = input('Amount of New address: ')
            nom = input('Amount of Old address: ')
            if (len(num)>0 and len(nom)>0) :
                query = "UPDATE Staff_address SET Address = '"+num+"' WHERE Employee_Id = "+h_id+" AND Address = '"+nom+"';"
            
        else:
            return

        try:
            cur.execute(query)
            con.commit()
            print("Updated details")
            input('Press any key to continue. ')

        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    else:
        return


def update_sal(cur,con):
    h_id = input('Enter Hotel id : ')
    job = input('Enter Job Type : ')
    name = input('New salary: ')
    if (len(h_id)>0 and len(job)>0 and len(name) > 0 and name.isnumeric()):
        query = "UPDATE Staff_Salary set Salary = "+name+" where Hotel_Id = "+h_id+" AND Job_Type = '"+job+"';"
    else :
        print("Input can not be empty or not of correct datatype")
        return
    try:
        cur.execute(query)
        con.commit()
        print("Updated details")
        input('Press any key to continue. ')

    except Exception as e:
        print("Failed to update")
        con.rollback()
        print(e)
        input('Press any key to continue. ')
        return

def update_Re_Activity(cur,con):
    h_id=input("Enter Hotel id -> ")
    a_id=input("Enter Activity name -> ")
    nae = input('New price of activity: ')
    if (len(nae) != 0  and len(h_id)!=0 and len(a_id)!=0 and nae.isnumeric() and h_id.isnumeric()) :
        query = "UPDATE Activity_price set Price="+nae+" where Hotel_Id="+h_id+" AND Activity_Name ='"+a_id+"';" 
    else :
        print("Input can not be empty or not of correct datatype")
        return
 
  
    try:
        cur.execute(query)
        con.commit()
        print("Updated details")
        input('Press any key to continue. ')

    except Exception as e:
        print("Failed to update")
        con.rollback()
        print(e)
        input('Press any key to continue. ')
        return


# def update_Expenditure():
#     while(1):
#         break


# def update_Availed():
#     while(1):
#         break


# def update_Charges():
#     while(1):
#         break

