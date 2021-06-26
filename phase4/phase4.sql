-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: Company
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DEPARTMENT`
--

DROP DATABASE IF EXISTS HOTELMANAGEMENT;
CREATE SCHEMA HOTELMANAGEMENT;
USE HOTELMANAGEMENT;

DROP TABLE IF EXISTS Hotel;
CREATE TABLE Hotel (
    Hotel_Id int NOT NULL,
    Hotel_Name varchar(50) NOT NULL,
    Number_of_Room_available int NOT NULL,
    Area varchar(50) NOT NULL,
    City varchar(50) NOT NULL,
    State varchar(50) NOT NULL,
    PRIMARY KEY (Hotel_Id)
)   ENGINE = InnoDB DEFAULT CHARSET = utf8;


DROP DATABASE IF EXISTS Hotel_contact;
CREATE TABLE Hotel_contact (
    Hotel_Id int NOT NULL,
    Contact_Number varchar(20) NOT NULL,
    PRIMARY KEY (Hotel_Id, Contact_Number),
    CONSTRAINT Hotel_contact_ibfk_1 FOREIGN KEY (Hotel_Id) REFERENCES Hotel (Hotel_Id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


DROP DATABASE IF EXISTS Booking;
CREATE TABLE Booking (
    Booking_Id int NOT NULL,
    Hotel_Id int NOT NULL,
    Status varchar(50) NOT NULL,
    Email varchar(50) NOT NULL, 
    Contact_Number varchar(20) NOT NULL,
    Payment_Mode varchar(50) NOT NULL,
    Booking_Type varchar(50) NOT NULL,
    PRIMARY KEY (Booking_Id,Hotel_Id),
    CONSTRAINT Booking_ibfk_1 FOREIGN KEY (Hotel_Id) REFERENCES Hotel (Hotel_Id)
    ON UPDATE CASCADE
    ON DELETE CASCADE

) ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP DATABASE IF EXISTS Event_Booking;
CREATE TABLE Event_Booking (
    Booking_Id int NOT NULL,
    Hall_Number varchar(50) NOT NULL,
    Hall_Charges float NOT NULL,
    Number_of_Guest int NOT NULL,
    Organised_By varchar(50) NOT NULL,
    Event_Starts_On date NOT NULL,
    Event_Till date NOT NULL,
    Duration float NOT NULL,
    PRIMARY KEY (Booking_Id),
    CONSTRAINT Event_Booking_ibfk_1 FOREIGN KEY (Booking_Id) REFERENCES Booking (Booking_Id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP DATABASE IF EXISTS Room_Booking;
CREATE TABLE Room_Booking (
    Booking_Id int NOT NULL,
    Number_of_Members int NOT NULL,
    Number_of_Rooms int NOT NULL,
    Room_Charges float NOT NULL,
    Check_in date NOT NULL,
    Check_out date NOT NULL,
    PRIMARY KEY (Booking_Id),
    CONSTRAINT Room_Booking_ibfk_1 FOREIGN KEY (Booking_Id) REFERENCES Booking (Booking_Id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


DROP DATABASE IF EXISTS B_Final_Charge;
CREATE TABLE B_Final_Charge (
    Hall_Charges float NOT NULL,
    Event_Starts_On date NOT NULL,
    Event_Till date NOT NULL,
    Duration float NOT NULL,
    Number_of_Rooms int NOT NULL,
    Room_Charges float NOT NULL,
    Check_in date NOT NULL,
    Check_out date NOT NULL,
    Final_charges float NOT NULL,
    PRIMARY KEY (Hall_Charges,Event_Starts_On, Duration , Number_of_Rooms, Room_Charges,Check_out,Check_in)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


DROP DATABASE IF EXISTS Guest ;
CREATE TABLE Guest (
    Guest_Id int NOT NULL,
    Booking_Id int NOT NULL,
    Age int NOT NULL,
    First_Name varchar(50) NOT NULL, 
    Last_Name varchar(50) NOT NULL,
    Gender varchar(50) NOT NULL,
    PRIMARY KEY (Guest_Id,Booking_Id),
    CONSTRAINT Guest_ibfk_1 FOREIGN KEY (Booking_Id) REFERENCES Booking (Booking_Id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP DATABASE IF EXISTS Expenditure ;
CREATE TABLE Expenditure (
    Hotel_Id int  NOT NULL,
    Month int NOT NULL,
    Year int NOT NULL,
    Income float NOT NULL,
    Staff_Salary float NOT NULL,
    Extra_Expenses float NOT NULL,
    PRIMARY KEY(Hotel_Id,Month,Year)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;



DROP DATABASE IF EXISTS Ex_Profit ;
CREATE TABLE Ex_Profit(
    Income float NOT NULL,
    Staff_Salary float NOT NULL, 
    Extra_Expenses float NOT NULL,
    Total_Profit float NOT NULL,
    PRIMARY KEY(Income, Staff_Salary , Extra_Expenses)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;



DROP DATABASE IF EXISTS Recreational_Activity ;
CREATE TABLE Recreational_Activity (
    Hotel_Id int NOT NULL,
    Guest_Id int NOT NULL, 
    Activity_Name varchar(50) NOT NULL,
    PRIMARY KEY(Hotel_Id, Activity_Name , Guest_Id),
    CONSTRAINT Recreational_Activity_ibfk_1 FOREIGN KEY (Hotel_Id) REFERENCES Hotel (Hotel_Id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
    CONSTRAINT Recreational_Activity_ibfk_2 FOREIGN KEY (Guest_Id) REFERENCES Guest (Guest_Id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8;



DROP DATABASE IF EXISTS Activity_price ;
CREATE TABLE Activity_price(
    Hotel_Id int NOT NULL,
    Activity_Name varchar(50) NOT NULL,
    Price float NOT NULL,
    PRIMARY KEY(Hotel_Id, Activity_Name),
    CONSTRAINT Activity_price_ibfk_1 FOREIGN KEY (Hotel_Id) REFERENCES Hotel (Hotel_Id) 
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


DROP DATABASE IF EXISTS Staff ;
CREATE TABLE Staff(
    Employee_Id int NOT NULL,
    Supervisor_Id int NOT NULL,
    Hotel_Id int NOT NULL,
    First_Name varchar(50) NOT NULL,
    Last_Name varchar(50) NOT NULL,
    Date_of_Birth date NOT NULL,
    Contact_Number varchar(20) NOT NULL,
    Job_Type varchar(50) NOT NULL,
    PRIMARY KEY(Employee_Id,Hotel_Id , Supervisor_Id),
    CONSTRAINT Staff_ibfk_1 FOREIGN KEY (Hotel_Id) REFERENCES Hotel (Hotel_Id) 
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


DROP DATABASE IF EXISTS Staff_address ;
CREATE TABLE Staff_address(
    Employee_Id int NOT NULL,
    Address varchar(50) NOT NULL,
    PRIMARY KEY(Employee_Id),
    CONSTRAINT Staff_address_ibfk_1 FOREIGN KEY (Employee_Id) REFERENCES Staff (Employee_Id)
    ON UPDATE CASCADE
    ON DELETE CASCADE 
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


DROP DATABASE IF EXISTS Staff_Salary ;
CREATE TABLE Staff_Salary(
    Hotel_Id int NOT NULL,
    Job_Type varchar(50) NOT NULL, 
    Salary float NOT NULL,
    PRIMARY KEY(Hotel_Id, Job_Type),
    CONSTRAINT Staff_Salary_ibfk_1 FOREIGN KEY (Hotel_Id) REFERENCES Hotel (Hotel_Id) 
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;



DROP DATABASE IF EXISTS Availed  ;
CREATE TABLE Availed (
    Guest_Id int NOT NULL, 
    Booking_Id int NOT NULL,
    Employee_Id int NOT NULL,
    Activity_Name varchar(50) NOT NULL,
    PRIMARY KEY(Guest_Id, Booking_Id , Employee_Id , Activity_Name),
    CONSTRAINT Availed_ibfk_1 FOREIGN KEY (Guest_Id) REFERENCES Guest (Guest_Id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT Availed_ibfk_2 FOREIGN KEY (Booking_Id) REFERENCES Booking (Booking_Id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT Availed_ibfk_3 FOREIGN KEY (Employee_Id) REFERENCES Staff (Employee_Id)
    ON UPDATE RESTRICT
    ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
