

def wordWrap(text, width, height):
    text = text.replace("\n", " ")
    return text


print("hello world")
a = "hello"
a[0] = "a"
print(a)
# print(wordWrap("hello\nworld"))




# if "ісус навин" == "ісус навин":
#     print("alright")
# else:
#     print("adlkj")


























# # -*- coding: utf-8 -*-

# # Form implementation generated from reading ui file 'test.ui'
# #
# # Created by: PyQt5 UI code generator 5.15.4
# #
# # WARNING: Any manual changes made to this file will be lost when pyuic5 is
# # run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_testWindow(object):
#     def setupUi(self, testWindow):
#         testWindow.setObjectName("testWindow")
#         testWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(testWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(80, 480, 651, 61))
#         font = QtGui.QFont()
#         font.setPointSize(30)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setScaledContents(True)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setWordWrap(True)
#         self.label.setObjectName("label")
#         testWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(testWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
#         self.menubar.setObjectName("menubar")
#         testWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(testWindow)
#         self.statusbar.setObjectName("statusbar")
#         testWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(testWindow)
#         QtCore.QMetaObject.connectSlotsByName(testWindow)

#     def retranslateUi(self, testWindow):
#         _translate = QtCore.QCoreApplication.translate
#         testWindow.setWindowTitle(_translate("testWindow", "MainWindow"))
#         self.label.setText(_translate("testWindow", "TextLabel"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     testWindow = QtWidgets.QMainWindow()
#     ui = Ui_testWindow()
#     ui.setupUi(testWindow)
#     testWindow.show()
#     sys.exit(app.exec_())
