import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'dcrm',
    passwd = 'pass',
    auth_plugin = 'mysql_native_password',

)

#prepare cursor object

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE dcrmdb")

print("CASS")