DROP DATABASE clubdbms;  

CREATE DATABASE clubdbms;  

\c clubdbms 




CREATE TABLE Faculty ( 

FacultyName Name NOT NULL, 

FacultyID INT, 

FacultyMailID VARCHAR (30), 

FacultyType VARCHAR (30), 

PRIMARY KEY (FacultyID) 

);  




CREATE TABLE Student ( 

StudentName Name NOT NULL, 

StudentGPA DECIMAL NOT NULL,

Semester INT NOT NULL, 

StudentSRN VARCHAR (20), 

StudentDepartment VARCHAR (20) NOT NULL, 

StudentMailID VARCHAR (30) NOT NULL, 

MobileNumber CHAR (10), 

isExternal INT CHECK (isExternal BETWEEN 0 AND 1) DEFAULT 0, 

PRIMARY KEY (StudentSRN) 

);  
  



CREATE TABLE Club (   

ClubID INT, 

ClubName VARCHAR (30) NOT NULL, 

ClubType VARCHAR (20) NOT NULL, 

ClubLocation VARCHAR (50),   

ClubDepartment VARCHAR (20), 

ClubHeadSRN VARCHAR (20) UNIQUE NOT NULL, 

ClubHeadFID INT, 

PRIMARY KEY (ClubID),

FOREIGN KEY (ClubHeadFID) REFERENCES Faculty (FacultyID),

FOREIGN KEY (ClubHeadSRN) REFERENCES Student (StudentSRN)

);  

  


CREATE TYPE Name AS (     

Firstname VARCHAR (30),   

Midname VARCHAR (30),   

Lastname VARCHAR (30) 

);  


  

CREATE TABLE Faculty_Department ( 

FacultyDepartment VARCHAR (20), 

FacultyID INT, 

PRIMARY KEY (FacultyDepartment, FacultyID), 

FOREIGN KEY (FacultyID) REFERENCES Faculty (FacultyID));   



   

CREATE TABLE Event ( 

EventBudget DECIMAL NOT NULL, 

EventDescription VARCHAR, 

EventLocation VARCHAR (50), 

EventDate DATE NOT NULL, 

EventID INT, 

ParticipantNo INT CHECK (ParticipantNo > 5) NOT NULL, 

EventName VARCHAR (30) NOT NULL, 

PRIMARY KEY (EventID) 

);  

  


CREATE TABLE Sponsor ( 

SponsorName VARCHAR (30) NOT NULL, 

SponsorID INT, 

SponsorType VARCHAR (30), 

PRIMARY KEY (SponsorID) 

); 


  

CREATE TABLE member_of( 

ClubID INT, 

FacultyID INT, 

PRIMARY KEY (ClubID, FacultyID), 

FOREIGN KEY (ClubID) REFERENCES Club (ClubID), 

FOREIGN KEY (FacultyID) REFERENCES Faculty (FacultyID) 

);  




CREATE TABLE part_of ( 

StudentSRN VARCHAR (20), 

ClubID INT,

StudentGPA DECIMAL CHECK (StudentGPA > 6),

PRIMARY KEY (StudentSRN, ClubID), 

FOREIGN KEY (StudentSRN) REFERENCES Student (StudentSRN), 

FOREIGN KEY (ClubID) REFERENCES Club (ClubID)

); 





CREATE TABLE sponsors_event ( 

Amount DECIMAL NOT NULL, 

SponsorID INT, 

EventID INT, 

PRIMARY KEY (SponsorID, EventID), 

FOREIGN KEY (SponsorID) REFERENCES Sponsor (SponsorID), 

FOREIGN KEY (EventID) REFERENCES Event (EventID) 

); 


  

CREATE TABLE sponsors_club ( 

StartDate DATE NOT NULL, 

EndDate DATE NOT NULL, 

Amount DECIMAL NOT NULL, 

Requirement DECIMAL, 

SponsorID INT, 

ClubID INT, 

PRIMARY KEY (SponsorID, ClubID), 

FOREIGN KEY (SponsorID) REFERENCES Sponsor (SponsorID), 

FOREIGN KEY (ClubID) REFERENCES Club (ClubID) 

); 

  

CREATE TABLE conducts ( 

EventID INT, 

ClubID INT, 

PRIMARY KEY (EventID, ClubID), 

FOREIGN KEY (EventID) REFERENCES Event (EventID), 

FOREIGN KEY (ClubID) REFERENCES Club (ClubID) 

); 




CREATE TABLE participates_in ( 

StudentSRN VARCHAR (20) NOT NULL, 

EventID INT NOT NULL, 

PRIMARY KEY (StudentSRN, EventID), 

FOREIGN KEY (StudentSRN) REFERENCES Student (StudentSRN), 

FOREIGN KEY (EventID) REFERENCES Event (EventID) 

); 