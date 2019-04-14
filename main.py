import pymysql



print('please input the username')
user = input()

print('please input the passwd of ' + user)
passwd = input()

db = pymysql.Connect(host='localhost', port=3306, user=user, passwd=passwd)

cursor = db.cursor()


try:
    cursor.execute("use library;")
    cursor.execute("desc book;")
    result = cursor.fetchall()
    for c in result:
        print(c[0] + "," + c[1])

except:
    print("database doesn't exist!")



cursor.close()
db.close()
