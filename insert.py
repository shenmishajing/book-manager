from dateutil.parser import *
from main import db
from function import *

cursor = db.cursor()


def parse_table(table):
    l = []
    try:
        result = execute_sql(db, "desc " + table + ";")
        for c in result:
            l.append([c[0], c[1]])
    except:
        print("Error")
    return l


def parse_type(type, inputs):
    if "char" in type:
        result = inputs
    elif "int" in type:
        result = int(inputs)
    elif "decimal" in type:
        result = float(inputs)
    elif "date" in type:
        result = parse(inputs).date()
    return result


def insert():
    table = input("Select a table:")
    l = parse_table(table)
    if len(l) != 0:
        values = []
        for c in l:
            print(c[0] + ":", end='')
            temp = input()
            value = parse_type(c[1], temp)
            values.append(value)
