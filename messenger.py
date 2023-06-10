"""
The receiver and sender part of the messenger
"""
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
from ui_welcome import Ui_Welcome
from ui_chat import Ui_Chat
import requests
from datetime import datetime


class Chat(QWidget, Ui_Chat):
    """
    Class that implements the chat window
    """
    def __init__(self, url, welcome):
        """
        Constructor of the Chat class
        :param url: Url of the connected server
        :param welcome: The instance of the welcome window
        """
        super().__init__()
        self.setupUi(self)
        self.open.clicked.connect(self.open_chat)
        self.send.clicked.connect(self.send_message)
        self.open_2.clicked.connect(self.change_account)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(100)
        self.welcome = welcome
        self.url = url
        self.name = ""
        self.opened = False
        self.to = ""

    def set_name(self, name):
        """
        The function that sets of the name currently using messenger
        :param name: Name of the user
        """
        self.name = name
        try:
            response = requests.get('{}/connect'.format(self.url), params={'name': self.name, 'signin': 'true'})
        except:
            QMessageBox.critical(self, "Server not available", "Something went wrong!")
            self.opened = False
            return
        if response.json()['status'] == 'true':
            self.greeting.setText("Hello, {}".format(self.name))
        else:
            QMessageBox.critical(self, "Something went wrong", "For some reason, the user was unable to be connected")

    def open_chat(self):
        """
        The function that opens the given chat
        """
        if self.user_to.text() == "":
            QMessageBox.critical(self, "Invalid username", "Please, write something!")
        else:
            try:
                response = requests.get('{}/connect'.format(self.url), params={'name': self.user_to.text(), 'signin': 'false'})
            except:
                QMessageBox.critical(self, "Server not available", "Something went wrong!")
                self.opened = False
                return
            if response.json()['status'] == 'true':
                self.to = self.user_to.text()
                self.opened = True
            else:
                QMessageBox.critical(self, "Invalid username", "Username wasn't found!")

    def send_message(self):
        """
        The function that sends the message
        """
        if not self.opened:
            QMessageBox.critical(self, "Chat not opened", "Please, open chat first!")
        elif self.message_enter.toPlainText() == "":
            QMessageBox.critical(self, "Invalid message", "Please, write a message!")
        else:
            message = {'from': self.name, 'to': self.to, 'text': self.message_enter.toPlainText()}
            try:
                response = requests.post('{}/send'.format(self.url), json=message)
                self.update_messages()
            except:
                QMessageBox.critical(self, "Server not available", "Something went wrong!")
                self.opened = False
                return
            finally:
                self.message_enter.setPlainText("")
            if response.status_code != 200:
                QMessageBox.critical(self, "An error occurred", "Something went wrong!")
                self.opened = False

    def display_message(self, message):
        """
        The function that displays the given message on the window
        :param message: Message displayed
        """
        if message['from'] == self.name:
            name = "You"
        else:
            name = message['from']
        date_time = datetime.fromtimestamp(message['time']).strftime('%H:%M:%S %d.%m.%Y')
        text = message['text']
        self.chat.setPlainText("{}{} at {}:\n{}\n\n".format(self.chat.toPlainText(), name, date_time, text))

    def update_messages(self):
        """
        The function that updates the list of messages needed to be displayed
        """
        if self.opened:
            self.chat.setPlainText("")
            try:
                response = requests.get('{}/messages'.format(self.url), params={'from': self.name, 'to': self.to})
            except:
                QMessageBox.critical(self, "Server not available", "Something went wrong!")
                self.opened = False
                return
            messages = response.json()['messages']
            if len(messages) == 0:
                self.chat.setPlainText("This chat has no messages yet. Send something!")
            else:
                for message in messages:
                    self.display_message(message)

    def change_account(self):
        """
        The function that return to the welcome window
        """
        self.welcome.show()
        self.close()


class Welcome(QWidget, Ui_Welcome):
    """
    Class that implements the welcome window
    """
    def __init__(self, url):
        """
        Constructor of the Welcome class
        :param url: Url of the connected server
        """
        super().__init__()
        self.setupUi(self)
        self.join.clicked.connect(self.join_clicked)
        self.url = url
        self.chat = Chat(url, self)

    def join_clicked(self):
        """
        Function that opens the chat window
        """
        if self.username.text() == "":
            QMessageBox.critical(self, "Invalid username", "Please, write something!")
        else:
            self.chat.set_name(self.username.text())
            self.chat.to = ""
            self.chat.opened = False
            self.chat.user_to.setText('')
            self.chat.chat.setPlainText('')
            self.chat.message_enter.setPlainText('')
            self.chat.show()
            self.close()
