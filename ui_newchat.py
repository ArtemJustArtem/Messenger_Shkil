# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newchat.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_NewChat(object):
    def setupUi(self, NewChat):
        if not NewChat.objectName():
            NewChat.setObjectName(u"NewChat")
        NewChat.resize(443, 186)
        self.label = QLabel(NewChat)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 30, 211, 16))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.name = QLineEdit(NewChat)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(70, 60, 311, 31))
        self.name.setFont(font)
        self.create_chat = QPushButton(NewChat)
        self.create_chat.setObjectName(u"create_chat")
        self.create_chat.setGeometry(QRect(150, 100, 141, 31))
        self.create_chat.setFont(font)

        self.retranslateUi(NewChat)

        QMetaObject.connectSlotsByName(NewChat)
    # setupUi

    def retranslateUi(self, NewChat):
        NewChat.setWindowTitle(QCoreApplication.translate("NewChat", u"Form", None))
        self.label.setText(QCoreApplication.translate("NewChat", u"Enter the name of the chat", None))
        self.name.setText("")
        self.create_chat.setText(QCoreApplication.translate("NewChat", u"Create chat", None))
    # retranslateUi

