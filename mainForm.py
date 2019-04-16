import wx
from function import *
import mainFormTemplate

class mainForm(mainFormTemplate.maiFrame):


    def connectClick(self, event):
        pwd = self.rootpwd.GetValue()
        try:
            self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd=pwd)
            self.rootpwd.Clear()
            self.admin_no.Enable(True)
            self.madmin_pwd.Enable(True)
            self.login.Enable(True)
            execute_sql(db = self.db,sql="use library;")
        except:
            wx.MessageBox(None, u"连接密码错误", u"错误", wx.YES_NO | wx.ICON_QUESTION)


    def loginClick( self, event ):
        user = self.admin_no.GetValue()
        pwd = self.madmin_pwd.GetValue()
        result = login(self.db,user,pwd)
        if result == "Error":
            wx.MessageBox(None, u"管理员账户错误", u"错误", wx.YES_NO | wx.ICON_QUESTION)
        else:
            self.available = True
            self.admin_no.Clear()
            self.madmin_pwd.Clear()

    def searchChooseChange(self, event):
        if self.available:
            table = self.table_choise.GetString(self.table_choise.GetSelection())
            info = execute_sql(self.db,"desc " + table + ";")

            select_op = []
            index = 0
            for c in info:
                select_op.append(c[0])
                #self.info_grid.SetColLabelValue(index,c)
                index += 1
            self.artribute_choice.SetItems(select_op)






app = wx.App()
mainform = mainForm(None)
mainform.Show()
app.MainLoop()
