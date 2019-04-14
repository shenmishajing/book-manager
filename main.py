import pymysql

print('please input the passwd of root')
passwd = input()

db = pymysql.connect(host='localhost', port=3306, user='root', passwd=passwd)


def select_option(message, options, default=0):
    pass


print('please input the username')
user = input()

print('please input the passwd of ' + user)
passwd = input()

db = pymysql.Connect(host='localhost', port=3306, user=user, passwd=passwd)

cursor = db.cursor()

try:
    cursor.execute("use library;")
    cursor.execute("desc borrow;")
    result = cursor.fetchall()
    for c in result:
        print(c)
        print(c[0] + "," + c[1])

except:
    print("database doesn't exist!")

cursor.close()
db.close()
