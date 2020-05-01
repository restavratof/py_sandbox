import mysql.connector
from mysql.connector import errorcode


dbhost = '0.0.0.0'
dbport = '3306'
dbuser = 'mysql1'
dbpass = 'test1'
dbname = 'gcpcostdb'

from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(host=dbhost, port=dbport, user=dbuser, password=dbpass, database=dbname,
                                auth_plugin='mysql_native_password')
  try:
      cursor = cnx.cursor()
      cursor.execute('SHOW TABLES;')
      result = cursor.fetchall()
      print(f'RESULT: {result}')
  except mysql.connector.Error as err:
      if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
          print("already exists.")
      else:
          print(err.msg)
  else:
      print("OK")
  finally:
    cursor.close()




except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
