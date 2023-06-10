from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QMessageBox, QListWidgetItem
from ui_welcome import Ui_Welcome
from ui_chat import Ui_Chat
from ui_newchat import Ui_NewChat
from ui_newuser import Ui_NewUser
import requests
from datetime import datetime


class Chat(QWidget, Ui_Chat):
    def __init__(self, url, welcome):
        super().__init__()
        self.setupUi(self)
        self.send.clicked.connect(self.send_message)
        self.change.clicked.connect(self.change_account)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self.chat_list.itemClicked.connect(self.open_chat)
        self.new_chat.clicked.connect(self.create_chat_clicked)
        self.add_user.clicked.connect(self.add_user_clicked)
        self.welcome = welcome
        self.url = url
        self.name = ""
        self.opened = False
        self.chat_name = ""
        self.prev_mess = []
        self.prev_chats = []
        self.new_chat = None
        self.new_user = None

    def set_name(self, name):
        self.name = name
        self.prev_mess = []
        self.prev_chats = []
        self.opened = False
        try:
            response = requests.get('{}/connect'.format(self.url), params={'name': self.name})
        except:
            QMessageBox.critical(self, "Server not available", "Something went wrong!")
            self.change_account()
            return
        if response.json()['status'] == 'true':
            self.greeting.setText("Hello, {}".format(self.name))
            self.update_chats(True)
        else:
            QMessageBox.critical(self, "Something went wrong", "For some reason, the user was unable to be connected")

    def open_chat(self, chat):
        self.chat_name = chat.text()
        self.update_messages(True)
        self.opened = True

    def send_message(self):
        if not self.opened:
            QMessageBox.critical(self, "Chat not opened", "Please, open chat first!")
        elif self.message_enter.toPlainText() == "":
            QMessageBox.critical(self, "Invalid message", "Please, write a message!")
        else:
            message = {'from': self.name, 'chat': self.chat_name, 'text': self.message_enter.toPlainText()}
            try:
                response = requests.post('{}/send'.format(self.url), json=message)
                self.update_messages()
            except:
                QMessageBox.critical(self, "Server not available", "Something went wrong!")
                self.opened = False
                return
            finally:
                self.message_enter.setPlainText("")
            if response.status_code != 200 or response.json()['status'] == 'false':
                QMessageBox.critical(self, "An error occurred", "Something went wrong!")
                self.opened = False

    def display_message(self, message):
        if message['from'] == self.name:
            name = "You"
        else:
            name = message['from']
        date_time = datetime.fromtimestamp(message['time']).strftime('%H:%M:%S %d.%m.%Y')
        text = message['text']
        self.chat.insertPlainText("{} at {}:\n{}\n\n".format(name, date_time, text))

    def update_messages(self, every=False):
        if self.opened:
            try:
                response = requests.get('{}/messages'.format(self.url), params={'user': self.name, 'chat': self.chat_name})
            except:
                QMessageBox.critical(self, "Server not available", "Something went wrong!")
                self.opened = False
                return
            if response.json()['status'] == 'false':
                QMessageBox.critical(self, "An error occurred", "Something went wrong!")
                self.opened = False
                return
            messages = response.json()['messages']
            if len(messages) == 0:
                self.chat.setPlainText("This chat has no messages yet. Send something!")
            else:
                if every or self.prev_mess == []:
                    self.chat.setPlainText("")
                for message in messages:
                    if every or message not in self.prev_mess:
                        self.display_message(message)
            self.prev_mess = messages

    def update_chats(self, every=False):
        if self.name == "":
            return
        try:
            response = requests.get("{}/chats".format(self.url), params={'user': self.name})
        except:
            QMessageBox.critical(self, "Server not available", "Something went wrong!")
            self.change_account()
            return
        if response.json()['status'] == 'false':
            QMessageBox.critical(self, "An error occurred", "Something went wrong!")
            self.change_account()
            return
        chats = response.json()['chats']
        if every:
            self.chat_list.clear()
        for chat in chats:
            if every or chat not in self.prev_chats:
                QListWidgetItem(chat, self.chat_list)
        self.prev_chats = chats

    def update(self):
        self.update_messages()
        self.update_chats()

    def change_account(self):
        self.welcome.show()
        self.close()

    def create_chat_clicked(self):
        self.new_chat = NewChat(self.url, self.name)
        self.new_chat.show()

    def add_user_clicked(self):
        if self.opened:
            self.new_user = NewUser(self.url, self.chat_name, self.name)
            self.new_user.show()
        else:
            QMessageBox.critical(self, "Chat not opened", "Please, open chat first")


class Welcome(QWidget, Ui_Welcome):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.join.clicked.connect(self.join_clicked)
        self.url = url
        self.chat = Chat(url, self)

    def join_clicked(self):
        if self.username.text() == "":
            QMessageBox.critical(self, "Invalid username", "Please, write something!")
        else:
            self.chat.set_name(self.username.text())
            self.chat.to = ""
            self.chat.opened = False
            self.chat.chat.setPlainText('')
            self.chat.message_enter.setPlainText('')
            self.chat.show()
            self.close()


class NewChat(QWidget, Ui_NewChat):
    def __init__(self, url, user):
        super().__init__()
        self.setupUi(self)
        self.create_chat.clicked.connect(self.create_clicked)
        self.url = url
        self.user = user

    def create_clicked(self):
        if self.name.text() == "":
            QMessageBox.critical(self, "Invalid name", "Please, write a name!")
            return
        try:
            response = requests.get("{}/addchat".format(self.url), params={'chat': self.name.text(), 'user': self.user})
        except:
            QMessageBox.critical(self, "Server not available", "Something went wrong!")
            return
        if response.json()['status'] == 'false':
            QMessageBox.critical(self, "Invalid name", "Chat with that name already exists!")
        else:
            self.close()


class NewUser(QWidget, Ui_NewUser):
    def __init__(self, url, chat, who):
        super().__init__()
        self.setupUi(self)
        self.add.clicked.connect(self.add_clicked)
        self.url = url
        self.who = who
        self.chat = chat

    def add_clicked(self):
        if self.name.text() == "":
            QMessageBox.critical(self, "Invalid name", "Please, write a name!")
            return
        try:
            response = requests.get("{}/adduser".format(self.url), params={'chat': self.chat, 'user': self.name.text(), 'who': self.who})
        except:
            QMessageBox.critical(self, "Server not available", "Something went wrong!")
            return
        if response.json()['status'] == 'false':
            QMessageBox.critical(self, "Invalid name", "User with that name doesn't exist")
        else:
            self.close()
