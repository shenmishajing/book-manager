import wx
import wx.xrc
import wx.adv
import sys

import pymysql
#from dateutil.parser import *
#from main import db
from function import *


#插入窗口定义
class insertForm(wx.Frame):
    def __init__(self, parent,tableInfo):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="信息插入", pos=wx.DefaultPosition,
                          size=wx.Size(526, 398), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)


        rootSizer = wx.BoxSizer(wx.VERTICAL)
        self.controlList = []
        self.types = list(x[1] for x in tableInfo)

        #根据table信息创建对应的窗口
        for temp in tableInfo:
            tempSizer = wx.BoxSizer( wx.HORIZONTAL )
            tempLabel = wx.StaticText( self, wx.ID_ANY, temp[0], wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
            tempLabel.Wrap(-1)
            tempSizer.Add(tempLabel, 2, wx.ALL, 5)
            if "date" in temp[1]:
                control = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
            elif "int" in temp[1]:
                control = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, sys.maxsize, 0 )
            elif "decimal" in temp[1]:
                temp[1].replace(" ","")
                nums = list(int(x) for x in temp[1].split("(")[1].split(")")[0].split(","))
                control = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS,
                                  0, float("inf"), 0, 1)
                control.SetDigits(nums[1])
            else:
                control = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.controlList.append(control)
            tempSizer.Add(self.controlList[len(self.controlList) - 1], 5 , wx.ALL, 5 )
            rootSizer.Add(tempSizer, 1, wx.EXPAND, 5 )

        self.confirmButton = wx.Button( self, wx.ID_ANY, "确定", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cancelButton = wx.Button(self, wx.ID_ANY, "取消", wx.DefaultPosition, wx.DefaultSize, 0)

        bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        bottomSizer.Add(self.confirmButton, 1, wx.ALL, 5)
        bottomSizer.Add(self.cancelButton, 1, wx.ALL, 5)

        rootSizer.Add(bottomSizer, 1, wx.EXPAND, 5 )

        self.SetSizer(rootSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Show()

        #将按钮与事件绑定
        self.confirmButton.Bind(wx.EVT_BUTTON,self.confirmButtonClick)

    def __del__(self):
        pass

    def confirmButtonClick(self, event):
        event.Skip()


def test(tableInfo):
    ex = wx.App()
    insertForm(None,tableInfo)
    ex.MainLoop()


passwd = input('please input the passwd of root:')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd=passwd)
table = input('choose a table:')

try:
    execute_sql(db,"use library;")
    result = execute_sql(db, "desc " + table + ";")
    test(result)
except:
    print("Error")


"""
cursor = db.cursor()


def parse_table(table):
    l = []
    try:
        result = execute_sql(db, "desc " + table + ";")
        for c in result:
            l.append([c[0], c[1]])
    except:
        print("Error")
    return l


def parse_type(type, inputs):
    if "char" in type:
        result = inputs
    elif "int" in type:
        result = int(inputs)
    elif "decimal" in type:
        result = float(inputs)
    elif "date" in type:
        result = parse(inputs).date()
    return result


def insert():
    table = input("Select a table:")
    l = parse_table(table)
    if len(l) != 0:
        values = []
        for c in l:
            print(c[0] + ":", end='')
            temp = input()
            value = parse_type(c[1], temp)
            values.append(value)

"""