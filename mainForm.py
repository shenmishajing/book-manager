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
            dlg = wx.MessageDialog(None, u"连接密码错误", u"错误", wx.YES_NO | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
            self.rootpwd.Clear()


    def loginClick( self, event ):
        user = self.admin_no.GetValue()
        pwd = self.madmin_pwd.GetValue()
        result = login(self.db,user,pwd)
        if result == "Error":
            dlg = wx.MessageDialog(None, u"连接密码错误", u"错误", wx.YES_NO | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            self.available = True
            self.admin_no.Clear()
            self.madmin_pwd.Clear()

    def searchChooseChange(self, event):
        if self.available:
            table = self.table_choise.GetString(self.table_choise.GetSelection())
            self.table_info = execute_sql(self.db,"desc " + table + ";")
            select_op = []
            for index in range(0,50):
                self.info_grid.SetColLabelValue(index, "null")
            index = 0
            for c in self.table_info:
                select_op.append(c[0])
                self.info_grid.SetColLabelValue(index,c[0])
                index += 1
            self.artribute_choice.SetItems(select_op)
            self.artribute_choice.Select(0)
            self.search_button.Enable(True)


    def searchButtonClick(self, event):
        if self.available:
            self.info_grid.ClearGrid()
            table = self.table_choise.GetString(self.table_choise.GetSelection())
            artribute = self.artribute_choice.GetString(self.artribute_choice.GetSelection())
            info = ''
            for c in self.table_info:
                if artribute == c[0]:
                    info = c[1]
                    break

            cond = self.condition.GetValue()
            sql = "select * from " + table
            if len(cond) != 0:
                sql += " where " + artribute + " = "
                if "char" in info or "date" in info:
                    sql += "'%{}%'".format(cond)
                else:
                    sql += "{}".format(cond)
            sql += ';'
            result = execute_sql(self.db,sql)
            l = min(50,len(result))
            if l == 0:
                templ = 0
            else:
                templ = len(result[0])

            for i in range(0,l):
                for j in range(0,templ):
                    self.info_grid.SetCellValue(i,j,"{}".format(result[i][j]))






app = wx.App()
mainform = mainForm(None)
mainform.Show()
app.MainLoop()
