#Create the Student table
CREATE TABLE Student (
    ID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(20) NOT NULL,
    Age INT NOT NULL,
    Address VARCHAR(25)
);

#Insert 5 records into the Student table
INSERT INTO Student (ID, Name, Age, Address)
VALUES
    (1, 'karthik', 25, 'nagra'),
    (2, 'raj', 27, 'chennai'),
    (3, 'shivae', 89, 'madurai'),
    (4, 'sai', 31, 'kovai'),
    (5, 'rai', 24, 'trichy');