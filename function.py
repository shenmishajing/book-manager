import pymysql
from execute_sql import *
import os


def select_option(message, options, default=0):
    print(message)
    for i, option in enumerate(options):
        print('[{}] '.format(i) + option)
    print('please input a number between 0 and {}, (default {}):'.format(len(options) - 1, default))
    choose = input()
    if choose:
        return int(choose)
    else:
        return default


def root_login():
    passwd = input('please input the passwd of root:')
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd=passwd)

    sql = 'use library;'

    execute_sql(db, sql)
    return db


def login(db):
    user = input('please input the username (input exit to exit):')
    if user == 'exit':
        return ''
    passwd = input('please input the passwd of {}:'.format(user))

    sql = '''
                    select * 
                    from administrator
                    where ID='{}' and passwd='{}'
                '''.format(user, passwd)

    result = execute_sql(db, sql)
    if not result:
        print('wrong username or passwd, please check your username and passwd')
        return ''
    else:
        return user


def register(db):
    user = input('please input the username (input exit to exit):')
    if user == 'exit' or not user:
        return ''

    while 1:
        passwd = input('please input the passwd of {} (input exit to exit):'.format(user))
        if not passwd:
            print('empty passwd is not valid')
            continue
        else:
            break

    if passwd == 'exit':
        return ''

    name = input('please input the name of {} (default null):'.format(user))
    if not name:
        name = 'null'
    contact = input('please input the contact of {} (default null):'.format(user))
    if not contact:
        contact = 'null'

    sql = '''
                insert into administrator
                values ('{}','{}','{}','{}')
            '''.format(user, passwd, name, contact)

    result = execute_sql(db, sql)
    return user


def stock_in(db):
    choose = select_option('Please choose method of stocking', ['single book', 'from file', 'exit'])

    if choose == 0:
        bno = input('please input the bno (input exit to exit):')
        if bno == 'exit':
            return
        category = input('please input the category (default null):')
        if not category:
            category = 'null'
        title = input('please input the title (default null):')
        if not title:
            title = 'null'
        press = input('please input the press (default null):')
        if not press:
            press = 'null'
        year = input('please input the year (default 2019):')
        if not year:
            year = 2019
        else:
            year = int(year)
        author = input('please input the author (default null):')
        if not press:
            press = 'null'
        if not author:
            author = 'null'
        price = input('please input the price (default null):')
        if not price:
            price = 'null'
        total = input('please input the total (default 0):')
        if not total:
            total = 0
        else:
            total = int(total)
        stock = input('please input the stock (default 0):')
        if not stock:
            stock = 0
        else:
            stock = int(stock)

        sql = '''
                insert into book
                values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')
            '''.format(bno, category, title, press, year, author, price, total, stock)

        result = execute_sql(db, sql)
    elif choose == 1:
        path = input('please input the file path (default data.txt): {}/'.format(os.getcwd()))
        if not path:
            path = 'data.txt'
        path = os.getcwd() + '/' + path

        lines = open(path, 'r').readlines()

        for line in lines:
            sql = '''
                    insert into book
                    values {}
                '''.format(line)

            result = execute_sql(db, sql)
    else:
        return


def que(db):
    pass


def borrow(db):
    pass


def ret(db):
    pass


def manager_card(db):
    choose = select_option('Please choose next action', ['add', 'delete', 'exit'])

    if choose == 0:
        cno = input('please input the cno (input exit to exit):')
        if cno == 'exit':
            return
        name = input('please input the name (default null):')
        if not name:
            name = 'null'
        department = input('please input the department (default null):')
        if not department:
            department = 'null'
        t = input('please input the type (default null):')
        if not t:
            t = 'null'

        sql = '''
                insert into card
                values ('{}','{}','{}','{}')
            '''.format(cno, name, department, t)

        result = execute_sql(db, sql)
    elif choose == 1:
        cno = input('please input the cno (input exit to exit):')
        if cno == 'exit':
            return

        sql = '''
                delete from card
                where cno='{}'
            '''.format(cno)

        result = execute_sql(db, sql)
    else:
        return
