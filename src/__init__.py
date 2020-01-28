import tbapy #gives access to TBA API
import mysql.connector #gives access to mySQL
#import pymysql

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")