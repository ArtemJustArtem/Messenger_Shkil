# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Chat(object):
    def setupUi(self, Chat):
        if not Chat.objectName():
            Chat.setObjectName(u"Chat")
        Chat.resize(420, 492)
        self.greeting = QLabel(Chat)
        self.greeting.setObjectName(u"greeting")
        self.greeting.setGeometry(QRect(20, 10, 231, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.greeting.setFont(font)
        self.label_2 = QLabel(Chat)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 60, 281, 21))
        self.label_2.setFont(font)
        self.user_to = QLineEdit(Chat)
        self.user_to.setObjectName(u"user_to")
        self.user_to.setGeometry(QRect(20, 90, 281, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.user_to.setFont(font1)
        self.open = QPushButton(Chat)
        self.open.setObjectName(u"open")
        self.open.setGeometry(QRect(310, 90, 91, 31))
        self.open.setFont(font)
        self.chat = QPlainTextEdit(Chat)
        self.chat.setObjectName(u"chat")
        self.chat.setGeometry(QRect(20, 130, 381, 301))
        self.chat.setFont(font1)
        self.chat.setReadOnly(True)
        self.message_enter = QPlainTextEdit(Chat)
        self.message_enter.setObjectName(u"message_enter")
        self.message_enter.setGeometry(QRect(20, 440, 301, 41))
        self.message_enter.setFont(font1)
        self.send = QPushButton(Chat)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(330, 440, 71, 41))
        self.send.setFont(font)
        self.open_2 = QPushButton(Chat)
        self.open_2.setObjectName(u"open_2")
        self.open_2.setGeometry(QRect(260, 10, 141, 31))
        self.open_2.setFont(font)

        self.retranslateUi(Chat)

        QMetaObject.connectSlotsByName(Chat)
    # setupUi

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(QCoreApplication.translate("Chat", u"Chat", None))
        self.greeting.setText(QCoreApplication.translate("Chat", u"Hello, ", None))
        self.label_2.setText(QCoreApplication.translate("Chat", u"To open chat, please enter username", None))
        self.user_to.setText("")
        self.open.setText(QCoreApplication.translate("Chat", u"Open", None))
        self.chat.setPlainText("")
        self.message_enter.setPlainText("")
        self.send.setText(QCoreApplication.translate("Chat", u"Send", None))
        self.open_2.setText(QCoreApplication.translate("Chat", u"Change account", None))
    # retranslateUi

