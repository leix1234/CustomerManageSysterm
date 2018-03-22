# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created: Sun Feb 18 20:47:39 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
import cPickle as p
import os


userlistfile = './config/userlist.dat'
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DiaLogin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_DiaLogin, self).__init__(parent)
        self.resize(640, 480)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.Qt.NoPen)
        painter.drawPixmap(0, 0, 640, 480, QtGui.QPixmap("loginbackground.jpg"))
        painter.end()

    #def drawBrushes(self, qp):
     #   print 'paintEvent'
      #  brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
       # qp.setBrush(brush)
        #qp.drawRect(10, 15, 90, 60)

    def setupUi(self, DiaLogin):
        DiaLogin.setObjectName(_fromUtf8("DiaLogin"))
        DiaLogin.resize(640, 480)
        self.labelUsername = QtGui.QLabel(DiaLogin)
        self.labelUsername.setGeometry(QtCore.QRect(173, 210, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUsername.setFont(font)

        #qp = QtGui.QPainter()

        #qp.begin(self)

        #qp.end()
        #self.background = QtGui.QPalette(self)
        #print str(QtGui.QPixmap('loginbackground.jpg'))
        #self.background.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('loginbackground.jpg')))
        #self.background.setBrush(QtGui.QPalette.Background, QtCore.Qt.DiagCrossPattern)

        self.labelUsername.setObjectName(_fromUtf8("labelUsername"))
        self.labelPasswd = QtGui.QLabel(DiaLogin)
        self.labelPasswd.setGeometry(QtCore.QRect(173, 240, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPasswd.setFont(font)
        self.labelPasswd.setObjectName(_fromUtf8("labelPasswd"))
        self.lineTextUser = QtGui.QLineEdit(DiaLogin)
        self.lineTextUser.setGeometry(QtCore.QRect(260, 207, 150, 24))
        self.lineTextUser.setObjectName(_fromUtf8("lineTextUser"))
        self.lineTextpasswd = QtGui.QLineEdit(DiaLogin)
        self.lineTextpasswd.setGeometry(QtCore.QRect(260, 235, 150, 24))
        self.lineTextpasswd.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineTextpasswd.setObjectName(_fromUtf8("lineTextpasswd"))
        self.lineTextpasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.labelLoginStyle = QtGui.QLabel(DiaLogin)
        self.labelLoginStyle.setGeometry(QtCore.QRect(173, 174, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLoginStyle.setFont(font)
        self.labelLoginStyle.setObjectName(_fromUtf8("labelLoginStyle"))
        self.pushBtnLogin = QtGui.QPushButton(DiaLogin)
        self.pushBtnLogin.setGeometry(QtCore.QRect(175, 290, 235, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushBtnLogin.setFont(font)
        self.pushBtnLogin.setObjectName(_fromUtf8("pushBtnLogin"))
        #self.pushBtnRegist = QtGui.QPushButton(DiaLogin)
        #self.pushBtnRegist.setGeometry(QtCore.QRect(320, 310, 95, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        #self.pushBtnRegist.setFont(font)
        #self.pushBtnRegist.setObjectName(_fromUtf8("pushBtnRegist"))
        self.comBoxLoginStyle = QtGui.QComboBox(DiaLogin)
        self.comBoxLoginStyle.setGeometry(QtCore.QRect(260, 174, 150, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comBoxLoginStyle.setFont(font)
        self.comBoxLoginStyle.setObjectName(_fromUtf8("comBoxLoginStyle"))
        self.comBoxLoginStyle.addItem(_fromUtf8(""))
        self.comBoxLoginStyle.addItem(_fromUtf8(""))
        self.comBoxLoginStyle.addItem(_fromUtf8(""))
        self.comBoxLoginStyle.addItem(_fromUtf8(""))

        self.connect(self.pushBtnLogin, QtCore.SIGNAL('clicked()'), self.DiaLoginfunc)

        self.retranslateUi(DiaLogin)
        QtCore.QMetaObject.connectSlotsByName(DiaLogin)

    def retranslateUi(self, DiaLogin):
        DiaLogin.setWindowTitle(_translate("DiaLogin", "登录", None))
        self.labelUsername.setText(_translate("DiaLogin", "用户名", None))
        self.labelPasswd.setText(_translate("DiaLogin", "密  码", None))
        self.labelLoginStyle.setText(_translate("DiaLogin", "登录方式", None))
        self.pushBtnLogin.setText(_translate("DiaLogin", "登     录", None))
        #self.pushBtnRegist.setText(_translate("DiaLogin", "取消", None))
        self.comBoxLoginStyle.setItemText(0, _translate("DiaLogin", "销售员", None))
        self.comBoxLoginStyle.setItemText(1, _translate("DiaLogin", "销售主管", None))
        self.comBoxLoginStyle.setItemText(2, _translate("DiaLogin", "销售总监", None))
        self.comBoxLoginStyle.setItemText(3, _translate("DiaLogin", "管理员", None))

    def LoginCheck(self, userstyle, username, userpsswd):
        if False == os.path.isfile(userlistfile):
            print 'user %s is not registerd!', username

        f = file(userlistfile)
        userlist = p.load(f)
        f.close()
        print 'userlist:', userlist
        if userlist[username] == userpsswd:
            print 'login success'
        else:
            print 'passwd is error!'


    def DiaLoginfunc(self):
        username = str(self.lineTextUser.text())
        passwd = str(self.lineTextpasswd.text())
        print 'username:', str(self.lineTextUser.text())
        print 'passwd  :', str(self.lineTextpasswd.text())
        self.LoginCheck(1, username, passwd)


        QtGui.QApplication.quit()
        #self.close()

    def DiaRegisterfunc(self):
        print 'register a new user'







