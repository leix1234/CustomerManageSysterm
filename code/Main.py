#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Login_new import CWidgetLogin
from PyQt4.QtGui import QApplication, QDialog


DialoginApp = QApplication(sys.argv)
window = QDialog()
ui = CWidgetLogin()
#ui.setup()
window.show()
sys.exit(DialoginApp.exec_())

