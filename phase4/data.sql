USE HOTELMANAGEMENT;

LOCK TABLES Hotel WRITE;
INSERT INTO Hotel
VALUES
    (
        '1',
        'River rame',
        '23',
        'Chandni chok',
        'jaipur',
        'rajasthan'
    ),
    (
        '2',
        'Selo hestelo',
        '20',
        'durga nagar',
        'Delhi',
        'Delhi'
    ),
    (   
        '3',
        'hill sky',
        '34',
        'ramp area',
        'abc',
        'xyz'
    ),
    (
        '4',
        'hill view',
        '45',
        'ads dsgf',
        'new',
        'town'
    );
UNLOCK TABLES;

LOCK TABLES Hotel_contact WRITE;
INSERT INTO Hotel_contact
VALUES
    (
        '1',
        '9875746387'
    ),
    (
        '2',
        '8947563846'
    ),
    (
        '2',
        '8947563848'
    ),
    (
        '3',
        '9447563846'
    );
UNLOCK TABLES;


LOCK TABLES Booking WRITE;
INSERT INTO Booking 
VALUES
    (
        '1',
        '2',
        'Confirmed',
        'abcd@gmail.com',
        '89744657392',
        'Cash',
        'E'
    ),
    (
        '2',
        '2',
        'Cancelled',
        'asadf@gmail.com',
        '89744657334',
        'Online',
        'R'
    ),
    (
        '3',
        '1',
        'Confirmed',
        'jdef@gmail.com',
        '89755657392',
        'Cash',
        'R'
    ),
    (
        '4',
        '1',
        'Confirmed',
        'abcfghd@gmail.com',
        '89324657392',
        'Cash',
        'R'
    ),
    (
        '5',
        '3',
        'Confirmed',
        'abcfdgfd@gmail.com',
        '8974557392',
        'Online',
        'E'
    ),
    (
        '6',
        '3',
        'Confirmed',
        'abcfdfdgfd@gmail.com',
        '8974557000',
        'Online',
        'E'
    );
UNLOCK TABLES;


LOCK TABLES Event_Booking WRITE;
INSERT INTO Event_Booking
VALUES
    (
        '1',
        '5',
        '900',
        '54',
        'ankit',
        '2020-12-21 13:00:00',
        '2020-12-22 22:00:00',
        '33'
    ),
    (
        '5',
        '4',
        '900',
        '50',
        'avil',
        '2020-12-20 13:00:00',
        '2020-12-22 13:00:00',
        '48'
    ),
     (
        '6',
        '6',
        '900',
        '60',
        'romil',
        '2020-11-20 13:00:00',
        '2020-11-22 13:00:00',
        '48'
    );
UNLOCK TABLES;

LOCK TABLES Room_Booking WRITE;
INSERT INTO Room_Booking
VALUES
    (
        '2',
        '5',
        '3',
        '6000',
        '2020-12-14',
        '2020-12-15'
    ),
    (
        '3',
        '4',
        '3',
        '6000',
        '2020-10-19',
        '2020-10-20'
    ),
    (
        '4',
        '7',
        '5',
        '6000',
        '2020-10-14',
        '2020-12-15'
    );
UNLOCK TABLES;

LOCK TABLES B_Final_Charge WRITE;
INSERT INTO B_Final_Charge
VALUES
    (
        '900',
        '2020-12-21',
        '2020-12-22',
        '33',
        '3',
        '6000',
        '2020-12-14',
        '2020-12-15',
        '35700'
    );
UNLOCK TABLES;


LOCK TABLES Guest WRITE;
INSERT INTO Guest
VALUES
    (
        '1',
        '2',
        '34',
        'ahaan',
        'singhal',
        'Male'
    ),
    (
        '2',
        '1',
        '24',
        'Mia',
        'Singh',
        'Female'
    ),
    (
        '3',
        '3',
        '28',
        'sami',
        'ron',
        'Female'
    ),
    (
        '4',
        '1',
        '34',
        'nani',
        'mani',
        'Female'
    ),
    (
        '5',
        '2',
        '28',
        'Miashi',
        'Singhvi',
        'Female'
    ),
    (
        '6',
        '3',
        '19',
        'adsi',
        'dgf',
        'Female'
    );
UNLOCK TABLES;

LOCK TABLES Expenditure WRITE;
INSERT INTO Expenditure
VALUES
    (
        '1',
        '05',
        '2021',
        '250000',
        '50000',
        '10000'
    ),
     (
        '1',
        '06',
        '2021',
        '250000',
        '50000',
        '10000'
    ),
     (
        '2',
        '05',
        '2021',
        '250000',
        '50000',
        '10000'
    );
UNLOCK TABLES;

LOCK TABLES Ex_Profit WRITE;
INSERT INTO Ex_Profit
VALUES
    (
        '250000',
        '50000',
        '10000',
        '190000'
    );
UNLOCK TABLES;

LOCK TABLES Recreational_Activity WRITE;
INSERT INTO Recreational_Activity
VALUES
    (
        '2',
        '1',
        'Deep Tissue Massage'
    ),
    (
        '2',
        '2',
        'Disco'
    ),
    (
        '1',
        '3',
        'dgf'
    ),
    (
        '3',
        '4',
        'fgd'
    ),
    (
        '3',
        '5',
        'Disco'
    );
UNLOCK TABLES;

LOCK TABLES Activity_price WRITE;
INSERT INTO Activity_price
VALUES
    (
        '1',
        'Zumba',
        '2000'
    ),
    (
        '2',
        'Disco',
        '10000'
    ),
    (
        '2',
        'Deep Tissue Massage',
        '5000'
    );
UNLOCK TABLES;


LOCK TABLES Staff WRITE;
INSERT INTO Staff
VALUES
    (
        '1',
        '2',
        '1',
        'Ramesh',
        'jain',
        '1991-08-21',
        '8475937465',
        'Cook'
    ),
    (
        '2',
        '2',
        '1',
        'Ram',
        'saini',
        '1991-04-11',
        '8475937466',
        'Manager'
    ),
    (
        '3',
        '3',
        '2',
        'Aami',
        'Sethi',
        '1999-03-01',
        '8475937467',
        'Room service'
    ),
    (
        '4',
        '3',
        '2',
        'Aamret',
        'Sare',
        '1995-05-05',
        '8475937468',
        'Room service'
    ),
    (
        '5',
        '3',
        '3',
        'tipu',
        'sam',
        '1994-04-05',
        '8475567468',
        'Security guard'
    );
UNLOCK TABLES;

LOCK TABLES Staff_address WRITE;
INSERT INTO Staff_address
VALUES
    (
        '1',
        '74 abc xyz, near 123'
    ),
    (
        '2',
        '12 asd asd, near asd'
    ),
    (
        '3',
        '32 asd era, near gfs'
    ),
    (
        '4',
        '43 dsg hdd, near gds'
    );
UNLOCK TABLES;

LOCK TABLES Staff_Salary WRITE;
INSERT INTO Staff_Salary
VALUES
    (
        '1',
        'Manager',
        '40000'
    ),
    (
        '1',
        'Cook',
        '50000'
    ),
    (
        '2',
        'Room service',
        '30000'
    ),
    (
        '2',
        'Receptionist',
        '35000'
    );
UNLOCK TABLES;

LOCK TABLES Availed WRITE;
INSERT INTO Availed
VALUES
    (
        '1',
        '1',
        '1',
        'Deep Tissue Massage'
    );
UNLOCK TABLES;
