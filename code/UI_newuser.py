# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newuser.ui'
#
# Created: Wed Mar 21 23:56:17 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

CountryList = ['中国','印度','俄罗斯','印度尼西亚','菲律宾']

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

class Ui_Dialog(QtGui.QWidget):
    def setupUi(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(690, 1024)
        self.setSizeIncrement(QtCore.QSize(25, 21))
        self.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setFont(font)
        #名称
        self.labelCustomerName = QtGui.QLabel(self)
        self.labelCustomerName.setGeometry(QtCore.QRect(42, 22, 90, 19))
        self.labelCustomerName.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerName.setFont(font)
        self.labelCustomerName.setObjectName(_fromUtf8("labelCustomerName"))
        self.lineEditCustomerName = QtGui.QLineEdit(self)
        self.lineEditCustomerName.setGeometry(QtCore.QRect(160, 15, 441, 31))
        self.lineEditCustomerName.setSizeIncrement(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCustomerName.setFont(font)
        self.lineEditCustomerName.setText(_fromUtf8(""))
        self.lineEditCustomerName.setObjectName(_fromUtf8("lineEditCustomerName"))
        #简称
        self.labelCustomerAbbreviation = QtGui.QLabel(self)
        self.labelCustomerAbbreviation.setGeometry(QtCore.QRect(40, 80, 90, 19))
        self.labelCustomerAbbreviation.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerAbbreviation.setFont(font)
        self.labelCustomerAbbreviation.setObjectName(_fromUtf8("labelCustomerAbbreviation"))
        self.lineEditCustomerAbbreviation = QtGui.QLineEdit(self)
        self.lineEditCustomerAbbreviation.setGeometry(QtCore.QRect(160, 70, 441, 31))
        self.lineEditCustomerAbbreviation.setSizeIncrement(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCustomerAbbreviation.setFont(font)
        self.lineEditCustomerAbbreviation.setText(_fromUtf8(""))
        self.lineEditCustomerAbbreviation.setObjectName(_fromUtf8("lineEditCustomerAbbreviation"))
        #联系方式
        self.lineEditCustomerTel1 = QtGui.QLineEdit(self)
        self.lineEditCustomerTel1.setGeometry(QtCore.QRect(160, 130, 211, 31))
        self.lineEditCustomerTel1.setSizeIncrement(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCustomerTel1.setFont(font)
        self.lineEditCustomerTel1.setText(_fromUtf8(""))
        self.lineEditCustomerTel1.setObjectName(_fromUtf8("lineEditCustomerTel1"))
        self.labelCustomerTel = QtGui.QLabel(self)
        self.labelCustomerTel.setGeometry(QtCore.QRect(40, 140, 90, 19))
        self.labelCustomerTel.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerTel.setFont(font)
        self.labelCustomerTel.setObjectName(_fromUtf8("labelCustomerTel"))
        self.lineEditCustomerTel2 = QtGui.QLineEdit(self)
        self.lineEditCustomerTel2.setGeometry(QtCore.QRect(390, 130, 211, 31))
        self.lineEditCustomerTel2.setSizeIncrement(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCustomerTel2.setFont(font)
        self.lineEditCustomerTel2.setText(_fromUtf8(""))
        self.lineEditCustomerTel2.setObjectName(_fromUtf8("lineEditCustomerTel2"))
        self.labelCustomerState = QtGui.QLabel(self)
        self.labelCustomerState.setGeometry(QtCore.QRect(40, 198, 90, 21))
        self.labelCustomerState.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerState.setFont(font)
        self.labelCustomerState.setObjectName(_fromUtf8("labelCustomerState"))
        self.comboBoxCustomerState = QtGui.QComboBox(self)
        self.comboBoxCustomerState.setGeometry(QtCore.QRect(160, 191, 211, 31))
        self.comboBoxCustomerState.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxCustomerState.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxCustomerState.setFont(font)
        self.comboBoxCustomerState.setObjectName(_fromUtf8("comboBoxCustomerState"))
        self.comboBoxCustomerState.addItem(_fromUtf8(""))
        self.comboBoxCustomerState.addItem(_fromUtf8(""))
        self.comboBoxCustomerState.addItem(_fromUtf8(""))
        self.comboBoxCustomerState.addItem(_fromUtf8(""))
        self.comboBoxCustomerState.addItem(_fromUtf8(""))
        self.comboBoxCustomerState.addItem(_fromUtf8(""))
        self.comboBoxCustomerState.addItem(_fromUtf8(""))
        self.labelCustomerType = QtGui.QLabel(self)
        self.labelCustomerType.setGeometry(QtCore.QRect(40, 260, 90, 21))
        self.labelCustomerType.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerType.setFont(font)
        self.labelCustomerType.setObjectName(_fromUtf8("labelCustomerType"))
        self.labelCustomerGrade = QtGui.QLabel(self)
        self.labelCustomerGrade.setGeometry(QtCore.QRect(40, 320, 90, 21))
        self.labelCustomerGrade.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerGrade.setFont(font)
        self.labelCustomerGrade.setObjectName(_fromUtf8("labelCustomerGrade"))
        self.comboBoxCustomerType = QtGui.QComboBox(self)
        self.comboBoxCustomerType.setGeometry(QtCore.QRect(160, 250, 211, 31))
        self.comboBoxCustomerType.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxCustomerType.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxCustomerType.setFont(font)
        self.comboBoxCustomerType.setObjectName(_fromUtf8("comboBoxCustomerType"))
        self.comboBoxCustomerType.addItem(_fromUtf8(""))
        self.comboBoxCustomerType.addItem(_fromUtf8(""))
        self.comboBoxCustomerType.addItem(_fromUtf8(""))
        self.comboBoxCustomerType.addItem(_fromUtf8(""))
        self.comboBoxCustomerGrade = QtGui.QComboBox(self)
        self.comboBoxCustomerGrade.setGeometry(QtCore.QRect(160, 310, 211, 31))
        self.comboBoxCustomerGrade.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxCustomerGrade.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxCustomerGrade.setFont(font)
        self.comboBoxCustomerGrade.setObjectName(_fromUtf8("comboBoxCustomerGrade"))
        self.comboBoxCustomerGrade.addItem(_fromUtf8(""))
        self.comboBoxCustomerGrade.addItem(_fromUtf8(""))
        self.comboBoxCustomerGrade.addItem(_fromUtf8(""))
        self.comboBoxCustomerGrade.addItem(_fromUtf8(""))
        self.labelImportance = QtGui.QLabel(self)
        self.labelImportance.setGeometry(QtCore.QRect(40, 380, 90, 21))
        self.labelImportance.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelImportance.setFont(font)
        self.labelImportance.setObjectName(_fromUtf8("labelImportance"))
        self.radioButtonImportance1 = QtGui.QRadioButton(self)
        self.radioButtonImportance1.setGeometry(QtCore.QRect(160, 380, 89, 21))
        self.radioButtonImportance1.setObjectName(_fromUtf8("radioButtonImportance1"))
        self.radioButtonImportance2 = QtGui.QRadioButton(self)
        self.radioButtonImportance2.setGeometry(QtCore.QRect(250, 380, 89, 21))
        self.radioButtonImportance2.setObjectName(_fromUtf8("radioButtonImportance2"))
        self.radioButtonImportance3 = QtGui.QRadioButton(self)
        self.radioButtonImportance3.setGeometry(QtCore.QRect(340, 380, 111, 21))
        self.radioButtonImportance3.setObjectName(_fromUtf8("radioButtonImportance3"))
        self.labelCustomerBirthday = QtGui.QLabel(self)
        self.labelCustomerBirthday.setGeometry(QtCore.QRect(40, 440, 90, 21))
        self.labelCustomerBirthday.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerBirthday.setFont(font)
        self.labelCustomerBirthday.setObjectName(_fromUtf8("labelCustomerBirthday"))
        self.dateEditCustomerBirthday = QtGui.QDateEdit(self)
        self.dateEditCustomerBirthday.setGeometry(QtCore.QRect(160, 430, 211, 31))
        self.dateEditCustomerBirthday.setBaseSize(QtCore.QSize(25, 21))
        self.dateEditCustomerBirthday.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dateEditCustomerBirthday.setDateTime(QtCore.QDateTime(QtCore.QDate(1950, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditCustomerBirthday.setCalendarPopup(True)
        self.dateEditCustomerBirthday.setObjectName(_fromUtf8("dateEditCustomerBirthday"))
        #国家
        self.labelCountry = QtGui.QLabel(self)
        self.labelCountry.setGeometry(QtCore.QRect(70, 500, 50, 21))
        self.labelCountry.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCountry.setFont(font)
        self.labelCountry.setObjectName(_fromUtf8("labelCountry"))
        self.comboBoxCustomerGrade_2 = QtGui.QComboBox(self)
        self.comboBoxCustomerGrade_2.setGeometry(QtCore.QRect(160, 490, 181, 31))
        self.comboBoxCustomerGrade_2.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxCustomerGrade_2.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxCustomerGrade_2.setFont(font)
        self.comboBoxCustomerGrade_2.setObjectName(_fromUtf8("comboBoxCustomerGrade_2"))
        #self.comboBoxCustomerGrade_2.addItem(_fromUtf8( "---请选择---"))
        for countrylistvar in CountryList:
            self.comboBoxCustomerGrade_2.addItem(_fromUtf8(countrylistvar))

        #区域
        self.labelArea = QtGui.QLabel(self)
        self.labelArea.setGeometry(QtCore.QRect(370, 500, 50, 21))
        self.labelArea.setSizeIncrement(QtCore.QSize(20, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelArea.setFont(font)
        self.labelArea.setObjectName(_fromUtf8("labelArea"))
        self.labelArea.setText(_translate("Dialog", "区域", None))
        self.comboBoxArea = QtGui.QComboBox(self)
        self.comboBoxArea.setGeometry(QtCore.QRect(430, 490, 181, 31))
        self.comboBoxArea.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxArea.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxArea.setFont(font)
        self.comboBoxArea.setObjectName(_fromUtf8("comboBoxArea"))
        self.comboBoxArea.addItem(_fromUtf8("---请选择---"))
        self.comboBoxArea.addItem(_fromUtf8("华东"))
        self.comboBoxArea.addItem(_fromUtf8("华南"))
        self.comboBoxArea.addItem(_fromUtf8("中部"))
        self.comboBoxArea.addItem(_fromUtf8("东北"))

        #详细地址
        self.labelCustomerAddress = QtGui.QLabel(self)
        self.labelCustomerAddress.setGeometry(QtCore.QRect(40, 560, 90, 21))
        self.labelCustomerAddress.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerAddress.setFont(font)
        self.labelCustomerAddress.setObjectName(_fromUtf8("labelCustomerAddress"))
        self.comboBoxProvince = QtGui.QComboBox(self)
        self.comboBoxProvince.setGeometry(QtCore.QRect(160, 550, 131, 31))
        self.comboBoxProvince.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxProvince.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxProvince.setFont(font)
        self.comboBoxProvince.setObjectName(_fromUtf8("comboBoxProvince"))
        self.comboBoxProvince.addItem(_fromUtf8(""))
        self.comboBoxProvince.addItem(_fromUtf8(""))
        self.comboBoxProvince.addItem(_fromUtf8(""))
        self.comboBoxProvince.addItem(_fromUtf8(""))
        self.comboBoxCity = QtGui.QComboBox(self)
        self.comboBoxCity.setGeometry(QtCore.QRect(310, 550, 131, 31))
        self.comboBoxCity.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxCity.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxCity.setFont(font)
        self.comboBoxCity.setObjectName(_fromUtf8("comboBoxCity"))
        self.comboBoxCity.addItem(_fromUtf8(""))
        self.comboBoxCity.addItem(_fromUtf8(""))
        self.comboBoxCity.addItem(_fromUtf8(""))
        self.comboBoxCity.addItem(_fromUtf8(""))
        self.comboBoxCounty = QtGui.QComboBox(self)
        self.comboBoxCounty.setGeometry(QtCore.QRect(460, 550, 141, 31))
        self.comboBoxCounty.setSizeIncrement(QtCore.QSize(25, 21))
        self.comboBoxCounty.setBaseSize(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxCounty.setFont(font)
        self.comboBoxCounty.setObjectName(_fromUtf8("comboBoxCounty"))
        self.comboBoxCounty.addItem(_fromUtf8(""))
        self.comboBoxCounty.addItem(_fromUtf8(""))
        self.comboBoxCounty.addItem(_fromUtf8(""))
        self.comboBoxCounty.addItem(_fromUtf8(""))
        self.lineEditAddress = QtGui.QLineEdit(self)
        self.lineEditAddress.setGeometry(QtCore.QRect(160, 600, 441, 31))
        self.lineEditAddress.setSizeIncrement(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditAddress.setFont(font)
        self.lineEditAddress.setObjectName(_fromUtf8("lineEditAddress"))
        self.labelCustomerProfile = QtGui.QLabel(self)
        self.labelCustomerProfile.setGeometry(QtCore.QRect(50, 670, 90, 21))
        self.labelCustomerProfile.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCustomerProfile.setFont(font)
        self.labelCustomerProfile.setObjectName(_fromUtf8("labelCustomerProfile"))
        self.textEditCustomerProfile = QtGui.QTextEdit(self)
        self.textEditCustomerProfile.setGeometry(QtCore.QRect(160, 660, 441, 81))
        self.textEditCustomerProfile.setObjectName(_fromUtf8("textEditCustomerProfile"))
        self.labelCreater = QtGui.QLabel(self)
        self.labelCreater.setGeometry(QtCore.QRect(60, 780, 90, 21))
        self.labelCreater.setSizeIncrement(QtCore.QSize(25, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCreater.setFont(font)
        self.labelCreater.setObjectName(_fromUtf8("labelCreater"))
        self.lineEditCreater = QtGui.QLineEdit(self)
        self.lineEditCreater.setGeometry(QtCore.QRect(160, 770, 441, 31))
        self.lineEditCreater.setSizeIncrement(QtCore.QSize(25, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditCreater.setFont(font)
        self.lineEditCreater.setText(_fromUtf8(""))
        self.lineEditCreater.setObjectName(_fromUtf8("lineEditCreater"))
        self.pushButtonConfirm = QtGui.QPushButton(self)
        self.pushButtonConfirm.setGeometry(QtCore.QRect(270, 870, 75, 31))
        self.pushButtonConfirm.setObjectName(_fromUtf8("pushButtonConfirm"))
        self.pushButtonCancel = QtGui.QPushButton(self)
        self.pushButtonCancel.setGeometry(QtCore.QRect(450, 870, 75, 31))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.verticalScrollBar = QtGui.QScrollBar(self)
        self.verticalScrollBar.setGeometry(QtCore.QRect(780, 0, 20, 941))
        self.verticalScrollBar.setAutoFillBackground(False)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setInvertedAppearance(False)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.connect(self.pushButtonConfirm, QtCore.SIGNAL('clicked()'), self.ConfirmFunc)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelCustomerName.setText(_translate("Dialog", "客户名称", None))
        self.labelCustomerAbbreviation.setText(_translate("Dialog", "客户简称", None))
        self.labelCustomerTel.setText(_translate("Dialog", "客户电话", None))
        self.labelCustomerState.setText(_translate("Dialog", "客户状态", None))
        self.comboBoxCustomerState.setItemText(0, _translate("Dialog", "---请选择---", None))
        self.comboBoxCustomerState.setItemText(1, _translate("Dialog", "潜在客户", None))
        self.comboBoxCustomerState.setItemText(2, _translate("Dialog", "初步接触", None))
        self.comboBoxCustomerState.setItemText(3, _translate("Dialog", "持续跟进", None))
        self.comboBoxCustomerState.setItemText(4, _translate("Dialog", "成交客户", None))
        self.comboBoxCustomerState.setItemText(5, _translate("Dialog", "忠诚客户", None))
        self.comboBoxCustomerState.setItemText(6, _translate("Dialog", "无效客户", None))
        self.labelCustomerType.setText(_translate("Dialog", "客户性质", None))
        self.labelCustomerGrade.setText(_translate("Dialog", "客户分级", None))
        self.comboBoxCustomerType.setItemText(0, _translate("Dialog", "---请选择---", None))
        self.comboBoxCustomerType.setItemText(1, _translate("Dialog", "企业客户", None))
        self.comboBoxCustomerType.setItemText(2, _translate("Dialog", "个人客户", None))
        self.comboBoxCustomerType.setItemText(3, _translate("Dialog", "政府事业单位", None))
        self.comboBoxCustomerGrade.setItemText(0, _translate("Dialog", "---请选择---", None))
        self.comboBoxCustomerGrade.setItemText(1, _translate("Dialog", "小型", None))
        self.comboBoxCustomerGrade.setItemText(2, _translate("Dialog", "中型", None))
        self.comboBoxCustomerGrade.setItemText(3, _translate("Dialog", "大型", None))
        self.labelImportance.setText(_translate("Dialog", "重要程度", None))
        self.radioButtonImportance1.setText(_translate("Dialog", "一般", None))
        self.radioButtonImportance2.setText(_translate("Dialog", "重要", None))
        self.radioButtonImportance3.setText(_translate("Dialog", "非常重要", None))
        self.labelCustomerBirthday.setText(_translate("Dialog", "客户生日", None))
        self.dateEditCustomerBirthday.setDisplayFormat(_translate("Dialog", "yyyy年M月d日", None))
        self.labelCountry.setText(_translate("Dialog", "国家", None))

        self.labelCustomerAddress.setText(_translate("Dialog", "客户地址", None))
        self.comboBoxProvince.setItemText(0, _translate("Dialog", "请选择省份", None))
        self.comboBoxProvince.setItemText(1, _translate("Dialog", "小型", None))
        self.comboBoxProvince.setItemText(2, _translate("Dialog", "中型", None))
        self.comboBoxProvince.setItemText(3, _translate("Dialog", "大型", None))
        self.comboBoxCity.setItemText(0, _translate("Dialog", "请选择城市", None))
        self.comboBoxCity.setItemText(1, _translate("Dialog", "小型", None))
        self.comboBoxCity.setItemText(2, _translate("Dialog", "中型", None))
        self.comboBoxCity.setItemText(3, _translate("Dialog", "大型", None))
        self.comboBoxCounty.setItemText(0, _translate("Dialog", "请选择区县", None))
        self.comboBoxCounty.setItemText(1, _translate("Dialog", "2", None))
        self.comboBoxCounty.setItemText(2, _translate("Dialog", "3", None))
        self.comboBoxCounty.setItemText(3, _translate("Dialog", "4", None))
        self.lineEditAddress.setText(_translate("Dialog", "所在的街道/村镇及门牌号", None))
        self.labelCustomerProfile.setText(_translate("Dialog", "客户简介", None))
        self.labelCreater.setText(_translate("Dialog", "创建人", None))
        self.pushButtonConfirm.setText(_translate("Dialog", "确认", None))
        self.pushButtonCancel.setText(_translate("Dialog", "取消", None))

    def ConfirmFunc(self):
        print 'confirm clicked!'
        print "customer name:", str(self.lineEditCustomerName.text())
        print "customer ", str(self.lineEditCustomerAbbreviation.text())
        print "customer tel1", str(self.lineEditCustomerTel1.text())
        print "customer tel2", str(self.lineEditCustomerTel2.text())



if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    form = Ui_Dialog()
    form.setupUi()
    form.show()
    app.exec_()