from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as msc
import re
from functools import partial


class Restaurant:
    def __init__(self, name, district, catagory, address, manager_id, restaurant_id):
        self.restaurant_id = restaurant_id
        self.name = name 
        self.district = district 
        self.catagory = catagory
        self.address = address
        self.manager_name = manager_id
        self.foods = []
    
class Ui_error_message_form(object):
    """This class will create windows that shows a error for email not being in database"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Your email was not found you should signup frist"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_error_message_form()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

class Ui_input_error(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Your input is empty try again"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_input_error()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

class Ui_not_right_password(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Password is incorrect try again"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_not_right_password()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_not_right_password()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

class Ui_name_not_valid(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Your ID nubmer is not valid try again"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_id_nubmer_not_valid()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

class Ui_id_nubmer_not_valid(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Your first/last name is not valid try again"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_name_not_valid()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

class customer:
    mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
    mydb_cursor = mydb.cursor()
    mydb_cursor.execute(f"SELECT customer_id FROM customer ORDER BY customer_id DESC LIMIT 1")
    try :
        resault = mydb_cursor.fetchall()
        resault = resault[0]
        customer_id = resault[0]
    except : 
        customer_id = 0
    def __init__(self, first_name : str, last_name : str, phone_number : int, email : str, Id_number : str, password : str, picture_path : str) : 
        """
        We don't do any checking here since we will check in the button command function
        """
        customer.customer_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.Id_number = Id_number
        self.password = password
        self.picture_path = picture_path

class Ui_name_not_valid(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Your ID nubmer is not valid try again"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_id_nubmer_not_valid()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

class Ui_phone_number_not_valid(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Your phone number is not valid try again"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_phone_number_not_valid()
        self.error_message_form.show()

class Ui_email_not_valid(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", "Your email is not valid try again"))


    def error_message_run(self):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_email_not_valid()
        self.ui.setupUi(self.error_message_form)
        self.error_message_form.show()

class Ui_password_not_valid(object):
    """This class will create windows that shows a error for input being empty"""
    def setupUi(self, error_message_form, text):
        error_message_form.setObjectName("error_message_form")
        error_message_form.resize(628, 149)
        error_message_form.setStyleSheet("#label {\n"
"    color : #f6c658;\n"
"    }\n"
"#error_message_form {\n"
"    background-color : #0f0f0f;\n"
"    }\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(error_message_form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(error_message_form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(error_message_form, text)
        QtCore.QMetaObject.connectSlotsByName(error_message_form)

    def retranslateUi(self, error_message_form, text):
        _translate = QtCore.QCoreApplication.translate
        error_message_form.setWindowTitle(_translate("error_message_form", "Error"))
        self.label.setText(_translate("error_message_form", text))


    def error_message_run(self, text):
        self.error_message_form = QtWidgets.QWidget()
        self.ui = Ui_password_not_valid()
        self.ui.setupUi(self.error_message_form, text)
        self.error_message_form.show()
