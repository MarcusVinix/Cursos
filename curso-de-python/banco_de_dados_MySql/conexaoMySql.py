
#forma de conexao sem tratar os erros
#import mysql.connector

#cnx = mysql.connector.connect(user='root', password='batata123',
#                               host='127.0.0.1',
#                              database='cursodego')

#forma de conexao tratando os erros
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='root',
                                database='cursodego',
                                host='127.0.0.1',
                                password='batata123')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Usuario ou senha inválidos")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Base de dados não existe")
  else:
    print(err)

cur = cnx.cursor()

#sql = "delete from place where id=9"
#cur.execute(sql)

sql = "select * from place"
cur.execute(sql)

recset = cur.fetchall()

for registro in recset:
      print(registro)

cnx.commit()
cnx.close()
