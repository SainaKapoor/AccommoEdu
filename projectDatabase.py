#using mysql.connector to connect with the sql database
import mysql.connector

mydb = mysql.connector.connect(
    host = "sql5.freemysqlhosting.net",
    user = "sql5667537",
    database = "sql5667537",
    passwd = "npSWwqzMhz"
)

print(mydb)
#cursor will allow to function the mysqloperation using the database connection
#cursor will allow to function the mysqloperation using the database connection
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS students")
sql = "CREATE TABLE students (student_ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), accomodation VARCHAR(255), start_date DATE, end_date DATE, comments VARCHAR(255))"
mycursor.execute(sql)
mydb.commit()