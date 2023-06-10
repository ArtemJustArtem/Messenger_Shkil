# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newuser.ui'
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

class Ui_NewUser(object):
    def setupUi(self, NewUser):
        if not NewUser.objectName():
            NewUser.setObjectName(u"NewUser")
        NewUser.resize(443, 186)
        self.label = QLabel(NewUser)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 30, 211, 16))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.name = QLineEdit(NewUser)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(70, 60, 311, 31))
        self.name.setFont(font)
        self.add = QPushButton(NewUser)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(150, 100, 141, 31))
        self.add.setFont(font)

        self.retranslateUi(NewUser)

        QMetaObject.connectSlotsByName(NewUser)
    # setupUi

    def retranslateUi(self, NewUser):
        NewUser.setWindowTitle(QCoreApplication.translate("NewUser", u"Form", None))
        self.label.setText(QCoreApplication.translate("NewUser", u"Enter the name of the user", None))
        self.name.setText("")
        self.add.setText(QCoreApplication.translate("NewUser", u"Add user", None))
    # retranslateUi

