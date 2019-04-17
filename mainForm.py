import wx
from function import *
import mainFormTemplate
import normalInsertForm
import borrowForm
import normalDeleteForm
import returnForm

last_order = None


class mainForm(mainFormTemplate.maiFrame):

    def connectClick(self, event):
        pwd = self.rootpwd.GetValue()
        try:
            self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd=pwd)
            self.rootpwd.Clear()
            self.admin_no.Enable(True)
            self.madmin_pwd.Enable(True)
            self.login.Enable(True)
            self.register.Enable(True)
            execute_sql(db=self.db, sql="use library;")
            dlg = wx.MessageDialog(None, u"数据库连接成功", u"连接", wx.YES_DEFAULT | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
            self.connect_button.Enable(False)
            self.rootpwd.Enable(False)
        except:
            dlg = wx.MessageDialog(None, u"连接密码错误", u"错误", wx.YES_NO | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
            self.rootpwd.Clear()

    def loginClick(self, event):
        user = self.admin_no.GetValue()
        pwd = self.madmin_pwd.GetValue()
        result = login(self.db, user, pwd)
        if result == "Error":
            dlg = wx.MessageDialog(None, u"账户错误", u"错误", wx.YES_NO | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            self.available = True
            borrowForm.admin_id = self.admin_no.GetValue()
            self.admin_no.Clear()
            self.madmin_pwd.Clear()
            dlg = wx.MessageDialog(None, u"登录成功", u"登录", wx.YES_DEFAULT | wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()
            self.admin_no.Enable(False)
            self.madmin_pwd.Enable(False)
            self.login.Enable(False)
            self.register.Enable(False)

    def searchChooseChange(self, event):
        if self.available:
            table = self.table_choise.GetString(self.table_choise.GetSelection())
            self.table_info = execute_sql(self.db, "desc " + table + ";")
            select_op = []
            for index in range(0, 50):
                self.info_grid.SetColLabelValue(index, "null")
            index = 0
            for c in self.table_info:
                select_op.append(c[0])
                self.info_grid.SetColLabelValue(index, c[0])
                index += 1
            self.artribute_choice.SetItems(select_op)
            self.order_choice.SetItems(select_op)
            self.artribute_choice.Select(0)
            self.order_choice.Select(0)
            self.search_button.Enable(True)

    def searchButtonClick(self, event):
        global last_order
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
                    sql += "'{}'".format(cond)
                else:
                    sql += "{}".format(cond)
            cur_order = self.order_choice.GetString(self.order_choice.GetSelection())
            sql += ' order by {};'.format(cur_order)
            result = execute_sql(self.db, sql)
            if cur_order == last_order:
                result = list(result)
                result.reverse()
                last_order = None
            else:
                last_order = cur_order
            l = min(50, len(result))
            if l == 0:
                templ = 0
            else:
                templ = len(result[0])

            for i in range(0, l):
                for j in range(0, templ):
                    self.info_grid.SetCellValue(i, j, "{}".format(result[i][j]))

    def insertManyClick(self, event):
        if self.available:
            file_wildcard = "文本文件(*.txt)|*.txt"
            dlg = wx.FileDialog(self, "打开文件",
                                os.getcwd(),
                                style=wx.FD_OPEN,
                                wildcard=file_wildcard)
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                lines = open(filename, 'r').readlines()
                for line in lines:
                    sql = '''
                                 insert into book
                                values {};
                            '''.format(line)
                    result = execute_sql(self.db, sql)
            dlg.Destroy()

    def modifyChoiceChange(self, event):
        choice = self.modify_table_choice.GetString(self.modify_table_choice.GetSelection())
        if choice == "图书管理":
            self.insert_button.SetLabel("单本入库")
            self.delete_button.Enable(False)
            self.delete_button.SetLabel("删除书籍")
        elif choice == "图书借阅管理":
            self.insert_button.SetLabel("借书")
            self.delete_button.Enable(True)
            self.delete_button.SetLabel("还书")
        elif choice == "借书卡管理":
            self.insert_button.SetLabel("添加借书卡")
            self.delete_button.Enable(True)
            self.delete_button.SetLabel("删除借书卡")
        else:
            self.insert_button.SetLabel("添加管理员")
            self.delete_button.Enable(False)
            self.delete_button.SetLabel("删除管理员")

    def insertButtonClick(self, event):
        if self.available:
            label = self.insert_button.GetLabel()
            if label == "借书":
                table_name = "borrow"
                table_info = execute_sql(self.db, "desc " + table_name + ";")
                insert_form = borrowForm.borrowForm(None, table_info, self.db, table_name)
            else:
                if label == "单本入库":
                    table_name = "book"
                elif label == "添加借书卡":
                    table_name = "card"
                else:
                    table_name = "administrator"
                table_info = execute_sql(self.db, "desc " + table_name + ";")
                insert_form = normalInsertForm.normalInsertForm(None, table_info, self.db, table_name)
            insert_form.Show()

    def deleteButtonClick(self, event):
        if self.available:
            label = self.delete_button.GetLabel()
            if label == "还书":
                table_name = "borrow"
                table_info = execute_sql(self.db, "desc " + table_name + ";")
                delete_form = returnForm.returnForm(None, table_info, self.db, table_name)
            else:
                if label == "删除书籍":
                    table_name = "book"
                elif label == "删除借书卡":
                    table_name = "card"
                else:
                    table_name = "administrator"
                table_info = execute_sql(self.db, "desc " + table_name + ";")
                delete_form = normalDeleteForm.deleteForm(None, table_info, self.db, table_name)
            delete_form.Show()

    def registerClick(self, event):
        table_info = execute_sql(self.db, "desc administrator;")
        insert_form = normalInsertForm.normalInsertForm(None, table_info, self.db, "administrator")
        insert_form.Show()
