import wx
import insert
from execute_sql import *


class normalInsertForm(insert.insertForm):


    def confirmButtonClick(self, event):
        values = []
        for c in self.control_list:
            values.append(c.GetValue())
        sql = "insert into " + self.table + " ("
        for index in range(0, len(self.info)):
            if index != len(self.info) - 1:
                sql = sql + self.info[index][0] + ","
            else:
                sql = sql + self.info[index][0] + ") values ("

        for index in range(0, len(values)):
            if type(values[index]) == str:
                values[index] = "'" + values[index] + "'"
            elif type(values[index]) == wx._core.DateTime:
                year = values[index].year
                month = values[index].month + 1
                day = values[index].day
                values[index] = "'{}/{}/{}'".format(year, month, day)
            if index != len(values) - 1:
                sql += "{},".format(values[index])
            else:
                sql += "{});".format(values[index])
        print(sql)
        result = execute_sql(self.db, sql)
        self.Close()