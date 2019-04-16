import wx
import insert
from execute_sql import *


class returnForm(insert.insertForm):

    def formOnShow(self, event):
        self.control_list[4].Enable(False)

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
            old_date = self.control_list[2].GetValue()
            old_date = "{}/{}/{}".format(old_date.year, old_date.month + 1, old_date.day)
            sql = "select return_date from borrow where bno = '{}' and cno = '{}' and borrow_date = '{}';".format(
                self.control_list[1].GetValue(), self.control_list[0].GetValue(), old_date)
            result = execute_sql(self.db, sql)
            if len(result) == 0:
                temp = 1
            else:
                temp = result[0][0]
            if temp is None:
                temp_date = self.control_list[3].GetValue()
                date = "{}/{}/{}".format(temp_date.year, temp_date.month + 1, temp_date.day)

                sql = ['''
                                update borrow
                                set return_date='{}'
                                where bno='{}' and cno='{}' and borrow_date='{}'
                            '''.format(date, self.control_list[1].GetValue(), self.control_list[0].GetValue(),
                                       old_date),
                       '''
                           update book
                           set stock=stock+1
                           where bno='{}';
                           '''.format(self.control_list[1].GetValue())
                       ]
                result = execute_sql(self.db, sql)
                if type(result) == str:
                    dlg = wx.MessageDialog(None, u"信息更新失败", u"错误", wx.YES_NO | wx.ICON_QUESTION)
                    dlg.ShowModal()
                    dlg.Destroy()
                else:
                    self.Close()
            else:
                dlg = wx.MessageDialog(None, u"还书操作错误", u"错误", wx.YES_NO | wx.ICON_QUESTION)
                dlg.ShowModal()
                dlg.Destroy()
