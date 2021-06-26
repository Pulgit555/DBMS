import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate

def delete_Hotel(cur,con):
    try:
        h_id = int(input("Enter Hotel id :"))
        query = "delete from Hotel where Hotel_Id = %s ;" % (h_id)
        cur.execute(query)
        con.commit()
        print("Deleted Hotel")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")
    return


def delete_Booking(cur,con):
    try:
        id1 = int(input("Enter Booking id: "))
        # id2 = int(input("Enter Hotel id: "))
        query = "delete from Booking where Booking_Id='%s';" % (
            id1)
        cur.execute(query)
        con.commit()
        print("Deleted Booking")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")
    return

def delete_Staff(cur,con):
        try:
            id1 = int(input("Enter Employee id: "))
            # id3 = int(input("Enter Supervisor id: "))
            query = "select * from Staff where Supervisor_Id=%d ;" % (id1)
            cur.execute(query)
            con.commit()
            result = cur.fetchall()
            if len(result)!=0 :
                print("Can't delete a supervisor")
                input("Press any key to continue")

            else :
                query = "delete from Staff where Employee_Id=%d ;" % (id1)
                cur.execute(query)
                con.commit()
                print("Deleted Staff")
                input("Press any key to continue")
        except Exception as e:
            con.rollback()
            print("Failed to delete from database")
            print(">>>>>>>>>>>>>", e)
            input("Press any key to continue")
    


def delete_Re_Activity(cur,con):
    try:
        id1 = int(input("Enter Hotel id: "))
        id2 = input("Enter Activity name: ")
        id3 = int(input("Enter Guest id: "))
        query = "delete from Recreational_Activity where Hotel_Id=%d AND  Activity_Name='%s' AND Guest_Id=%d ;" % (id1, id2, id3)
        cur.execute(query)
        con.commit()
        print("Deleted Recreational Activity")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")
    return

def delete_Expenditure(cur,con):
    try:
        id1 = int(input("Enter Hotel id: "))
        id2 = int(input("Enter Month: "))
        id3 = int(input("Enter Year: "))
        query = "delete from Expenditure where Hotel_Id=%d AND  Month=%d AND Year=%d ;" % (id1, id2, id3)
        cur.execute(query)
        con.commit()
        print("Deleted Expenditure")
        input("Press any key to continue")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")
    return
