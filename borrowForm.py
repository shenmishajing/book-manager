import wx
import insert
from execute_sql import *


class borrowForm(insert.insertForm):

    def confirmButtonClick(self, event):
        sql = "select * from card where cno = '{}';".format(self.control_list[0].GetValue())
        result = execute_sql(self.db, sql)
        if not result:
            dlg = wx.MessageDialog(None, u"借书证不存在", u"错误", wx.YES_NO | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
        sql = "select stock from book where bno = '{}';".format(self.control_list[1].GetValue())
        result = execute_sql(self.db, sql)
        if not result:
            dlg = wx.MessageDialog(None, u"书本不存在", u"错误", wx.YES_NO | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            stock = result[0][0]
            if not stock:
                dlg = wx.MessageDialog(None, u"书本没有库存", u"错误", wx.YES_NO | wx.ICON_QUESTION)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                sql = ['''
                            insert into borrow
                            values ('{}','{}','{}','{}','{}');
                        '''.format(self.control_list[0].GetValue(), self.control_list[1].GetValue(), data, 'null',
                                   cur_administrator_ID),
                       '''
                            update book
                            set stock=stock-1
                            where bno='{}'
                            '''.format(self.control_list[0].GetValue())
                       ]
                result = execute_sql(self.db, sql)


db = pymysql.connect(host='localhost', port=3306, user='root', passwd='pytniiqg0412')
execute_sql(db, "use library;")
result = execute_sql(db, "insert into borrow values ('12123','2423');")
result = execute_sql(db, "desc borrow;")
app = wx.App()
temp = borrowForm(None, result, db, "borrow")
app.MainLoop()
