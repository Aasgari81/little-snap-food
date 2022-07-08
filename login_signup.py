from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as msc
import re
from error_ui import *
from dashboard import *
import smtplib
import random
import string
from mainwindow import MainWindow



class Ui_signup(object):
    def generate_random_password():
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        ## length of password from the user
        length = 3

        ## shuffling the characters
        random.shuffle(characters)

        ## picking random characters from the list
        password = []
        for length in range(length):
            password.append(random.choice(characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
        ## printing the list
        return "Devel01." + "".join(password)
    
    def signing_up(self) :
        """
        In this function we will do the signing up proccess such as checking inputs and then create an object of customer class
        in wich we will pass it to the database and then by its attribute database wil be updated
        """
        print("clicked")
        checking = True
        if len(self.first_name_input.text().strip()) == 0 or len(self.last_name_input.text().strip()) == 0 or len(self.email_input.text().strip()) == 0 or len(self.password_input.text().strip()) == 0 or len(self.confirm_password_input.text().strip()) == 0 or len(self.phone_number_input.text().strip()) == 0 :
            Ui_input_error.error_message_run(self)
            checking = False
            return
        mydb_cursor = login_Ui_MainWindow.mydb_cursor.cursor()
        mydb_cursor.execute("SELECT email, password FROM customer")
        customers_info = mydb_cursor.fetchall()
        mydb_cursor.execute("SELECT email, password FROM manager")
        managers_info = mydb_cursor.fetchall ()
        numbers = "123456789"
        lowercase_words = "abcdefghigklmnopqrstuvwxyz"
        uppercase_words = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
        characters = "!@#$%^&*"
        #displaying propper message if ID nubmer is not right
        if len(self.id_number_input.text().strip()) != 10:
            Ui_id_nubmer_not_valid.error_message_run(self)
            checking = False
            return
        for letter in lowercase_words :
            if letter in self.id_number_input.text().strip() :
                Ui_id_nubmer_not_valid.error_message_run(self)
                checking = False
                return
        for letter in uppercase_words :
            if letter in self.id_number_input.text().split() :
                Ui_id_nubmer_not_valid.error_message_run(self)
                checking = False
                return
        for character in characters :
            if character in self.id_number_input.text().split() :
                Ui_id_nubmer_not_valid.error_message_run(self)
                checking = False
                return
        #displaying propper mesage if names aren't valid
        for character in characters :
            if character in self.first_name_input.text().strip() or character in self.last_name_input.text().strip() :
                Ui_name_not_valid.error_message_run(self)
                checking = False
                return
        for number in numbers :
            if number in self.first_name_input.text().strip() or number in self.last_name_input.text().strip():
                Ui_name_not_valid.error_message_run(self)
                checking = False
                return
        #checking email address
        pat_email = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if not (re.match(pat_email,self.email_input.text().strip())):
            Ui_email_not_valid.error_message_run(self)
            checking = False
            return
        for email_tupe in managers_info:
            for email in email_tupe :
                if email == self.email_input.text().strip().lower():
                    Ui_password_not_valid.error_message_run(self, "This email already exist in database")
                    checking = False
                    return
        for email_tupe in customers_info:
            for email in email_tupe :
                if email == self.email_input.text().strip().lower():
                    Ui_password_not_valid.error_message_run(self, "This email already exist in database")
                    checking = False
                    return
            
        #checking phone number 
        regex_phone = re.compile(r'(?:\+\d{2})?\d{10,11}')
        if not(re.match(regex_phone, self.phone_number_input.text().strip())):
            Ui_phone_number_not_valid.error_message_run(self)
            checking = False
            return
        if len(self.phone_number_input.text().strip()) > 14  or len(self.phone_number_input.text().strip()) < 10:
            Ui_phone_number_not_valid.error_message_run(self)
            checking = False
            return
        #checking password
        if len(self.password_input.text().strip()) < 8 :
            Ui_password_not_valid.error_message_run(self, "Your password must contain at least 8 characters")
            checking = False
            return
        if not any(char in self.password_input.text().strip() for char in characters ) :
            Ui_password_not_valid.error_message_run(self, "Your password must contain at least one special character")
            checking = False
            return
        if not any(char.isupper() for char in self.password_input.text().strip()) :
            Ui_password_not_valid.error_message_run(self, "Your password must contain at least one uppercase letter")
            checking = False
            return
        if not any(char.islower() for char in self.password_input.text().strip()) :
            Ui_password_not_valid.error_message_run(self, "Your password must contain at least one lowercase letter")
            checking = False
            return
        if not any(char.isdigit() for char in self.password_input.text().strip()) :
            Ui_password_not_valid.error_message_run(self, "Your password must contain at least one number")
            checking = False
            return
        #checking if the confirm password is equal to password
        if not(self.confirm_password_input.text().strip() == self.password_input.text().strip()) :
            Ui_password_not_valid.error_message_run(self, "The confirmation password does not match password")
            checking = False
            return
        #saving informations in database by creating a object from custumer class
        if checking :
            my_customer = customer(self.first_name_input.text().strip().lower(), self.last_name_input.text().strip().lower(), self.phone_number_input.text().strip(), self.email_input.text().strip().lower(), self.id_number_input.text().strip(), self.password_input.text().strip(), 'D:/projects/FPAP/profilepicture.png')
            mydb_cursor.execute(f"INSERT INTO customer VALUES ('{customer.customer_id}', '{my_customer.first_name}', '{my_customer.last_name}', '{my_customer.phone_number}', '{my_customer.email}', '{my_customer.Id_number}', '{my_customer.password}', '{my_customer.picture_path}', NULL)")
            login_Ui_MainWindow.mydb_cursor.commit()
            #going to main page 
            self.email = my_customer.email
            Ui_dashboard.dashboard_run(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 750)
        self.signup_page = QtWidgets.QWidget(MainWindow)
        self.signup_page.setStyleSheet("*{\n"
"    color:#f6c658;\n"
"    }\n"
"#signup_page{\n"
"    background-color :#0f0f0f;\n"
"    }\n"
"#first_name_input, #last_name_input, #phone_number_input, #email_input, #id_number_input,#password_input, #confirm_password_input{\n"
"    color:#0f0f0f;\n"
"}\n"
"#sigup_btn_frame{\n"
"    background-color :#f6c658;\n"
"    border : 2px solid #0f0f0f;\n"
"    border-radius : 10px;\n"
"    \n"
"    }\n"
"#signup_btn {\n"
"    border:none;    \n"
"    color :#0f0f0f;\n"
"    }")
        self.signup_page.setObjectName("signup_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.signup_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signup_widget = QtWidgets.QWidget(self.signup_page)
        self.signup_widget.setObjectName("signup_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.signup_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Login_label = QtWidgets.QLabel(self.signup_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Login_label.setFont(font)
        self.Login_label.setObjectName("Login_label")
        self.verticalLayout_2.addWidget(self.Login_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.signup_widget, 0, QtCore.Qt.AlignTop)
        self.widget = QtWidgets.QWidget(self.signup_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.first_name_frame = QtWidgets.QFrame(self.widget)
        self.first_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_name_frame.setObjectName("first_name_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.first_name_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.first_name_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.first_name_input = QtWidgets.QLineEdit(self.first_name_frame)
        self.first_name_input.setObjectName("first_name_input")
        self.verticalLayout_4.addWidget(self.first_name_input)
        self.verticalLayout_3.addWidget(self.first_name_frame)
        self.last_name_frame = QtWidgets.QFrame(self.widget)
        self.last_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.last_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.last_name_frame.setObjectName("last_name_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.last_name_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.last_name_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.last_name_input = QtWidgets.QLineEdit(self.last_name_frame)
        self.last_name_input.setObjectName("last_name_input")
        self.verticalLayout_5.addWidget(self.last_name_input)
        self.verticalLayout_3.addWidget(self.last_name_frame)
        self.Phone_number_frame = QtWidgets.QFrame(self.widget)
        self.Phone_number_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Phone_number_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Phone_number_frame.setObjectName("Phone_number_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Phone_number_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.Phone_number_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.phone_number_input = QtWidgets.QLineEdit(self.Phone_number_frame)
        self.phone_number_input.setObjectName("phone_number_input")
        self.verticalLayout_6.addWidget(self.phone_number_input)
        self.verticalLayout_3.addWidget(self.Phone_number_frame)
        self.email_frame = QtWidgets.QFrame(self.widget)
        self.email_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.email_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.email_frame.setObjectName("email_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.email_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.email_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.email_input = QtWidgets.QLineEdit(self.email_frame)
        self.email_input.setObjectName("email_input")
        self.verticalLayout_7.addWidget(self.email_input)
        self.verticalLayout_3.addWidget(self.email_frame)
        self.ID_nubmer_frame = QtWidgets.QFrame(self.widget)
        self.ID_nubmer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ID_nubmer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ID_nubmer_frame.setObjectName("ID_nubmer_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.ID_nubmer_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.ID_nubmer_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.id_number_input = QtWidgets.QLineEdit(self.ID_nubmer_frame)
        self.id_number_input.setObjectName("id_number_input")
        self.verticalLayout_8.addWidget(self.id_number_input)
        self.verticalLayout_3.addWidget(self.ID_nubmer_frame)
        self.password_frame = QtWidgets.QFrame(self.widget)
        self.password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_frame.setObjectName("password_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.password_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.password_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.password_input = QtWidgets.QLineEdit(self.password_frame)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout_9.addWidget(self.password_input)
        self.verticalLayout_3.addWidget(self.password_frame)
        self.repeat_password_frame = QtWidgets.QFrame(self.widget)
        self.repeat_password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.repeat_password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.repeat_password_frame.setObjectName("repeat_password_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.repeat_password_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.repeat_password_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.confirm_password_input = QtWidgets.QLineEdit(self.repeat_password_frame)
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_input.setObjectName("confirm_password_input")
        self.verticalLayout_10.addWidget(self.confirm_password_input)
        self.verticalLayout_3.addWidget(self.repeat_password_frame)
        self.verticalLayout.addWidget(self.widget)
        self.sigup_btn_widget = QtWidgets.QWidget(self.signup_page)
        self.sigup_btn_widget.setObjectName("sigup_btn_widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.sigup_btn_widget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.sigup_btn_frame = QtWidgets.QFrame(self.sigup_btn_widget)
        self.sigup_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sigup_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sigup_btn_frame.setObjectName("sigup_btn_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.sigup_btn_frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.signup_btn = QtWidgets.QPushButton(self.sigup_btn_frame)
        self.signup_btn.clicked.connect(self.signing_up)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        self.verticalLayout_12.addWidget(self.signup_btn)
        self.verticalLayout_11.addWidget(self.sigup_btn_frame)
        self.verticalLayout.addWidget(self.sigup_btn_widget)
        MainWindow.setCentralWidget(self.signup_page)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signup"))
        self.Login_label.setText(_translate("MainWindow", "Sign up"))
        self.label.setText(_translate("MainWindow", "First name"))
        self.label_2.setText(_translate("MainWindow", "Last name"))
        self.label_3.setText(_translate("MainWindow", "Phone number"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_5.setText(_translate("MainWindow", "ID number"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_7.setText(_translate("MainWindow", "Confirm password"))
        self.signup_btn.setText(_translate("MainWindow", "Sign up"))


    def signup_runner(self) :
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_signup()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

class login_Ui_MainWindow(object):
    mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
    mydb_cursor = mydb.cursor()

    def generate_random_password():
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        ## length of password from the user
        length = 3

        ## shuffling the characters
        random.shuffle(characters)

        ## picking random characters from the list
        password = []
        for length in range(length):
            password.append(random.choice(characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
        ## printing the list
        return "Devel01." + "".join(password)




    def logingin(self) :
        mydb_cursor = login_Ui_MainWindow.mydb_cursor
        
        """
    In this function we will check whether the email is in the database or not if there was it will
    a proper window (base on the user) otherwise it will open a window that shows appropriate message
    to the user
        """
        print("clicked")
        
        if len(self.email_input.text().strip()) == 0 :
            Ui_input_error.error_message_run(self)
            return
        if len(self.password_input.text()) == 0 :
            Ui_input_error.error_message_run(self)
            return
        password = self.password_input.text()
        self.email = self.email_input.text().lower()
        mydb_cursor = login_Ui_MainWindow.mydb_cursor.cursor()
        mydb_cursor.execute("SELECT email, password FROM customer")
        customers_info = mydb_cursor.fetchall()
        mydb_cursor.execute("SELECT email, password FROM manager")
        managers_info = mydb_cursor.fetchall ()
        




        #checking inputs and displaying proper message for each onoe of them
        for customer in customers_info :
            if self.email in customer and password == customer[1] : 
                Ui_dashboard.dashboard_run(self)
                return
            elif self.email in customer and password != customer[1] :
                if login_Ui_MainWindow.entered_incorrect_pass < 3:
                    Ui_not_right_password.error_message_run(self)
                    login_Ui_MainWindow.entered_incorrect_pass += 1
                    return
                else:
                    sender_email = "develgroup01@gmail.com"
                    rec_email = self.email
                    password = "1381382aliamir"
                    customer_password = login_Ui_MainWindow.generate_random_password()
                    message = f"""hey, it seemed that you forgot your password. \n your password is: {customer_password}"""
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, rec_email, message)
                    sql = "UPDATE customers SET password = %s WHERE email = %s"
                    cumstomer_info = (customer_password, rec_email)
                    mydb_cursor.execute(sql, cumstomer_info)
                    login_Ui_MainWindow.mydb.execute()
                    

        for manager in managers_info :
            if self.email in manager and password == manager[1] :
                mydb_cursor.execute(f"SELECT restaurant_id FROM restuarantinfo WHERE manager_id = {manager[0]}")
                self.restaurant_id = mydb_cursor.fetchall()[0][0] 
                MainWindow.__init__(self, self.restaurant_id)
                return
            elif self.email in manager and password != manager[1] :
                Ui_not_right_password.error_message_run(self)
                return
        
        Ui_error_message_form.error_message_run(self)




    def signup_runner(self) : 
        Ui_signup.signup_runner(self)
        return

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 758)
        self.Login_Page = QtWidgets.QWidget(MainWindow)
        self.Login_Page.setStyleSheet("*{\n"
"    color:#f6c658;\n"
"    }\n"
"#Login_Page{\n"
"    background-color :#0f0f0f;\n"
"    }\n"
"#login_btn {\n"
"    border :none;\n"
"    color:#0f0f0f;\n"
"    }\n"
"#login_btn_frame{    \n"
"    background-color :#f6c658;\n"
"    border :2px solid #0f0f0f;\n"
"    border-radius : 10px;\n"
"    }\n"
"#email_input{\n"
"    color: #0f0f0f;\n"
"    }\n"
"#email_input, #password_input{\n"
"    color:#0f0f0f;\n"
"    }\n"
"#signup_btn{\n"
"    background-color:#0f0f0f;\n"
"    border : none;\n"
"    }")
        self.Login_Page.setObjectName("Login_Page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Login_Page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Loginlabel_widget = QtWidgets.QWidget(self.Login_Page)
        self.Loginlabel_widget.setObjectName("Loginlabel_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Loginlabel_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Login_label = QtWidgets.QLabel(self.Loginlabel_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Login_label.setFont(font)
        self.Login_label.setObjectName("Login_label")
        self.verticalLayout_2.addWidget(self.Login_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Loginlabel_widget)
        self.Main_widget = QtWidgets.QWidget(self.Login_Page)
        self.Main_widget.setMinimumSize(QtCore.QSize(0, 677))
        self.Main_widget.setObjectName("Main_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Main_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.email_password_frame = QtWidgets.QFrame(self.Main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_password_frame.sizePolicy().hasHeightForWidth())
        self.email_password_frame.setSizePolicy(sizePolicy)
        self.email_password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.email_password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.email_password_frame.setObjectName("email_password_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.email_password_frame)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.email_frame = QtWidgets.QFrame(self.email_password_frame)
        self.email_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.email_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.email_frame.setObjectName("email_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.email_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.email_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.email_input = QtWidgets.QLineEdit(self.email_frame)
        self.email_input.setObjectName("email_input")
        self.verticalLayout_5.addWidget(self.email_input)
        self.verticalLayout_4.addWidget(self.email_frame, 0, QtCore.Qt.AlignTop)
        self.password_frame = QtWidgets.QFrame(self.email_password_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_frame.sizePolicy().hasHeightForWidth())
        self.password_frame.setSizePolicy(sizePolicy)
        self.password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_frame.setObjectName("password_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.password_frame)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.password_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.password_input = QtWidgets.QLineEdit(self.password_frame)
        self.password_input.setObjectName("password_input")
        self.verticalLayout_6.addWidget(self.password_input)
        self.verticalLayout_4.addWidget(self.password_frame, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.email_password_frame, 0, QtCore.Qt.AlignTop)
        self.login_btn_frame = QtWidgets.QFrame(self.Main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn_frame.sizePolicy().hasHeightForWidth())
        self.login_btn_frame.setSizePolicy(sizePolicy)
        self.login_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_btn_frame.setObjectName("login_btn_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_btn_frame)
        self.horizontalLayout.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_btn = QtWidgets.QPushButton(self.login_btn_frame)
        self.login_btn.clicked.connect(self.logingin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.login_btn_frame, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.Main_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.signup_btn = QtWidgets.QPushButton(self.frame)
        self.signup_btn.clicked.connect(self.signup_runner)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_btn.sizePolicy().hasHeightForWidth())
        self.signup_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        self.verticalLayout_7.addWidget(self.signup_btn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout.addWidget(self.Main_widget, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.Login_Page)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.Login_label.setText(_translate("MainWindow", "Log in"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.signup_btn.setText(_translate("MainWindow", "Sign up"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())