# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledRsIoCI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 450)
        MainWindow.setMinimumSize(QSize(450, 450))
        MainWindow.setMaximumSize(QSize(450, 450))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_menu = QFrame(self.centralwidget)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setMaximumSize(QSize(16777215, 45))
        self.top_menu.setStyleSheet(u"background-color: rgb(135, 206, 255);")
        self.top_menu.setFrameShape(QFrame.NoFrame)
        self.top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_3 = QFrame(self.top_menu)
        self.left_menu_3.setObjectName(u"left_menu_3")
        self.left_menu_3.setMinimumSize(QSize(50, 0))
        self.left_menu_3.setMaximumSize(QSize(50, 16777215))
        self.left_menu_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"")
        self.left_menu_3.setFrameShape(QFrame.NoFrame)
        self.left_menu_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.left_menu_3)

        self.left_menu_2 = QFrame(self.top_menu)
        self.left_menu_2.setObjectName(u"left_menu_2")
        self.left_menu_2.setMaximumSize(QSize(16777215, 16777215))
        self.left_menu_2.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(2,0,36,1), stop:0.30 rgba(9,9,121,1), stop:0.80 rgba(0,212,255,1), stop:1 rgba(0, 0, 0, 0));\n"
"}")
        self.left_menu_2.setFrameShape(QFrame.NoFrame)
        self.left_menu_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.left_menu_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 401, 41))
        font = QFont()
        font.setFamily(u"Segoe UI Variable Text Semibold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: white;\n"
"font: 63 20pt \"Segoe UI Variable Text Semibold\";")
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setIndent(-1)
        self.label_3.setOpenExternalLinks(False)

        self.horizontalLayout_2.addWidget(self.left_menu_2)


        self.verticalLayout.addWidget(self.top_menu)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.content)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(50, 0))
        self.left_menu.setMaximumSize(QSize(50, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.left_menu)

        self.content_right = QFrame(self.content)
        self.content_right.setObjectName(u"content_right")
        self.content_right.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.content_right.setFrameShape(QFrame.NoFrame)
        self.content_right.setFrameShadow(QFrame.Raised)
        self.lsegundo = QSpinBox(self.content_right)
        self.lsegundo.setObjectName(u"lsegundo")
        self.lsegundo.setGeometry(QRect(300, 30, 81, 31))
        self.lsegundo.setStyleSheet(u"QSpinBox {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"	font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.lsegundo.setAlignment(Qt.AlignCenter)
        self.lsegundo.setAccelerated(True)
        self.label = QLabel(self.content_right)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 251, 31))
        self.label.setStyleSheet(u"color: white;\n"
"font: 75 8pt \"System\";")
        self.label_2 = QLabel(self.content_right)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 261, 31))
        self.label_2.setStyleSheet(u"color: white;\n"
"font: 75 8pt \"System\";")
        self.pushButton = QPushButton(self.content_right)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 330, 361, 51))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(2,0,36,1), stop:0.30 rgba(9,9,121,1), stop:0.80 rgba(0,212,255,1), stop:1 rgba(0, 0, 0, 0));\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	font: 63 26pt \"Segoe UI Variable Text Semibold\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(2,0,36,1), stop:0.30 rgba(0,0,0,1), stop:0.80 rgba(0,212,255,1), stop:1 rgba(0, 0, 0, 0));\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	font: 63 26pt \"Segoe UI Variable Text Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(113,0,0,1), stop:0.30 rgba(45,53,55,1), stop:0.80 rgba(0,212,255,1), stop:1 rgba(0,212,255,1));\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	font: 63 26pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.lmsg1 = QLineEdit(self.content_right)
        self.lmsg1.setObjectName(u"lmsg1")
        self.lmsg1.setGeometry(QRect(20, 170, 361, 41))
        self.lmsg1.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	font: 63 18pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.lmsg1.setAlignment(Qt.AlignCenter)
        self.lmsg2 = QLineEdit(self.content_right)
        self.lmsg2.setObjectName(u"lmsg2")
        self.lmsg2.setGeometry(QRect(20, 210, 361, 41))
        self.lmsg2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 1px;\n"
"	color: white;\n"
"	font: 63 18pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.lmsg2.setAlignment(Qt.AlignCenter)
        self.lmsg3 = QLineEdit(self.content_right)
        self.lmsg3.setObjectName(u"lmsg3")
        self.lmsg3.setGeometry(QRect(20, 250, 361, 41))
        self.lmsg3.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	font: 63 18pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.lmsg3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.content_right)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 130, 361, 31))
        self.label_4.setStyleSheet(u"color: white;\n"
"font: 75 10pt \"System\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.lmeta = QLineEdit(self.content_right)
        self.lmeta.setObjectName(u"lmeta")
        self.lmeta.setGeometry(QRect(300, 80, 81, 31))
        self.lmeta.setStyleSheet(u"QLineEdit {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"	font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.lmeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.content_right)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"COTA\u00c7\u00c3O DO EURO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o do Euro", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Atualizar em quantos segundos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Valor que voc\u00ea quer ser alertado", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RESULTADO", None))
    # retranslateUi

