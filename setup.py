import pymysql
from function import *

passwd = input('please input the passwd of root:')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd=passwd)

sqls = ['''
            show databases;
        ''',
        '''
            drop database library;
        ''',
        '''
            show databases;
        ''',
        '''
            create database library;
        ''',
        '''
            show databases;
        ''',
        '''
            use library;
        ''',
        '''
            create table book
            (
                bno char(8) primary key ,
                category varchar(10) null,
                title varchar(40) null,
                press varchar(30) null,
                year int null,
                author varchar(20) null,
                price decimal(7,2) null,
                total int null,
                stock int null
            );
        ''',
        '''
            create table card
            (
                cno char(7)  primary key ,
                name varchar(10) null,
                department varchar(40) null,
                type char null
            );
        ''',
        '''
            create table administrator
            (
                ID char(7) primary key,
                passwd varchar(30) not null,
                name varchar(20) null,
                contact varchar(20) null
            );
        ''',
        '''
            create table borrow
            (
                cno char(7),
                bno char(8),
                borrow_date date null,
                return_date date null,
                administrator_ID char(7) null,
                primary key (bno,cno),
                foreign key (bno) references book(bno) on update cascade on delete cascade,
                foreign key (cno) references card(cno) on update cascade on delete cascade,
                foreign key (administrator_ID) references administrator(ID) on update cascade on delete cascade
            );
        ''',
        '''
            show tables;
        ''']

results = execute_sql(db, sqls)

for result in results:
    print(result)

db.close()
