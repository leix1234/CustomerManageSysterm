 # -*- coding: UTF8 -*-
from PyQt4 import QtCore, QtGui
import sys
import os
import cPickle as p
from UI_newuser import Ui_Dialog


#newcumtormer = Ui_Dialog()
#newcumtormer.setupUi()

class MyLabel(QtGui.QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        print "you clicked the label"

    def mouseReleaseEvent(self, QMouseEvent):
        print 'you have release the mouse'

class MyMainWindow(QtGui.QWidget):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.new2 = Ui_Dialog()
        self.resize(930, 550)
        self.setFixedSize(930,550)
        self.setUp()

    #坑啊，event事件需要放在前面
    def mousePressEvent(self, e):
        str = "(" + QtCore.QString.number(e.x()) + "," + QtCore.QString.number(e.y()) + ")"
        if e.button() == QtCore.Qt.LeftButton:
            # self.sBar.showMessage(self.tr("Mouse Left Button Pressed:")+str)
            print 'Mouse Left Button Pressed:', str
            if e.x() > 100 and e.x() < 200 and e.y() > 100 and e.y() < 200 :
                print "pressd new customer"
                self.new2.setupUi()
                self.new2.show()


        elif e.button() == QtCore.Qt.RightButton:
            # self.sBar.showMessage(self.tr("Mouse Right Button Pressed:")+str)
            print 'Mouse Right Button Pressed:', str
        elif e.button() == QtCore.Qt.MidButton:
            # self.sBar.showMessage(self.tr("Mouse Middle Button Pressed:")+str)
            print 'Mouse Middle Button Pressed:', str

    def paintEvent(self, event): #绘制logo
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawPixmap(100, 100, 100, 100, QtGui.QPixmap("../icon/addpeople_fill.png"))
        painter.drawPixmap(300, 100, 100, 100, QtGui.QPixmap("../icon/addressbook.png"))
        painter.drawPixmap(500, 100, 100, 100, QtGui.QPixmap("../icon/search.png"))
        painter.drawPixmap(700, 100, 100, 100, QtGui.QPixmap("../icon/narrow.png"))

        painter.drawPixmap(100, 300, 100, 100, QtGui.QPixmap("../icon/businesscard.png"))
        painter.drawPixmap(300, 300, 100, 100, QtGui.QPixmap("../icon/like_fill.png"))
        painter.drawPixmap(500, 300, 100, 100, QtGui.QPixmap("../icon/like_fill.png"))
        painter.drawPixmap(700, 300, 100, 100, QtGui.QPixmap("../icon/setup.png"))
        painter.end()

    def setUp(self):
        self.setWindowTitle(u'客户管理系统')
        #self.setNumDigits(0)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.90)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)


        # lable new customer
        self.labelNewCustomer = MyLabel(self)
        self.labelNewCustomer.setGeometry(100, 210, 100, 20)
        self.labelNewCustomer.setFont(font)
        self.labelNewCustomer.setText(u'新增客户')

        # lable my customer
        self.labelMyCustomer = QtGui.QLabel(self)
        self.labelMyCustomer.setGeometry(300, 210, 100, 20)
        self.labelMyCustomer.setFont(font)
        self.labelMyCustomer.setText(u'我的客户')

        # lable serch customer
        self.labelSearchCustomer = QtGui.QLabel(self)
        self.labelSearchCustomer.setGeometry(500, 210, 100, 20)
        self.labelSearchCustomer.setFont(font)
        self.labelSearchCustomer.setText(u'查找客户')

        # lable  customer
        self.labelHandoverCustomer = QtGui.QLabel(self)
        self.labelHandoverCustomer.setGeometry(700, 210, 100, 20)
        self.labelHandoverCustomer.setFont(font)
        self.labelHandoverCustomer.setText(u'交接客户')

        # lable  sale chance
        self.labelSaleChance = QtGui.QLabel(self)
        self.labelSaleChance.setGeometry(100, 410, 100, 20)
        self.labelSaleChance.setFont(font)
        self.labelSaleChance.setText(u'销售机会')

        # lable  tbd
        self.labeltbd1 = QtGui.QLabel(self)
        self.labeltbd1.setGeometry(300, 410, 100, 20)
        self.labeltbd1.setFont(font)
        self.labeltbd1.setText(u'  待定')

        # lable  tbd2
        self.labeltbd2 = QtGui.QLabel(self)
        self.labeltbd2.setGeometry(500, 410, 100, 20)
        self.labeltbd2.setFont(font)
        self.labeltbd2.setText(u'  待定')

        # lable  setting
        self.labelSetting = QtGui.QLabel(self)
        self.labelSetting.setGeometry(700, 410, 100, 20)
        self.labelSetting.setFont(font)
        self.labelSetting.setText(u'系统设置')

        #self.connect(self.labelNewCustomer, QtCore.SIGNAL('mousePress()'), QtGui.QMessageBox.question(self, 'Error', u"我的客户", QtGui.QMessageBox.Yes))
        #self.connect(self, QtCore.SIGNAL('mousePress()'), self, self.CheckMouseClickPosion())

    def CheckMouseClickPosion(self):
        print '111'







if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    form = MyMainWindow()
    form.show()
    app.exec_()