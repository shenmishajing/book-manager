import wx
import insert
from execute_sql import *

class borrowForm(insert.insertForm):


    def confirmButtonClick(self, event):
        sql = "select cno from book where cno = " + "'{}';".format(self.control_list[0].GetValue())
        sql = "select stock from book where bno = " + "'{}';".format(self.control_list[1].GetValue())
        result = execute_sql(self.db,sql)
        print(result)
        if type(result) == tuple:
            if len(result) == 0:
                dlg = wx.MessageDialog(None, u"书本不存在", u"错误", wx.YES_NO | wx.ICON_QUESTION)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                stock = result[0][0]


db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Jingyang6268')
execute_sql(db, "use library;")
result = execute_sql(db, "desc borrow;")
app = wx.App()
temp = borrowForm(None,result,db,"borrow")
app.MainLoop()