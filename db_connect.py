import mysql.connector

def conn():
 mydb = mysql.connector.connect(
   host="127.0.0.1",
   port = "3306",
   user="root",
   password="cronus123",
   database = "cronus"
 )
 return mydb
def get_cp(cp):
 mydb = conn()
 mycursor = mydb.cursor()
 val = (cp,)
 sql = "SELECT answer FROM cronus_personality where predicate = %s"
 mycursor.execute(sql, val)
 records = mycursor.fetchall()
 result = []
 for i in records:
  result.append(i[0])
 return tuple(result)

def get_up(up_param):
 mydb = conn()
 mycursor = mydb.cursor()
 val = (up_param,)
 sql = "SELECT answer FROM user_attr_ans_variation where attribute = %s"
 mycursor.execute(sql, val)
 records = mycursor.fetchall()
 result = []
 for i in records:
  result.append(i[0])
 return tuple(result)

def get_all_user_attribute_pattern():
 mydb = conn()
 mycursor = mydb.cursor()
 mycursor.execute("select answer,attribute from user_attr_ans_variation")
 records = mycursor.fetchall()
 result = []
 for i in records:
  result.append(i)
 return result

