import wx
import wx.xrc
import wx.adv

# import
from function import *


# 插入窗口定义
class insertForm(wx.Frame):
    def __init__(self, parent, tableInfo, db, tableName):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="" , pos=wx.DefaultPosition,
                          size=wx.Size(526, 398), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        root_sizer = wx.BoxSizer(wx.VERTICAL)
        self.control_list = []
        self.info = tableInfo
        self.table = tableName
        self.db = db

        # 根据table信息创建对应的窗口
        for temp in tableInfo:
            temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
            temp_text = titleMap[temp[0]]
            temp_label = wx.StaticText(self, wx.ID_ANY, temp_text, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
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


        # 将按钮与事件绑定
        self.Bind(wx.EVT_SHOW, self.formOnShow)
        self.confirm_button.Bind(wx.EVT_BUTTON, self.confirmButtonClick)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.cancelButtomClick)

    def __del__(self):
        pass

    def formOnShow(self, event):
        event.Skip()


    def confirmButtonClick(self, event):
        event.Skip()


    def cancelButtomClick(self, event):
        self.Close()

