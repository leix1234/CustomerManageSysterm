 # -*- coding: UTF8 -*-
from PyQt4 import QtCore, QtGui
import sys
import os
import cPickle as p
from  MainWindow import MyMainWindow

_fromUtf8 = QtCore.QString.fromUtf8
userlistfile = '../config/userlist.dat'
#loginstylekey=['销售员',]
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class CWidgetLogin(QtGui.QWidget):
    def __init__(self):
        super(CWidgetLogin,self).__init__()
        self.resize(640,480)
        self.setup()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawPixmap(0, 0, 640, 480, QtGui.QPixmap("loginbackground.jpg"))
        painter.end()

    def setup(self):
        self.setWindowTitle(_fromUtf8('用户登录'))

        # lable login style
        self.labelLoginStyle = QtGui.QLabel(self)
        self.labelLoginStyle.setGeometry(QtCore.QRect(170, 170, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLoginStyle.setFont(font)
        self.labelLoginStyle.setText(_fromUtf8('登陆方式'))
        #lable username
        self.labelUsername = QtGui.QLabel(self)
        self.labelUsername.setGeometry(170, 210, 90, 24)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelUsername.setFont(font)
        self.labelUsername.setText(_fromUtf8('用户名'))
        #lable passwd
        self.labelPasswd = QtGui.QLabel(self)
        self.labelPasswd.setGeometry(170, 250, 90, 24)
        self.labelPasswd.setFont(font)
        self.labelPasswd.setText(_fromUtf8('密  码'))
        #combox login style
        self.comBoxLoginStyle = QtGui.QComboBox(self)
        self.comBoxLoginStyle.setGeometry(QtCore.QRect(260, 168, 150, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comBoxLoginStyle.setFont(font)
        self.comBoxLoginStyle.addItem(_fromUtf8("销售员"))
        self.comBoxLoginStyle.addItem(_fromUtf8("销售主管"))
        self.comBoxLoginStyle.addItem(_fromUtf8("销售总监"))
        self.comBoxLoginStyle.addItem(_fromUtf8("管理员"))
        #text username
        self.lineTextUser = QtGui.QLineEdit(self)
        self.lineTextUser.setGeometry(QtCore.QRect(260, 210, 150, 24))
        self.lineTextUser.setObjectName(_fromUtf8("lineTextUser"))
        # text passwd
        self.lineTextpasswd = QtGui.QLineEdit(self)
        self.lineTextpasswd.setGeometry(QtCore.QRect(260, 250, 150, 24))
        self.lineTextpasswd.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineTextpasswd.setObjectName(_fromUtf8("lineTextpasswd"))
        self.lineTextpasswd.setEchoMode(QtGui.QLineEdit.Password)
        #botton login
        self.pushBtnLogin = QtGui.QPushButton(self)
        self.pushBtnLogin.setGeometry(QtCore.QRect(175, 290, 235, 30))
        font.setPointSize(14)
        self.pushBtnLogin.setFont(font)
        #self.pushBtnLogin.setObjectName(_fromUtf8("pushBtnLogin"))
        self.pushBtnLogin.setText(_fromUtf8("登    陆"))

        self.connect(self.pushBtnLogin, QtCore.SIGNAL('clicked()'), self.DiaLoginfunc)

    def LoginCheck(self, userstyle, username, userpsswd):
        if False == os.path.isfile(userlistfile):
            print 'user %s is not registerd!', username

        f = file(userlistfile)
        userlist = p.load(f)
        f.close()
        print 'userlist:', userlist
        #print 'userlst[%s] = %s'%(username,userlist[username])
        if (username not in userlist.keys()):
            print 'user is not exist'
            QtGui.QMessageBox.question(self, 'Error', _fromUtf8("用户不存在"), QtGui.QMessageBox.Yes)
        elif userlist[username] == userpsswd:
            print 'login success'
            return True
        else:
            print 'passwd is error!'
            QtGui.QMessageBox.question(self, 'Error', _fromUtf8("用户名或密码错误"), QtGui.QMessageBox.Yes)
        return False

    def DiaLoginfunc(self):
        username = str(self.lineTextUser.text())
        passwd = str(self.lineTextpasswd.text())
        #loginstyle = str(self.comBoxLoginStyle.itemText(3))
        print 'username:', str(self.lineTextUser.text())
        print 'passwd  :', str(self.lineTextpasswd.text())
        #print '\n login style ：', _fromUtf8(self.comBoxLoginStyle.itemText(self.comBoxLoginStyle.currentIndex()))
        if self.comBoxLoginStyle.currentIndex() == 0 : #销售员
            print u"销售员"
        elif self.comBoxLoginStyle.currentIndex() == 1: #销售主管
            print u"销售主管"
        elif self.comBoxLoginStyle.currentIndex() == 2: #销售主管
            print u"销售总监"
        elif self.comBoxLoginStyle.currentIndex() == 3: #销售主管
            print u"管理员"

        if True == self.LoginCheck(1, username, passwd) :
            mainwindow1.show()
            self.hide()

        #QtGui.QApplication.quit()

    def DiaRegisterfunc(self):
        print 'register a new user'

app = QtGui.QApplication(sys.argv)
form = CWidgetLogin()
mainwindow1 = MyMainWindow()
form.show()
app.exec_()
