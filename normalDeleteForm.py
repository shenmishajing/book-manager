#import wx
import insert
from execute_sql import *

class deleteForm(insert.insertForm):

    def confirmButtonClick(self, event):
        sql = "delete from {} where ".format(self.table)
        l = len(self.info)
        for i in range(0,l):
            name = self.info[i][0]
            type = self.info[i][1]
            if i == l - 1:
                if "char" in type or "date" in type:
                    sql += "{}='{}';".format(name,self.control_list[i].GetValue())
                else:
                    sql += "{}={}".format(name,self.control_list[i].GetValue())
            else:
                if "char" in type or "date" in type:
                    sql += "{}='{}' or ".format(name, self.control_list[i].GetValue())
                else:
                    sql += "{}={} or ".format(name, self.control_list[i].GetValue())
            execute_sql(self.db,sql)
        self.Close()