import pymysql
from execute_sql import *


def select_option(message, options, default=0):
    print(message)
    for i, option in enumerate(options):
        print('[{}] '.format(i) + option)
    print('please input a number between 0 and {}, (default {})'.format(len(options) - 1, default))
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
    user = input('please input the username: (input exit to exit)')
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
    pass


def que(db):
    pass


def borrow(db):
    pass


def ret(db):
    pass


def manager_card(db):
    pass
