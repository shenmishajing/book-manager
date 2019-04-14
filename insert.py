from dateutil.parser import *
from main import cursor

def parseTable(table):
    l = list()
    try:
        cursor.execute("desc " + table + ";")
        result = cursor.fetchall()
        for c in result:
            l.append([c[0],c[1]])
    except:
        print("Error")
    return l


def parseType(type,inputs):
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
    print("Select a table:")
    table = input()
    l = parseTable(table)
    if len(l) != 0:
        values = list()
        for c in l:
            print(c[0] + ":",end='')
            temp = input()
            value = parseType(c[1],temp)
            values.append(value)



