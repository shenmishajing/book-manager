import wx
import wx.xrc
import wx.adv

# import
from function import *


# 插入窗口定义
class insertForm(wx.Frame):
    def __init__(self, parent, tableInfo, db, tableName, superForm):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=tableName + "信息插入", pos=wx.DefaultPosition,
                          size=wx.Size(526, 398), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        root_sizer = wx.BoxSizer(wx.VERTICAL)
        self.control_list = []
        self.info = tableInfo
        self.table = tableName
        # self.db = db

        # 根据table信息创建对应的窗口
        for temp in tableInfo:
            temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
            temp_label = wx.StaticText(self, wx.ID_ANY, temp[0], wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
            temp_label.Wrap(-1)
            temp_sizer.Add(temp_label, 2, wx.ALL, 5)
            if "date" in temp[1]:
                control = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,
                                                style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
            elif "int" in temp[1]:
                control = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.SP_ARROW_KEYS, 0, 10000, 0)
            elif "decimal" in temp[1]:
                temp[1].replace(" ", "")
                nums = list(int(x) for x in temp[1].split("(")[1].split(")")[0].split(","))
                control = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.SP_ARROW_KEYS,
                                            0, float("inf"), 0, 1)
                control.SetDigits(nums[1])
            else:
                control = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
            self.control_list.append(control)
            temp_sizer.Add(self.control_list[len(self.control_list) - 1], 5, wx.ALL, 5)
            root_sizer.Add(temp_sizer, 1, wx.EXPAND, 5)

        self.confirm_button = wx.Button(self, wx.ID_ANY, "确定", wx.DefaultPosition, wx.DefaultSize, 0)
        self.cancel_button = wx.Button(self, wx.ID_ANY, "取消", wx.DefaultPosition, wx.DefaultSize, 0)

        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bottom_sizer.Add(self.confirm_button, 1, wx.ALL, 5)
        bottom_sizer.Add(self.cancel_button, 1, wx.ALL, 5)

        root_sizer.Add(bottom_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(root_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Show()

        # 将按钮与事件绑定
        self.confirm_button.Bind(wx.EVT_BUTTON, self.confirmButtonClick)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.cancelButtomClick)

    def __del__(self):
        pass



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
        result = execute_sql(db,sql)

        self.Close()


    def cancelButtomClick(self, event):
        self.Close()


def test(tableInfo, db, tableName):
    ex = wx.App()
    insertForm(None, tableInfo, db, tableName, None)
    ex.MainLoop()


passwd = input('please input the passwd of root:')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd=passwd)
table = input('choose a table:')

try:
    execute_sql(db, "use library;")
    result = execute_sql(db, "desc " + table + ";")
    test(result, db, table)
except:
    print("Error")
