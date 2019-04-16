import pymysql


def execute_single_sql(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()

    return result


def execute_sql(db, sql):
    try:
        cursor = db.cursor()
        if isinstance(sql, list) or isinstance(sql, tuple):
            result = []
            for s in sql:
                assert isinstance(s, str)
                res = execute_single_sql(cursor, s)
                result.append(res)
        elif isinstance(sql, str):
            result = execute_single_sql(cursor, sql)
        else:
            print('The var sql must be valid sql query in string format or sequence format')
            return 0
        db.commit()
    except AttributeError as e:
        print('The db var must be a pymysql.connect instance')
        print('OR The version of your pymysql may not be right, you can get more information from requirements.txt')
        print(e)
        db.rollback()
        return "{}".format(e)
    except ValueError as e:
        print("The var sql must be valid sql query in string format or sequence format")
        print(e)
        db.rollback()
        return "{}".format(e)
    except pymysql.err.IntegrityError as e:
        print(e)
        db.rollback()
        return "{}".format(e)
    except pymysql.err.OperationalError as e:
        print(e)
        db.rollback()
        return '{}'.format(e)
    except BaseException as e:
        print(e)
        db.rollback()
        return '{}'.format(e)
    cursor.close()
    return result
