# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SMeter_Statistics.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1110, 853)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_1)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_database_setting = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_database_setting.sizePolicy().hasHeightForWidth())
        self.pushButton_database_setting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_database_setting.setFont(font)
        self.pushButton_database_setting.setObjectName("pushButton_database_setting")
        self.horizontalLayout.addWidget(self.pushButton_database_setting)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Label.setFont(font)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.DateTimeEdit_fac_start = QtWidgets.QDateTimeEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DateTimeEdit_fac_start.setFont(font)
        self.DateTimeEdit_fac_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateTimeEdit_fac_start.setCalendarPopup(True)
        self.DateTimeEdit_fac_start.setObjectName("DateTimeEdit_fac_start")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_fac_start)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setVerticalSpacing(7)
        self.formLayout_4.setObjectName("formLayout_4")
        self.Label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Label_3.setFont(font)
        self.Label_3.setObjectName("Label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.DateTimeEdit_fac_end = QtWidgets.QDateTimeEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DateTimeEdit_fac_end.setFont(font)
        self.DateTimeEdit_fac_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(23, 59, 59)))
        self.DateTimeEdit_fac_end.setTime(QtCore.QTime(23, 59, 59))
        self.DateTimeEdit_fac_end.setCalendarPopup(True)
        self.DateTimeEdit_fac_end.setObjectName("DateTimeEdit_fac_end")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_fac_end)
        self.horizontalLayout.addLayout(self.formLayout_4)
        self.pushButton_fac = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_fac.setFont(font)
        self.pushButton_fac.setObjectName("pushButton_fac")
        self.horizontalLayout.addWidget(self.pushButton_fac)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.widget_fac = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_fac.sizePolicy().hasHeightForWidth())
        self.widget_fac.setSizePolicy(sizePolicy)
        self.widget_fac.setObjectName("widget_fac")
        self.verticalLayout_3.addWidget(self.widget_fac)
        self.gridLayout_11.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.Label_alert_start_2 = QtWidgets.QLabel(self.groupBox_5)
        self.Label_alert_start_2.setObjectName("Label_alert_start_2")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_alert_start_2)
        self.DateTimeEdit_meterForm_start = QtWidgets.QDateTimeEdit(self.groupBox_5)
        self.DateTimeEdit_meterForm_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateTimeEdit_meterForm_start.setCalendarPopup(True)
        self.DateTimeEdit_meterForm_start.setObjectName("DateTimeEdit_meterForm_start")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_meterForm_start)
        self.Label_alert_end_2 = QtWidgets.QLabel(self.groupBox_5)
        self.Label_alert_end_2.setObjectName("Label_alert_end_2")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_alert_end_2)
        self.DateTimeEdit_meterForm_end = QtWidgets.QDateTimeEdit(self.groupBox_5)
        self.DateTimeEdit_meterForm_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(23, 59, 59)))
        self.DateTimeEdit_meterForm_end.setCalendarPopup(True)
        self.DateTimeEdit_meterForm_end.setObjectName("DateTimeEdit_meterForm_end")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_meterForm_end)
        self.verticalLayout.addLayout(self.formLayout_6)
        self.pushButton_meterForm = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_meterForm.setFont(font)
        self.pushButton_meterForm.setObjectName("pushButton_meterForm")
        self.verticalLayout.addWidget(self.pushButton_meterForm)
        self.pushButton_export_meter = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_export_meter.setObjectName("pushButton_export_meter")
        self.verticalLayout.addWidget(self.pushButton_export_meter)
        spacerItem = QtWidgets.QSpacerItem(118, 549, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableWidget_meterForm = QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget_meterForm.setAlternatingRowColors(True)
        self.tableWidget_meterForm.setObjectName("tableWidget_meterForm")
        self.tableWidget_meterForm.setColumnCount(0)
        self.tableWidget_meterForm.setRowCount(0)
        self.gridLayout_7.addWidget(self.tableWidget_meterForm, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label_2 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Label_2.setFont(font)
        self.Label_2.setObjectName("Label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.DateTimeEdit_meterGraph_start = QtWidgets.QDateTimeEdit(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DateTimeEdit_meterGraph_start.setFont(font)
        self.DateTimeEdit_meterGraph_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateTimeEdit_meterGraph_start.setCalendarPopup(True)
        self.DateTimeEdit_meterGraph_start.setObjectName("DateTimeEdit_meterGraph_start")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_meterGraph_start)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_5.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setVerticalSpacing(7)
        self.formLayout_5.setObjectName("formLayout_5")
        self.Label_4 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Label_4.setFont(font)
        self.Label_4.setObjectName("Label_4")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.DateTimeEdit_meterGraph_end = QtWidgets.QDateTimeEdit(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DateTimeEdit_meterGraph_end.setFont(font)
        self.DateTimeEdit_meterGraph_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(23, 59, 59)))
        self.DateTimeEdit_meterGraph_end.setTime(QtCore.QTime(23, 59, 59))
        self.DateTimeEdit_meterGraph_end.setCalendarPopup(True)
        self.DateTimeEdit_meterGraph_end.setObjectName("DateTimeEdit_meterGraph_end")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_meterGraph_end)
        self.horizontalLayout_2.addLayout(self.formLayout_5)
        self.pushButton_meterGraph = QtWidgets.QPushButton(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_meterGraph.setFont(font)
        self.pushButton_meterGraph.setObjectName("pushButton_meterGraph")
        self.horizontalLayout_2.addWidget(self.pushButton_meterGraph)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.widget_meterGraph = QtWidgets.QWidget(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_meterGraph.sizePolicy().hasHeightForWidth())
        self.widget_meterGraph.setSizePolicy(sizePolicy)
        self.widget_meterGraph.setObjectName("widget_meterGraph")
        self.verticalLayout_4.addWidget(self.widget_meterGraph)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setFlat(True)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.Label_alert_start_3 = QtWidgets.QLabel(self.groupBox_8)
        self.Label_alert_start_3.setObjectName("Label_alert_start_3")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_alert_start_3)
        self.DateTimeEdit_error_start = QtWidgets.QDateTimeEdit(self.groupBox_8)
        self.DateTimeEdit_error_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateTimeEdit_error_start.setCalendarPopup(True)
        self.DateTimeEdit_error_start.setObjectName("DateTimeEdit_error_start")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_error_start)
        self.Label_alert_end_3 = QtWidgets.QLabel(self.groupBox_8)
        self.Label_alert_end_3.setObjectName("Label_alert_end_3")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_alert_end_3)
        self.DateTimeEdit_error_end = QtWidgets.QDateTimeEdit(self.groupBox_8)
        self.DateTimeEdit_error_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(23, 59, 59)))
        self.DateTimeEdit_error_end.setCalendarPopup(True)
        self.DateTimeEdit_error_end.setObjectName("DateTimeEdit_error_end")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DateTimeEdit_error_end)
        self.verticalLayout_2.addLayout(self.formLayout_7)
        self.pushButton_error = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_error.setFont(font)
        self.pushButton_error.setObjectName("pushButton_error")
        self.verticalLayout_2.addWidget(self.pushButton_error)
        self.pushButton_export_error = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_export_error.setObjectName("pushButton_export_error")
        self.verticalLayout_2.addWidget(self.pushButton_export_error)
        spacerItem1 = QtWidgets.QSpacerItem(118, 549, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_10.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setFlat(True)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableWidget_error = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_error.setAlternatingRowColors(True)
        self.tableWidget_error.setObjectName("tableWidget_error")
        self.tableWidget_error.setColumnCount(0)
        self.tableWidget_error.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget_error, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_7, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.gridLayout_6.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "电能表室内检定质量分析工具（年度数据统计）"))
        self.label.setText(_translate("MainWindow", "电能表室内检定质量分析工具（年度数据统计）"))
        self.pushButton_database_setting.setText(_translate("MainWindow", "数据库配置"))
        self.Label.setText(_translate("MainWindow", "起"))
        self.DateTimeEdit_fac_start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.Label_3.setText(_translate("MainWindow", "止"))
        self.DateTimeEdit_fac_end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.pushButton_fac.setText(_translate("MainWindow", "显示"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "供应商分布"))
        self.groupBox_5.setTitle(_translate("MainWindow", "设置"))
        self.Label_alert_start_2.setText(_translate("MainWindow", "起"))
        self.DateTimeEdit_meterForm_start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.Label_alert_end_2.setText(_translate("MainWindow", "止"))
        self.DateTimeEdit_meterForm_end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.pushButton_meterForm.setText(_translate("MainWindow", "显示数据"))
        self.pushButton_export_meter.setText(_translate("MainWindow", "导出当前数据"))
        self.groupBox_6.setTitle(_translate("MainWindow", "数据表显示"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "到货后全检（表）"))
        self.Label_2.setText(_translate("MainWindow", "起"))
        self.DateTimeEdit_meterGraph_start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.Label_4.setText(_translate("MainWindow", "止"))
        self.DateTimeEdit_meterGraph_end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.pushButton_meterGraph.setText(_translate("MainWindow", "显示"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "到货后全检（图）"))
        self.groupBox_8.setTitle(_translate("MainWindow", "设置"))
        self.Label_alert_start_3.setText(_translate("MainWindow", "起"))
        self.DateTimeEdit_error_start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.Label_alert_end_3.setText(_translate("MainWindow", "止"))
        self.DateTimeEdit_error_end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.pushButton_error.setText(_translate("MainWindow", "显示数据"))
        self.pushButton_export_error.setText(_translate("MainWindow", "导出当前数据"))
        self.groupBox_7.setTitle(_translate("MainWindow", "数据表显示"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "全年误差分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "检定质量分析"))

