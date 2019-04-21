# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class maiFrame
###########################################################################

class maiFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.db = None
		self.available = False
		self.table_info = None

		root_sizer = wx.BoxSizer( wx.HORIZONTAL )

		login_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"root密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		login_sizer.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.rootpwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		login_sizer.Add( self.rootpwd, 0, wx.ALL, 5 )

		self.connect_button = wx.Button( self, wx.ID_ANY, u"连接", wx.DefaultPosition, wx.DefaultSize, 0 )
		login_sizer.Add( self.connect_button, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"管理员帐号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		login_sizer.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.admin_no = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		login_sizer.Add( self.admin_no, 0, wx.ALL, 5 )
		self.admin_no.Enable(False)

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"管理员密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		login_sizer.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.madmin_pwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		login_sizer.Add( self.madmin_pwd, 0, wx.ALL, 5 )
		self.madmin_pwd.Enable(False)

		self.login = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		login_sizer.Add( self.login, 0, wx.ALL, 5 )
		self.login.Enable(False)

		self.register = wx.Button(self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0)
		login_sizer.Add(self.register, 0, wx.ALL, 5)
		self.register.Enable(False)

		root_sizer.Add( login_sizer, 2, wx.EXPAND, 5 )

		show_sizer = wx.BoxSizer( wx.VERTICAL )

		function_sizer = wx.BoxSizer( wx.HORIZONTAL )

		table_choiseChoices = [ u"图书", u"借书记录", u"借书卡"]
		self.table_choise = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, table_choiseChoices, 0 )
		self.table_choise.SetSelection( 0 )
		function_sizer.Add( self.table_choise, 1, wx.ALL, 5 )

		artribute_choiceChoices = []
		self.artribute_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, artribute_choiceChoices, 0 )
		self.artribute_choice.SetSelection( 0 )
		function_sizer.Add( self.artribute_choice, 1, wx.ALL, 5 )


		self.condition = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		function_sizer.Add( self.condition, 1, wx.ALL, 5 )

		self.search_button = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		function_sizer.Add( self.search_button, 1, wx.ALL, 5 )
		self.search_button.Enable(False)

		order_choices = []
		self.order_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, order_choices,0)
		self.order_choice.SetSelection(0)
		function_sizer.Add(self.order_choice, 1, wx.ALL, 5)

		show_sizer.Add( function_sizer, 1, wx.EXPAND, 5 )

		modify_sizer = wx.BoxSizer( wx.HORIZONTAL )

		modify_table_choiceChoices = [ u"图书管理", u"图书借阅管理", u"借书卡管理", u"管理员信息管理"]
		self.modify_table_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, modify_table_choiceChoices, 0 )
		self.modify_table_choice.SetSelection( 0 )
		modify_sizer.Add( self.modify_table_choice, 1, wx.ALL, 5 )

		self.insert_button = wx.Button( self, wx.ID_ANY, u"单本入库", wx.DefaultPosition, wx.DefaultSize, 0 )
		modify_sizer.Add( self.insert_button, 0, wx.ALL, 5 )

		self.insert_many = wx.Button(self, wx.ID_ANY, u"批量入库", wx.DefaultPosition, wx.DefaultSize, 0)
		modify_sizer.Add(self.insert_many, 0, wx.ALL, 5)

		self.delete_button = wx.Button( self, wx.ID_ANY, u"删除书籍", wx.DefaultPosition, wx.DefaultSize, 0 )
		modify_sizer.Add( self.delete_button, 0, wx.ALL, 5 )


		show_sizer.Add( modify_sizer, 1, wx.EXPAND, 5 )

		self.info_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.info_grid.CreateGrid( 50, 50 )
		self.info_grid.EnableEditing( False )
		self.info_grid.EnableGridLines( True )
		self.info_grid.EnableDragGridSize( False )
		self.info_grid.SetMargins( 0, 0 )

		# Columns
		self.info_grid.EnableDragColMove( False )
		self.info_grid.EnableDragColSize( True )
		self.info_grid.SetColLabelSize( 30 )
		self.info_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.info_grid.EnableDragRowSize( True )
		self.info_grid.SetRowLabelSize( 80 )
		self.info_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.info_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		show_sizer.Add( self.info_grid, 5, wx.ALL, 5 )


		root_sizer.Add( show_sizer, 5, wx.EXPAND, 5 )


		self.SetSizer( root_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.connect_button.Bind( wx.EVT_BUTTON, self.connectClick )
		self.login.Bind( wx.EVT_BUTTON, self.loginClick )
		self.register.Bind( wx.EVT_BUTTON, self.registerClick)
		self.table_choise.Bind( wx.EVT_CHOICE, self.searchChooseChange )
		self.modify_table_choice.Bind(wx.EVT_CHOICE,self.modifyChoiceChange)
		self.search_button.Bind( wx.EVT_BUTTON, self.searchButtonClick )
		self.insert_button.Bind( wx.EVT_BUTTON, self.insertButtonClick )
		self.delete_button.Bind( wx.EVT_BUTTON, self.deleteButtonClick )
		self.insert_many.Bind( wx.EVT_BUTTON, self.insertManyClick)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def connectClick( self, event ):
		event.Skip()

	def loginClick( self, event ):
		event.Skip()

	def searchChooseChange( self, event ):
		event.Skip()

	def searchButtonClick( self, event ):
		event.Skip()

	def modifyChoiceChange(self, event):
		event.Skip()

	def insertButtonClick( self, event ):
		event.Skip()

	def deleteButtonClick( self, event ):
		event.Skip()

	def insertManyClick(self , event):
		event.Skip()

	def registerClick(self , event):
		event.Skip()