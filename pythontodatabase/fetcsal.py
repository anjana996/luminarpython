import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Anjana@7",
    auth_plugin="mysql_native_password",
    database="luminarpython"
)
print(db)
cursor=db.cursor()

sql="SELECT FIRST_NAME FROM EMPLOYEE WHERE INCOME>15000"
try:
    cursor.execute(sql)
    res = cursor.fetchall()

    for x in res:
        print(x)

except Exception as e:
    print(e.args)

finally:
    db.close()
