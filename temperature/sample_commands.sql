-- These are various SQL commands I used when toying with the project.
-- They are intended for Microsoft SQL Server and won't neccesarily work with MySQL.
-- In SQL Server Management Studio, you can select (highlight) a command 
-- and run just that command rather than the whole script, so you can select
-- from below and run as needed.

-- Create the database (this should happen first)
CREATE DATABASE temperature;

-- Make sure we're in the right schema
use temperature;

-- Create the table (if it doesn't exist already or if you just dropped it...)
CREATE TABLE temps(recordID INT IDENTITY(1,1), temptime DATETIME, temp_c DECIMAL(6,3));

-- Get the number of records in the table:
select count(*) as '# of Records' from temps;

-- Return every record in the table
select * from temps;

-- Delete the entire table (this includes ALL of the data...)
DROP TABLE temps;


-- Empty the table without deleting the table itself (deletes all records)
DELETE FROM temps;

-- Show information about the structure of the table
sp_help temps;

-- Return a list of times and temperatures without showing recordID
SELECT temptime 'TIMESTAMP', temp_c 'CELSIUS' FROM temps ORDER BY temptime;

-- Return the average temperature of all records
SELECT AVG(temp_c) FROM temps;

-- Return the maximum temperature of all records
SELECT MAX(temp_c) FROM temps;

-- Return the minimum temperature of all records
SELECT MIN(temp_c) FROM temps;

-- Return the maximum, minimum, and average temperature from the table
SELECT AVG(temp_c) 'Average', MAX(temp_c) 'Maximum', MIN(temp_c) 'Minimum' FROM temps;