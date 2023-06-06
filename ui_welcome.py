# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
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

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if not Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(449, 190)
        self.label = QLabel(Welcome)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 291, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.username = QLineEdit(Welcome)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(70, 70, 311, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.username.setFont(font1)
        self.join = QPushButton(Welcome)
        self.join.setObjectName(u"join")
        self.join.setGeometry(QRect(160, 110, 131, 31))
        self.join.setFont(font)

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"Welcome", None))
        self.label.setText(QCoreApplication.translate("Welcome", u"Welcome, please enter your username", None))
        self.username.setText("")
        self.join.setText(QCoreApplication.translate("Welcome", u"Join", None))
    # retranslateUi

