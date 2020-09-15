#import paxkage

import mysql.connector
#establish commection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Anjana@7",
    auth_plugin="mysql_native_password",
    database="luminarpython"
)
#open databse
print(db)
cursor=db.cursor()#python to data base connection
#query
sql="INSERT INTO EMPLOYEE(FIRST_NAME,AGE,SEX,INCOME)VALUES('AMI',22,'F',50000)"
try:
    
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()#partial changes are undone
    print(e.args)
finally:
    db.close()