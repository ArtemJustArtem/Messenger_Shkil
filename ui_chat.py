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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Chat(object):
    def setupUi(self, Chat):
        if not Chat.objectName():
            Chat.setObjectName(u"Chat")
        Chat.resize(651, 492)
        self.greeting = QLabel(Chat)
        self.greeting.setObjectName(u"greeting")
        self.greeting.setGeometry(QRect(20, 10, 231, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.greeting.setFont(font)
        self.chat = QPlainTextEdit(Chat)
        self.chat.setObjectName(u"chat")
        self.chat.setGeometry(QRect(20, 50, 381, 381))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
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
        self.change = QPushButton(Chat)
        self.change.setObjectName(u"change")
        self.change.setGeometry(QRect(500, 10, 141, 31))
        self.change.setFont(font)
        self.new_chat = QPushButton(Chat)
        self.new_chat.setObjectName(u"new_chat")
        self.new_chat.setGeometry(QRect(410, 440, 111, 41))
        self.new_chat.setFont(font)
        self.add_user = QPushButton(Chat)
        self.add_user.setObjectName(u"add_user")
        self.add_user.setGeometry(QRect(530, 440, 111, 41))
        self.add_user.setFont(font)
        self.chat_list = QListWidget(Chat)
        self.chat_list.setObjectName(u"chat_list")
        self.chat_list.setGeometry(QRect(410, 90, 231, 341))
        self.chat_list.setFont(font)
        self.greeting_2 = QLabel(Chat)
        self.greeting_2.setObjectName(u"greeting_2")
        self.greeting_2.setGeometry(QRect(500, 50, 51, 31))
        self.greeting_2.setFont(font)

        self.retranslateUi(Chat)

        QMetaObject.connectSlotsByName(Chat)
    # setupUi

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(QCoreApplication.translate("Chat", u"Chat", None))
        self.greeting.setText(QCoreApplication.translate("Chat", u"Hello, ", None))
        self.chat.setPlainText("")
        self.message_enter.setPlainText("")
        self.send.setText(QCoreApplication.translate("Chat", u"Send", None))
        self.change.setText(QCoreApplication.translate("Chat", u"Change account", None))
        self.new_chat.setText(QCoreApplication.translate("Chat", u"New chat", None))
        self.add_user.setText(QCoreApplication.translate("Chat", u"Add user", None))
        self.greeting_2.setText(QCoreApplication.translate("Chat", u"Chats", None))
    # retranslateUi

