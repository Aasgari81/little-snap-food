from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as msc
import re
from functools import partial
from order import *



class Ui_search(object):
    def setupUi(self, MainWindow):
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mycursor = mydb.cursor()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 692)
        MainWindow.setStyleSheet("QRadioButton::indicator:checked {\n"
"    background-color:#FDB827;\n"
"    border: 2px solid #F1F1F1;\n"
"    border-radius: 10px;\n"
"}\n"
"background-color: #23120B;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #000000;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("\n"
"color: #F1F1F1;\n"
"font: 14pt \"Calibri\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setStyleSheet("border-radius: 8px;\n"
"background-color: #393E46;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setStyleSheet("background-color: #FDB827;\n"
"border-radius: 10px;\n"
"width: 30px;\n"
"height: 30px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 872, 557))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.radioButton.setText("food")
        self.radioButton_2.setText("restaurant")
        self.radioButton_3.setText("material")

        self.pushButton.clicked.connect(self.search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


        if self.radioButton.isChecked():
                val = self.radioButton.text()
        elif self.radioButton_2.isChecked():
                val = self.radioButton_2.text()
        else:
                val = self.radioButton_3.text()

        if val == 'restaurant':
                search_input = self.lineEdit.text()
                sql_find_restaurantname = f"SELECT * FROM restuarantinfo WHERE restaurant_name LIKE '%{search_input}%'"
                mycursor.execute(sql_find_restaurantname)
                restaurants = mycursor.fetchall()



        elif val == 'material': 
                restaurant_id_list = tuple()
                restaurants = []
                search_input = self.lineEdit.text()
                sql_find_foodname = f"SELECT * FROM foodofrestuarant  WHERE food_material LIKE '%{search_input}%'"
                mycursor.execute(sql_find_foodname)
                restaurantname_result = mycursor.fetchall()
                for restaurant_info in restaurantname_result:
                        restaurant_id_list += restaurant_info[0],

                for restaurant_id in restaurant_id_list:
                        mycursor.execute(f"SELECT * FROM restuarantinfo WHERE restaurant_id = {restaurant_id}")
                        restaurants.append(mycursor.fetchall()[0])

        else: 
                restaurants = []
                restaurant_id_list = tuple()
                search_input = self.lineEdit.text()
                sql_find_foodname = f"SELECT * FROM foodofrestuarant  WHERE food_name LIKE '%{search_input}%'"
                mycursor.execute(sql_find_foodname)
                restaurantname_result = mycursor.fetchall()
                for restaurant_info in restaurantname_result:
                        restaurant_id_list += restaurant_info[0],

                for restaurant_id in restaurant_id_list:
                        mycursor.execute(f"SELECT * FROM restuarantinfo WHERE restaurant_id = {restaurant_id}")
                        restaurants.append(mycursor.fetchall()[0])


        for i in restaurants :
            self.restaurant_id = i[0]
            self.fast_food_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.fast_food_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.fast_food_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.fast_food_frame.setObjectName("fast_food_frame")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.fast_food_frame)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setSpacing(7)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.picture_frame = QtWidgets.QFrame(self.fast_food_frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.picture_frame.sizePolicy().hasHeightForWidth())
            self.picture_frame.setSizePolicy(sizePolicy)
            self.picture_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.picture_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.picture_frame.setObjectName("picture_frame")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.picture_frame)
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.label = QtWidgets.QLabel(self.picture_frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
            self.label.setSizePolicy(sizePolicy)
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap(f"{i[6]}"))
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
            self.horizontalLayout.addWidget(self.picture_frame)
            self.info_frame = QtWidgets.QFrame(self.fast_food_frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
            self.info_frame.setSizePolicy(sizePolicy)
            self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.info_frame.setObjectName("info_frame")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.info_frame)
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            self.frame = QtWidgets.QFrame(self.info_frame)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label_2 = QtWidgets.QLabel(self.frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")
            self.horizontalLayout_2.addWidget(self.label_2)
            self.restaurant_label = QtWidgets.QLabel(self.frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.restaurant_label.setFont(font)
            self.restaurant_label.setObjectName("restaurant_label")
            self.horizontalLayout_2.addWidget(self.restaurant_label)
            self.verticalLayout_4.addWidget(self.frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
            self.frame_5 = QtWidgets.QFrame(self.info_frame)
            self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_5.setObjectName("frame_5")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.label_4 = QtWidgets.QLabel(self.frame_5)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label_4")
            self.horizontalLayout_3.addWidget(self.label_4)
            self.category_label = QtWidgets.QLabel(self.frame_5)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.category_label.setFont(font)
            self.category_label.setObjectName("category_label")
            self.horizontalLayout_3.addWidget(self.category_label)
            self.verticalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.frame_6 = QtWidgets.QFrame(self.info_frame)
            self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_6.setObjectName("frame_6")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.label_6 = QtWidgets.QLabel(self.frame_6)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label_6")
            self.horizontalLayout_4.addWidget(self.label_6)
            self.district_label = QtWidgets.QLabel(self.frame_6)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(False)
            font.setWeight(50)
            self.district_label.setFont(font)
            self.district_label.setObjectName("district_label")
            self.horizontalLayout_4.addWidget(self.district_label)
            self.verticalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.order_btn_frame = QtWidgets.QFrame(self.info_frame)
            self.order_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.order_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.order_btn_frame.setObjectName("order_btn_frame")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.order_btn_frame)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.order_btn = QtWidgets.QPushButton(self.order_btn_frame)
            self.order_btn.clicked.connect(partial(Ui_search.restaurant_menu, self, self.restaurant_id, self.customer_id))
            self.order_btn.setObjectName("order_btn")
            self.horizontalLayout_5.addWidget(self.order_btn)
            self.verticalLayout_4.addWidget(self.order_btn_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.horizontalLayout.addWidget(self.info_frame)
            self.verticalLayout_2.addWidget(self.fast_food_frame)
            self.scrollarea_for_order.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.scrollarea_for_order)
            self.MainWindow.setCentralWidget(self.order_widget)
            self.retranslateUi(self.MainWindow, i)
            QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    
    def retranslateUi(self, MainWindow, i):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "food"))
        self.radioButton_2.setText(_translate("MainWindow", "restaurant"))
        self.radioButton_3.setText(_translate("MainWindow", "materail"))
        self.lineEdit.setText(_translate("MainWindow", "search..."))
        self.label_2.setText(_translate("MainWindow", "Restaurant name :"))
        self.restaurant_label.setText(_translate("MainWindow", f"{i[1]}"))
        self.label_4.setText(_translate("MainWindow", "category :"))
        self.category_label.setText(_translate("MainWindow", f"{i[3]}"))
        self.label_6.setText(_translate("MainWindow", "District :"))
        self.district_label.setText(_translate("MainWindow", f"{i[2]}"))
        self.order_btn.setText(_translate("MainWindow", "Order from this restaurant"))

    def restaurant_menu (self, restaurant_id, customer_id) :
        Ui_order_from_restaurant.order_from_restauranu_runner(self, restaurant_id)

class Ui_comment_page(object):
    """
    This page class will create a page fo commenting on the food
    """
    def setupUi(self, comment_page, food_id):
        #asiigning food_id to the food
        self.food_id = food_id
        #setting up ui page
        comment_page.setObjectName("comment_page")
        comment_page.resize(719, 179)
        self.centralwidget = QtWidgets.QWidget(comment_page)
        self.centralwidget.setStyleSheet("* {\n"
"    color :#f7c55d;\n"
"    }\n"
"#centralwidget{\n"
"    background-color :#0f0f0f;\n"
"    }\n"
"#comment_input {\n"
"    background-color :#292929;\n"
"    }\n"
"#submit_btn_frame{\n"
"    background-color :#f7c55d;\n"
"    border-radius :10px;\n"
"    }\n"
"#submit_btn{\n"
"    background-color :#f7c55d;\n"
"    color:#292929;\n"
"    border :none;\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.comment_input = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comment_input.setFont(font)
        self.comment_input.setText("")
        self.comment_input.setObjectName("comment_input")
        self.verticalLayout_2.addWidget(self.comment_input)
        self.verticalLayout.addWidget(self.frame)
        self.submit_btn_frame = QtWidgets.QFrame(self.centralwidget)
        self.submit_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.submit_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.submit_btn_frame.setObjectName("submit_btn_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.submit_btn_frame)
        self.horizontalLayout.setContentsMargins(5, 7, 5, 7)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submit_btn = QtWidgets.QPushButton(self.submit_btn_frame)
        self.submit_btn.clicked.connect(self.comment_submiter)
        self.submit_btn.setObjectName("submit_btn")
        self.horizontalLayout.addWidget(self.submit_btn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.submit_btn_frame, 0, QtCore.Qt.AlignHCenter)
        comment_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(comment_page)
        QtCore.QMetaObject.connectSlotsByName(comment_page)

    def retranslateUi(self, comment_page):
        _translate = QtCore.QCoreApplication.translate
        comment_page.setWindowTitle(_translate("comment_page", "Comment page"))
        self.label.setText(_translate("comment_page", "Enter your comment:"))
        self.submit_btn.setText(_translate("comment_page", "Submit"))


    def comment_page_runner(self, food_id) :
        self.comment_page = QtWidgets.QMainWindow()
        self.ui = Ui_comment_page()
        self.ui.setupUi(self.comment_page, food_id)
        self.comment_page.show()
        """
        this function will add the inputed comment to the database and for either going well or not will display proper message
        """
    def comment_submiter(self) :
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        mydb_cursor.execute(f"SELECT food_comments FROM foodsofrestaurant WHERE food_id = {self.food_id}")
        comments = mydb_cursor.fetchall()[0][0]
        mydb_cursor.execute(f"UPDATE foodsofrestaurant SET food_comments = '{comments}/{self.comment_input.text()}' WHERE food_id = {self.food_id}")
        mydb.commit()
        Ui_password_not_valid.error_message_run(self, "your comment has successfully add")
        return








class Ui_paying(object):
    """
    This class will create Ui for paying
    """
    def setupUi(self, paying, customer_id):
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        #getting price and amount of orders from database
        mydb_cursor.execute(f"SELECT price, amount FROM orders WHERE customer_id = {customer_id} and status = 'waiting'")
        result = mydb_cursor.fetchall()
        self.customer_id = customer_id
        total_price = 0
        #calculating the total price for paying
        for food in result :
            total_price += food[0] * food[1]
        self.total_price = total_price
        paying.setObjectName("paying")
        paying.setFixedSize(603, 298)
        self.centralwidget = QtWidgets.QWidget(paying)
        self.centralwidget.setStyleSheet("* {\n"
"    color:#f7c55d;\n"
"    }\n"
"#centralwidget {\n"
"    background-color :#292929;\n"
"    }\n"
"#finalize_btn {\n"
"    background-color :#f7c55d;\n"
"    color :#292929;\n"
"    border :none;\n"
"    }\n"
"#finalize_order_btn {\n"
"    background-color :#f7c55d;\n"
"    border-radius :10px;\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.credit_card_radiobtn = QtWidgets.QRadioButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.credit_card_radiobtn.setFont(font)
        self.credit_card_radiobtn.setObjectName("credit_card_radiobtn")
        self.verticalLayout_2.addWidget(self.credit_card_radiobtn)
        self.cash_radiobtn = QtWidgets.QRadioButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cash_radiobtn.setFont(font)
        self.cash_radiobtn.setObjectName("cash_radiobtn")
        self.verticalLayout_2.addWidget(self.cash_radiobtn)
        self.horizontalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
        self.finalize_order_btn = QtWidgets.QFrame(self.centralwidget)
        self.finalize_order_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.finalize_order_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.finalize_order_btn.setObjectName("finalize_order_btn")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.finalize_order_btn)
        self.horizontalLayout_3.setContentsMargins(5, 6, 5, 6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.finalize_btn = QtWidgets.QPushButton(self.finalize_order_btn)
        self.finalize_btn.clicked.connect(self.finalizing)
        self.finalize_btn.setObjectName("finalize_btn")
        self.horizontalLayout_3.addWidget(self.finalize_btn)
        self.verticalLayout.addWidget(self.finalize_order_btn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        paying.setCentralWidget(self.centralwidget)

        self.retranslateUi(paying)
        QtCore.QMetaObject.connectSlotsByName(paying)

    def retranslateUi(self, paying):
        total_price = self.total_price
        _translate = QtCore.QCoreApplication.translate
        paying.setWindowTitle(_translate("paying", "Finalizing page"))
        self.label.setText(_translate("paying", "Total price :"))
        self.label_2.setText(_translate("paying", f"{total_price}$"))
        self.label_3.setText(_translate("paying", "How would you like to pay:"))
        self.credit_card_radiobtn.setText(_translate("paying", "Credit card"))
        self.cash_radiobtn.setText(_translate("paying", "Cash"))
        self.finalize_btn.setText(_translate("paying", "Finalize the order"))


    def Ui_paying_runner (self, customer_id) :
        self.paying = QtWidgets.QMainWindow()
        self.ui = Ui_paying()
        self.ui.setupUi(self.paying, customer_id)
        self.paying.show()
    def finalizing(self) :
        """
        This function will finalize the orders and change the status of order in dataase to completed
        """
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        if self.credit_card_radiobtn.isChecked() :
            Ui_password_not_valid.error_message_run(self, "You are going to payment page.....")
            mydb_cursor.execute(f"UPDATE orders SET status = 'completed' WHERE customer_id = {self.customer_id} and status = 'waiting'")
            mydb.commit()
            return
        elif self.cash_radiobtn.isChecked() :
            Ui_password_not_valid.error_message_run(self, "You should pay cash to our delivery person")
            mydb_cursor.execute(f"UPDATE orders SET status = 'completed' WHERE customer_id = {self.customer_id} and status = 'waiting'")
            mydb.commit()
            return
        else :
            Ui_password_not_valid.error_message_run(self, "You should choose one way of paying")
            return









class Ui_privious_order(object):
    """
    This class will create a Ui that displayes the provious order of the customer
    """
    my_db = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
    
    def comment_page_runner(self, food_id) :
        Ui_comment_page.comment_page_runner(self, food_id)
    
    def setupUi(self, privious_order, customer_id):
        
        db_cursor = Ui_privious_order.my_db.cursor()
        #getting all the information from orders table with customer id and status of completed which means it has been paid
        db_cursor.execute(f"SELECT * FROM orders WHERE customer_id = {customer_id} and status = 'completed'")
        result = db_cursor.fetchall()
        privious_order.setObjectName("privious_order")
        privious_order.resize(1327, 568)
        self.centralwidget = QtWidgets.QWidget(privious_order)
        self.centralwidget.setStyleSheet("*{\n"
"    color :#f7c55d;\n"
"    }\n"
"#centralwidget {\n"
"    background-color :#0f0f0f;\n"
"    }\n"
"#scrollAreaWidgetContents{\n"
"    background-color:#292929;\n"
"    }\n"
"#comment_btn_frame{\n"
"    background-color :#f7c55d;\n"
"    border-radius :10px;\n"
"    }\n"
"#comment_btn {\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    color:#292929;\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1303, 544))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        #iterating through the result of orders result and setiting up ui for each one of them
        for i in result :
            food_id = i[3]
            self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.frame_2 = QtWidgets.QFrame(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
            self.frame_2.setSizePolicy(sizePolicy)
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            self.frame_4 = QtWidgets.QFrame(self.frame_2)
            self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_4.setObjectName("frame_4")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.name_frame = QtWidgets.QFrame(self.frame_4)
            self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.name_frame.setObjectName("name_frame")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.name_frame)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label = QtWidgets.QLabel(self.name_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.horizontalLayout_2.addWidget(self.label)
            self.name_label = QtWidgets.QLabel(self.name_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.name_label.setFont(font)
            self.name_label.setObjectName("name_label")
            self.horizontalLayout_2.addWidget(self.name_label)
            self.horizontalLayout_5.addWidget(self.name_frame)
            self.restaurant_frame = QtWidgets.QFrame(self.frame_4)
            self.restaurant_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.restaurant_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.restaurant_frame.setObjectName("restaurant_frame")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.restaurant_frame)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.label_3 = QtWidgets.QLabel(self.restaurant_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label_3")
            self.horizontalLayout_3.addWidget(self.label_3)
            self.restaurant_label = QtWidgets.QLabel(self.restaurant_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.restaurant_label.setFont(font)
            self.restaurant_label.setObjectName("restaurant_label")
            self.horizontalLayout_3.addWidget(self.restaurant_label)
            self.horizontalLayout_5.addWidget(self.restaurant_frame)
            self.price_frame = QtWidgets.QFrame(self.frame_4)
            self.price_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.price_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.price_frame.setObjectName("price_frame")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.price_frame)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.label_5 = QtWidgets.QLabel(self.price_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label_5")
            self.horizontalLayout_4.addWidget(self.label_5)
            self.pice_label = QtWidgets.QLabel(self.price_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.pice_label.setFont(font)
            self.pice_label.setObjectName("pice_label")
            self.horizontalLayout_4.addWidget(self.pice_label)
            self.horizontalLayout_5.addWidget(self.price_frame)
            self.amount_frame = QtWidgets.QFrame(self.frame_4)
            self.amount_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.amount_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.amount_frame.setObjectName("amount_frame")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.amount_frame)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            self.label_9 = QtWidgets.QLabel(self.amount_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_9.setFont(font)
            self.label_9.setObjectName("label_9")
            self.horizontalLayout_6.addWidget(self.label_9)
            self.amount_label = QtWidgets.QLabel(self.amount_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.amount_label.setFont(font)
            self.amount_label.setObjectName("amount_label")
            self.horizontalLayout_6.addWidget(self.amount_label)
            self.horizontalLayout_5.addWidget(self.amount_frame)
            self.total_frame = QtWidgets.QFrame(self.frame_4)
            self.total_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.total_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.total_frame.setObjectName("total_frame")
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.total_frame)
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")
            self.label_11 = QtWidgets.QLabel(self.total_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_11.setFont(font)
            self.label_11.setObjectName("label_11")
            self.horizontalLayout_7.addWidget(self.label_11)
            self.total_price_label = QtWidgets.QLabel(self.total_frame)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.total_price_label.setFont(font)
            self.total_price_label.setObjectName("total_price_label")
            self.horizontalLayout_7.addWidget(self.total_price_label)
            self.horizontalLayout_5.addWidget(self.total_frame)
            self.verticalLayout_4.addWidget(self.frame_4)
            self.verticalLayout_2.addWidget(self.frame_2)
            self.comment_btn_frame = QtWidgets.QFrame(self.frame)
            self.comment_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.comment_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.comment_btn_frame.setObjectName("comment_btn_frame")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.comment_btn_frame)
            self.verticalLayout_3.setContentsMargins(7, 7, 7, 7)
            self.verticalLayout_3.setSpacing(0)
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.comment_btn = QtWidgets.QPushButton(self.comment_btn_frame)
            self.comment_btn.clicked.connect(partial(Ui_privious_order.comment_page_runner, self,food_id))
            self.comment_btn.setObjectName("comment_btn")
            self.verticalLayout_3.addWidget(self.comment_btn)
            self.verticalLayout_2.addWidget(self.comment_btn_frame, 0, QtCore.Qt.AlignHCenter)
            self.verticalLayout_5.addWidget(self.frame)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.scrollArea)
            privious_order.setCentralWidget(self.centralwidget)

            self.retranslateUi(privious_order, i)
            QtCore.QMetaObject.connectSlotsByName(privious_order)

    def retranslateUi(self, privious_order, info):
        """
        this function will use information that has been send and get other needed information from
        database and retranslate the ui
        """
        price = info[6]
        amount = info[5]
        db_cursor = Ui_privious_order.my_db.cursor()
        db_cursor.execute(f"SELECT food_name FROM foodsofrestaurant WHERE food_id = {info[3]}")
        food_name = db_cursor.fetchall()[0][0]
        db_cursor.execute(f"SELECT restaurant_name FROM restuarantinfo WHERE restaurant_id = {info[1]}")
        restaurant_name = db_cursor.fetchall()[0][0]
        _translate = QtCore.QCoreApplication.translate
        privious_order.setWindowTitle(_translate("privious_order", "Previous Orders"))
        self.label.setText(_translate("privious_order", "Name :"))
        self.name_label.setText(_translate("privious_order", f"{food_name}"))
        self.label_3.setText(_translate("privious_order", "restaurant :"))
        self.restaurant_label.setText(_translate("privious_order", f"{restaurant_name}"))
        self.label_5.setText(_translate("privious_order", "price :"))
        self.pice_label.setText(_translate("privious_order", f"{price}"))
        self.label_9.setText(_translate("privious_order", "amount :"))
        self.amount_label.setText(_translate("privious_order", f"{amount}"))
        self.label_11.setText(_translate("privious_order", "Total Price :"))
        self.total_price_label.setText(_translate("privious_order", f"{price * amount}$"))
        self.comment_btn.setText(_translate("privious_order", "Comment this food"))


    def previous_order_runner (self) :
        self.privious_order = QtWidgets.QMainWindow()
        self.ui = Ui_privious_order()
        self.ui.setupUi(self.privious_order, self.customer_id)
        self.privious_order.show()








class Ui_cart(object):
    """
    Thsi class will get the information of orders 
    from database and put them on the ui and then 
    in it user can eather cancel the order or pay the order
    """
    mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
    def setupUi(self, MainWindow, customer_id):
        mydb = Ui_cart.mydb
        mydb_cursor = mydb.cursor()
        self.customer_id = customer_id
        #getting information from orders table based on customer_id and status o waiting
        mydb_cursor.execute(f"SELECT * FROM orders WHERE customer_id = {customer_id} and status = 'waiting'")
        orders = mydb_cursor.fetchall()
        self.orders = orders
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(734, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    color :#f7c55d;\n"
"    }\n"
"#centralwidget {\n"
"    background-color :#0f0f0f;\n"
"    }\n"
"#canceling_btn, #finaliz_btn{\n"
"    background-color :#f7c55d;\n"
"    color :#292929;\n"
"    border:none;\n"
"    }\n"
"#finalize_btn_frame, #cancel_btn_frame{\n"
"    background-color :#f7c55d;\n"
"    border-radius  : 5px;\n"
"    background-color :;\n"
"    }\n"
"#scrollAreaWidgetContents {\n"
"    background-color :#292929;\n"
"\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
        self.info_frame.setSizePolicy(sizePolicy)
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.info_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 708, 523))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        #itterating throgh the orders and setting up ui for each one of them
        for i in orders :
            self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.frame_2 = QtWidgets.QFrame(self.frame)
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label = QtWidgets.QLabel(self.frame_2)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.horizontalLayout_2.addWidget(self.label)
            self.name_label = QtWidgets.QLabel(self.frame_2)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.name_label.setFont(font)
            self.name_label.setObjectName("name_label")
            self.horizontalLayout_2.addWidget(self.name_label)
            self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
            self.frame_3 = QtWidgets.QFrame(self.frame)
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.label_3 = QtWidgets.QLabel(self.frame_3)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label_3")
            self.horizontalLayout_3.addWidget(self.label_3)
            self.price_btn = QtWidgets.QLabel(self.frame_3)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.price_btn.setFont(font)
            self.price_btn.setObjectName("price_btn")
            self.horizontalLayout_3.addWidget(self.price_btn)
            self.horizontalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft)
            self.frame_4 = QtWidgets.QFrame(self.frame)
            self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_4.setObjectName("frame_4")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.label_5 = QtWidgets.QLabel(self.frame_4)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label_5")
            self.horizontalLayout_4.addWidget(self.label_5)
            self.amount_label = QtWidgets.QLabel(self.frame_4)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.amount_label.setFont(font)
            self.amount_label.setObjectName("amount_label")
            self.horizontalLayout_4.addWidget(self.amount_label)
            self.horizontalLayout.addWidget(self.frame_4)
            self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout_2.addWidget(self.scrollArea)
            self.verticalLayout.addWidget(self.info_frame)
            self.retranslateUi(i)
            
        self.commands_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commands_frame.sizePolicy().hasHeightForWidth())
        self.commands_frame.setSizePolicy(sizePolicy)
        self.commands_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.commands_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.commands_frame.setObjectName("commands_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.commands_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cancel_btn_frame = QtWidgets.QFrame(self.commands_frame)
        self.cancel_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cancel_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cancel_btn_frame.setObjectName("cancel_btn_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.cancel_btn_frame)
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.canceling_btn = QtWidgets.QPushButton(self.cancel_btn_frame)
        self.canceling_btn.clicked.connect(self.canceling_error)
        self.canceling_btn.setObjectName("canceling_btn")
        self.horizontalLayout_6.addWidget(self.canceling_btn)
        self.horizontalLayout_5.addWidget(self.cancel_btn_frame, 0, QtCore.Qt.AlignVCenter)
        self.finalize_btn_frame = QtWidgets.QFrame(self.commands_frame)
        self.finalize_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.finalize_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.finalize_btn_frame.setObjectName("finalize_btn_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.finalize_btn_frame)
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.finaliz_btn = QtWidgets.QPushButton(self.finalize_btn_frame)
        self.finaliz_btn.clicked.connect(self.finalizing_runner)
        self.finaliz_btn.setObjectName("finaliz_btn")
        self.horizontalLayout_7.addWidget(self.finaliz_btn)
        self.horizontalLayout_5.addWidget(self.finalize_btn_frame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.commands_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslatebutton(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, info):
        food_id = info[3]
        db_cursor = Ui_cart.mydb.cursor()
        db_cursor.execute(f"SELECT * FROM foodsofrestaurant WHERE food_id = {food_id}")
        informations = db_cursor.fetchall()
        informations = informations[0]
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Name :"))
        self.name_label.setText(_translate("MainWindow", f"{informations[3]}"))
        self.label_3.setText(_translate("MainWindow", "price :"))
        self.price_btn.setText(_translate("MainWindow", f"{informations[7]}$"))
        self.label_5.setText(_translate("MainWindow", "amount :"))
        self.amount_label.setText(_translate("MainWindow", f"{info[5]}"))


    def retranslatebutton(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cart"))
        self.canceling_btn.setText(_translate("MainWindow", "Cancel the order"))
        self.finaliz_btn.setText(_translate("MainWindow", "Finalize the order"))

    def cart_runner(self, customer_id) :
        #in here we run the cart page but at first we will try to delete self.ui so ui
        #always be assigned to self so the cart alwaus be updated
        
        try :
            del self.ui
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_cart()
            self.ui.setupUi(self.MainWindow, customer_id)
            self.MainWindow.show()
        except :
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_cart()
            self.ui.setupUi(self.MainWindow, customer_id)
            self.MainWindow.show()
    
    def canceling_error(self) :
        orders = self.orders
        customer_id = self.customer_id
        db_cursor = Ui_cart.mydb.cursor()
        for order in orders :
            food_id = order[3]
            amount = order[5]
            db_cursor.execute(f"UPDATE foodsofrestaurant SET food_inventory = food_inventory + {amount} WHERE food_id = {food_id} ")
            Ui_cart.mydb.commit()
        db_cursor.execute(f"UPDATE orders SET status = 'canceled' WHERE customer_id = {customer_id}")
        Ui_cart.mydb.commit()
        Ui_password_not_valid.error_message_run(self, "Successfully canceled reload the page")

    def finalizing_runner (self): 
        """
        This function will send information to finalize the order
        """
        customer_id = self.customer_id
        Ui_paying.Ui_paying_runner(self, customer_id)




class Ui_dashboard(object):
    """
    This class will create ui  of dashboard which contains
    edit page
    cart
    order section
    previous orders
    search
    """
    @QtCore.pyqtSlot()
    def order_page_runner (self, _food_kind) :
            Ui_order_page.order_page_runner(self, _food_kind)
            return
    def setupUi(self, MainWindow, email_for_info):
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        #getting user picture_path so we can display it on the picture label and customer_id
        #so we can eather get information from database or change tables in database  
        
        mydb_cursor.execute(f"SELECT picture_path,customer_id FROM customer WHERE email = '{email_for_info}'")
        result = mydb_cursor.fetchall()
        result = result[0]
        picture_path = result[0]
        self.cusomer_id = result[1]
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1407, 912)
        self.mainwidget = QtWidgets.QWidget(MainWindow)
        self.mainwidget.setStyleSheet("*{\n"
"    color :#f7c55d;\n"
"    }\n"
"#mainwidget {\n"
"    background-color: #0f0f0f;\n"
"    }\n"
"#profileframe {\n"
"    background-color : #292929;\n"
"    }\n"
"\n"
"#infobtn_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius : 10px;\n"
"    }\n"
"#edit_info_btn{\n"
"    background-color :#f7c55d;\n"
"    color :#292929;\n"
"    border :none;\n"
"    }\n"
"#kebab_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius:20px;\n"
"    }\n"
"#kebab_btn{    \n"
"    color :#0f0f0f;\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    }\n"
"#pizza_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius:20px;\n"
"    }\n"
"#pizza_btn{    \n"
"    color :#0f0f0f;\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    }\n"
"#hamburger_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius:20px;\n"
"    }\n"
"#hamburger_btn{    \n"
"    color :#0f0f0f;\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    }\n"
"#others_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius:20px;\n"
"    }\n"
"#others_btn{    \n"
"    color :#0f0f0f;\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    }\n"
"#previous_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius:20px;\n"
"    }\n"
"#previous_btn{    \n"
"    color :#0f0f0f;\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    }\n"
"#cart_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius:20px;\n"
"    }\n"
"#cart_btn{\n"
"    color :#0f0f0f;\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    \n"
"    }\n"
"#search_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius : 10px\n"
"\n"
"    }\n"
"#search_btn{\n"
"    color :#0f0f0f;\n"
"    background-color :#f7c55d;\n"
"    border:none;\n"
"    }\n"
"#searchinput{\n"
"    border:none;\n"
"    background-color :#f7c55d;\n"
"    color:#0f0f0f;\n"
"    }")
        self.mainwidget.setObjectName("mainwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upperwidget = QtWidgets.QWidget(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperwidget.sizePolicy().hasHeightForWidth())
        self.upperwidget.setSizePolicy(sizePolicy)
        self.upperwidget.setObjectName("upperwidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.upperwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cart_frame = QtWidgets.QFrame(self.upperwidget)
        self.cart_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cart_frame.setObjectName("cart_frame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.cart_frame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cart_btn = QtWidgets.QPushButton(self.cart_frame)
        self.cart_btn.clicked.connect(self.cart_runner)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/shopping-cart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cart_btn.setIcon(icon)
        self.cart_btn.setObjectName("cart_btn")
        self.horizontalLayout_12.addWidget(self.cart_btn)
        self.horizontalLayout_11.addWidget(self.cart_frame, 0, QtCore.Qt.AlignLeft)
        self.search_frame = QtWidgets.QFrame(self.upperwidget)
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.search_frame)
        self.horizontalLayout_13.setContentsMargins(5, 0, 10, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.search_btn = QtWidgets.QPushButton(self.search_frame)
        self.search_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_13.addWidget(self.search_btn)
        self.horizontalLayout_11.addWidget(self.search_frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.upperwidget)
        self.lowerwidget = QtWidgets.QWidget(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerwidget.sizePolicy().hasHeightForWidth())
        self.lowerwidget.setSizePolicy(sizePolicy)
        self.lowerwidget.setObjectName("lowerwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.lowerwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.profileframe = QtWidgets.QFrame(self.lowerwidget)
        self.profileframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profileframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profileframe.setObjectName("profileframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.profileframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pictureframe = QtWidgets.QFrame(self.profileframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictureframe.sizePolicy().hasHeightForWidth())
        self.pictureframe.setSizePolicy(sizePolicy)
        self.pictureframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pictureframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pictureframe.setObjectName("pictureframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pictureframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.picturemain_frame = QtWidgets.QFrame(self.pictureframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picturemain_frame.sizePolicy().hasHeightForWidth())
        self.picturemain_frame.setSizePolicy(sizePolicy)
        self.picturemain_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picturemain_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picturemain_frame.setObjectName("picturemain_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.picturemain_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.picturemain_frame)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(600, 400))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(f"{picture_path}"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.verticalLayout_3.addWidget(self.picturemain_frame, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.pictureframe, 0, QtCore.Qt.AlignLeft)
        self.infoframe = QtWidgets.QFrame(self.profileframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoframe.sizePolicy().hasHeightForWidth())
        self.infoframe.setSizePolicy(sizePolicy)
        self.infoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoframe.setObjectName("infoframe")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.infoframe)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.name_frame = QtWidgets.QFrame(self.infoframe)
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.name_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.name_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.name_label = QtWidgets.QLabel(self.name_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.name_frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.infoframe)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.phonenumber_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.phonenumber_label.setFont(font)
        self.phonenumber_label.setObjectName("phonenumber_label")
        self.horizontalLayout_3.addWidget(self.phonenumber_label)
        self.verticalLayout_5.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.infoframe)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.email_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.horizontalLayout_4.addWidget(self.email_label)
        self.verticalLayout_5.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft)
        self.frame_4 = QtWidgets.QFrame(self.infoframe)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.idnumber_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.idnumber_label.setFont(font)
        self.idnumber_label.setObjectName("idnumber_label")
        self.horizontalLayout_5.addWidget(self.idnumber_label)
        self.verticalLayout_5.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft)
        self.infobtn_frame = QtWidgets.QFrame(self.infoframe)
        self.infobtn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infobtn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infobtn_frame.setObjectName("infobtn_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.infobtn_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.edit_info_btn = QtWidgets.QPushButton(self.infobtn_frame)
        self.edit_info_btn.setObjectName("edit_info_btn")
        self.edit_info_btn.clicked.connect(self.edit_page_run)
        self.horizontalLayout_6.addWidget(self.edit_info_btn)
        self.verticalLayout_5.addWidget(self.infobtn_frame, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.infoframe)
        self.horizontalLayout.addWidget(self.profileframe, 0, QtCore.Qt.AlignLeft)
        self.orderingframe = QtWidgets.QFrame(self.lowerwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderingframe.sizePolicy().hasHeightForWidth())
        self.orderingframe.setSizePolicy(sizePolicy)
        self.orderingframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.orderingframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.orderingframe.setObjectName("orderingframe")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.orderingframe)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.order_frame = QtWidgets.QFrame(self.orderingframe)
        self.order_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.order_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.order_frame.setObjectName("order_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.order_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.hamburger_frame = QtWidgets.QFrame(self.order_frame)
        self.hamburger_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hamburger_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hamburger_frame.setObjectName("hamburger_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.hamburger_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.hamburger_btn = QtWidgets.QPushButton(self.hamburger_frame)
        self.hamburger_btn.clicked.connect(lambda : Ui_dashboard.order_page_runner(self, "HAMBURGER"))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hamburger_btn.setFont(font)
        self.hamburger_btn.setObjectName("hamburger_btn")
        self.horizontalLayout_8.addWidget(self.hamburger_btn)
        self.gridLayout.addWidget(self.hamburger_frame, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.kebab_frame = QtWidgets.QFrame(self.order_frame)
        self.kebab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.kebab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.kebab_frame.setObjectName("kebab_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.kebab_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.kebab_btn = QtWidgets.QPushButton(self.kebab_frame)
        self.kebab_btn.clicked.connect(lambda : Ui_dashboard.order_page_runner(self, "KEBAB"))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kebab_btn.setFont(font)
        self.kebab_btn.setObjectName("kebab_btn")
        self.verticalLayout_7.addWidget(self.kebab_btn)
        self.gridLayout.addWidget(self.kebab_frame, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.pizza_frame = QtWidgets.QFrame(self.order_frame)
        self.pizza_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pizza_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pizza_frame.setObjectName("pizza_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.pizza_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pizza_btn = QtWidgets.QPushButton(self.pizza_frame)
        self.pizza_btn.clicked.connect(lambda : Ui_dashboard.order_page_runner(self, "PIZZA"))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pizza_btn.setFont(font)
        self.pizza_btn.setObjectName("pizza_btn")
        self.horizontalLayout_7.addWidget(self.pizza_btn, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.pizza_frame, 0, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.others_frame = QtWidgets.QFrame(self.order_frame)
        self.others_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.others_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.others_frame.setObjectName("others_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.others_frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.others_btn = QtWidgets.QPushButton(self.others_frame)
        self.others_btn.clicked.connect(lambda : Ui_dashboard.order_page_runner(self,"OTHERS"))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.others_btn.setFont(font)
        self.others_btn.setObjectName("others_btn")
        self.horizontalLayout_9.addWidget(self.others_btn)
        self.gridLayout.addWidget(self.others_frame, 1, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.order_frame)
        self.previousorder_frame = QtWidgets.QFrame(self.orderingframe)
        self.previousorder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.previousorder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.previousorder_frame.setObjectName("previousorder_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.previousorder_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.previous_frame = QtWidgets.QFrame(self.previousorder_frame)
        self.previous_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.previous_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.previous_frame.setObjectName("previous_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.previous_frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.previous_btn = QtWidgets.QPushButton(self.previous_frame)
        self.previous_btn.clicked.connect(self.previous_runner)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.previous_btn.setFont(font)
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout_10.addWidget(self.previous_btn)
        self.verticalLayout_8.addWidget(self.previous_frame, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.previousorder_frame)
        self.horizontalLayout.addWidget(self.orderingframe)
        self.verticalLayout.addWidget(self.lowerwidget)
        MainWindow.setCentralWidget(self.mainwidget)

        self.retranslateUi(MainWindow, email_for_info)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, email_for_info):
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        mydb_cursor.execute(f"SELECT * FROM customer WHERE email = '{email_for_info}'")
        result = mydb_cursor.fetchall()
        result = result[0]
        self.customer_id = result[0]
        self.first_name = result[1]
        self.last_name = result[2]
        self.email = email_for_info
        self.phone_number = result[3]
        self.id_number = result[5]
        self.password = result[6]
        self.picture_path = result[7]
        self.customer = customer(self.first_name, self.last_name, self.phone_number, self.email, self.id_number, self.password, self.picture_path)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cart_btn.setText(_translate("MainWindow", "Cart"))
        self.label.setText(_translate("MainWindow", "Name :"))
        self.name_label.setText(_translate("MainWindow", f"{result[1]} {result[2]}"))
        self.label_2.setText(_translate("MainWindow", "Phone number :"))
        self.phonenumber_label.setText(_translate("MainWindow", f"{result[3]}"))
        self.label_3.setText(_translate("MainWindow", "Email :"))
        self.email_label.setText(_translate("MainWindow", f"{email_for_info}"))
        self.label_4.setText(_translate("MainWindow", "ID number :"))
        self.idnumber_label.setText(_translate("MainWindow", f"{result[5]}"))
        self.edit_info_btn.setText(_translate("MainWindow", "Edit Information"))
        self.hamburger_btn.setText(_translate("MainWindow", "HAMBURGER"))
        self.kebab_btn.setText(_translate("MainWindow", "KEBAB"))
        self.pizza_btn.setText(_translate("MainWindow", "PIZZA"))
        self.others_btn.setText(_translate("MainWindow", "OTHERS"))
        self.previous_btn.setText(_translate("MainWindow", "Previous Orders"))

    def edit_page_run (self) :
        """
        This function will run edit page
        """
        Ui_edit_page.edit_page_runner(self, self.customer)

    def dashboard_run(self) :
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self.MainWindow, self.email)
        self.MainWindow.show()


    def cart_runner(self) :
        """
        This function will run the cart ui
        """
        Ui_cart.cart_runner(self, self.customer_id)
    def previous_runner(self) :
        """
        This function will run the previous order page
        """
        Ui_privious_order.previous_order_runner(self)

class Ui_edit_page(object):
    """
    This class gets some information and by using that information goes to the database
    and recieves other information is needed and enable user to edit those information
    """
    
    def setupUi(self, MainWindow, customer_object):
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        #getting picture_path of user so it can display it on the ui
        mydb_cursor.execute(f"SELECT picture_path FROM customer WHERE email = '{customer_object.email}'")
        result = mydb_cursor.fetchall()
        result = result[0]
        picture_path = result[0]
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(558, 1013)
        self.edit_profile_widget = QtWidgets.QWidget(MainWindow)

        self.edit_profile_widget.setStyleSheet("*{\n"
"    color :#f7c55d;\n"
"    }\n"
"#edit_profile_widget{\n"
"    background-color: #0f0f0f;\n"
"    }\n"
"\n"
"#profileframe {\n"
"    background-color : #292929;\n"
"    }\n"
"\n"
"#submit_btn_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius : 10px;\n"
"    }\n"
"#submit_btn{\n"
"    background-color :#f7c55d;\n"
"    color :#292929;\n"
"    border :none;\n"
"    }\n"
"#first_name_input , #last_name_input, #phonenumber_input, #email_input, #id_number_input, #password_input, #picture_path_input{\n"
"    background-color : #292929;\n"
"\n"
"    }\n"
"    ")
        self.edit_profile_widget.setObjectName("edit_profile_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.edit_profile_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.profileframe = QtWidgets.QFrame(self.edit_profile_widget)
        self.profileframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profileframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profileframe.setObjectName("profileframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.profileframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pictureframe = QtWidgets.QFrame(self.profileframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictureframe.sizePolicy().hasHeightForWidth())
        self.pictureframe.setSizePolicy(sizePolicy)
        self.pictureframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pictureframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pictureframe.setObjectName("pictureframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pictureframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.picturemain_frame = QtWidgets.QFrame(self.pictureframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picturemain_frame.sizePolicy().hasHeightForWidth())
        self.picturemain_frame.setSizePolicy(sizePolicy)
        self.picturemain_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picturemain_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picturemain_frame.setObjectName("picturemain_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.picturemain_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.picturemain_frame)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(600, 400))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(f"{picture_path}"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.verticalLayout_3.addWidget(self.picturemain_frame, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.pictureframe, 0, QtCore.Qt.AlignLeft)
        self.infoframe = QtWidgets.QFrame(self.profileframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoframe.sizePolicy().hasHeightForWidth())
        self.infoframe.setSizePolicy(sizePolicy)
        self.infoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoframe.setObjectName("infoframe")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.infoframe)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.name_frame = QtWidgets.QFrame(self.infoframe)
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.name_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.name_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.first_name_input = QtWidgets.QLineEdit(self.name_frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.first_name_input.setFont(font)
        self.first_name_input.setObjectName("first_name_input")
        self.horizontalLayout_2.addWidget(self.first_name_input)
        self.verticalLayout_5.addWidget(self.name_frame)
        self.frame = QtWidgets.QFrame(self.infoframe)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.last_name_input = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.last_name_input.setFont(font)
        self.last_name_input.setObjectName("last_name_input")
        self.horizontalLayout_6.addWidget(self.last_name_input)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.infoframe)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.phonenumber_input = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.phonenumber_input.setFont(font)
        self.phonenumber_input.setObjectName("phonenumber_input")
        self.horizontalLayout_3.addWidget(self.phonenumber_input)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.infoframe)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.email_input = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_input.setFont(font)
        self.email_input.setObjectName("email_input")
        self.horizontalLayout_4.addWidget(self.email_input)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.infoframe)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.id_number_input = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.id_number_input.setFont(font)
        self.id_number_input.setObjectName("id_number_input")
        self.horizontalLayout_5.addWidget(self.id_number_input)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.infoframe)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.password_input = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_input.setFont(font)
        self.password_input.setObjectName("password_input")
        self.horizontalLayout_8.addWidget(self.password_input)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.infoframe)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.picture_path_input = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.picture_path_input.setFont(font)
        self.picture_path_input.setObjectName("picture_path_input")
        self.horizontalLayout_7.addWidget(self.picture_path_input)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.submit_btn_frame = QtWidgets.QFrame(self.infoframe)
        self.submit_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.submit_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.submit_btn_frame.setObjectName("submit_btn_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.submit_btn_frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.submit_btn = QtWidgets.QPushButton(self.submit_btn_frame)
        self.submit_btn.setObjectName("submit_btn")

        def submit() :
            """
            This function will get information that has been entered to the lineedit 
            and set them to the customer information in database wich means it technically 
            update data 
            """
            print("clicked")
            mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
            mydb_cursor = mydb.cursor()
            mydb_cursor.execute("SELECT email, password FROM customer")
            customers_info = mydb_cursor.fetchall()
            mydb_cursor.execute("SELECT email, password FROM manager")
            managers_info = mydb_cursor.fetchall ()
            first_name = self.first_name_input.text().strip()
            last_name = self.last_name_input.text().strip()
            phone_number = self.phonenumber_input.text().strip()
            cemail = self.email_input.text().strip()
            id_number = self.id_number_input.text().strip()
            password = self.password_input.text().strip()
            #validating the picture path
            try :
                picture_path = self.picture_path_input.text().strip()
                img = Image.open(picture_path)
            except :
                picture_path =  "profilepicture.png"
            checking = True
            numbers = "123456789"
            lowercase_words = "abcdefghigklmnopqrstuvwxyz"
            uppercase_words = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
            characters = "!@#$%^&*"
            #in here on we will check the inputs as we did in the sign up
            if len(first_name) == 0 or len(last_name) == 0 or len(cemail) == 0 or len(password) == 0  or len(phone_number) == 0 or len(picture_path) == 0 :
                Ui_input_error.error_message_run(self)
                checking = False
                return
            #displaying propper message if ID nubmer is not right
            if len(id_number) != 10:
                Ui_id_nubmer_not_valid.error_message_run(self)
                checking = False
                return
            for letter in lowercase_words :
                if letter in id_number :
                    Ui_id_nubmer_not_valid.error_message_run(self)
                    checking = False
                    return
            for letter in uppercase_words :
                if letter in id_number :
                    Ui_id_nubmer_not_valid.error_message_run(self)
                    checking = False
                    return
            for character in characters :
                if character in id_number :
                    Ui_id_nubmer_not_valid.error_message_run(self)
                    checking = False
                    return
            #displaying propper mesage if names aren't valid
            for character in characters :
                if character in first_name or character in last_name :
                    Ui_name_not_valid.error_message_run(self)
                    checking = False
                    return
            for number in numbers :
                if number in first_name or number in last_name:
                    Ui_name_not_valid.error_message_run(self)
                    checking = False
                    return
            #checking email address
            pat_email = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if not (re.match(pat_email, cemail)):
                Ui_email_not_valid.error_message_run(self)
                checking = False
                return
            for email_tupe in managers_info:
                for email in email_tupe :
                    if email == self.email_input.text().strip().lower() and cemail != self.email:
                        Ui_password_not_valid.error_message_run(self, "This email already exist in database")
                        checking = False
                        return
            for email_tupe in customers_info:
                for email in email_tupe :
                    if email == self.email_input.text().strip().lower() and cemail != self.email :
                        Ui_password_not_valid.error_message_run(self, "This email already exist in database")
                        checking = False
                        return
                
            #checking phone number 
            regex_phone = re.compile(r'(?:\+\d{2})?\d{10,11}')
            if not(re.match(regex_phone, phone_number)):
                Ui_phone_number_not_valid.error_message_run(self)
                checking = False
                return
            if len(phone_number) > 14  or len(phone_number) < 10:
                Ui_phone_number_not_valid.error_message_run(self)
                checking = False
                return
            #checking password
            if len(password) < 8 :
                Ui_password_not_valid.error_message_run(self, "Your password must contain at least 8 characters")
                checking = False
                return
            if not any(char in password for char in characters ) :
                Ui_password_not_valid.error_message_run(self, "Your password must contain at least one special character")
                checking = False
                return
            if not any(char.isupper() for char in password) :
                Ui_password_not_valid.error_message_run(self, "Your password must contain at least one uppercase letter")
                checking = False
                return
            if not any(char.islower() for char in password) :
                Ui_password_not_valid.error_message_run(self, "Your password must contain at least one lowercase letter")
                checking = False
                return
            if not any(char.isdigit() for char in password) :
                Ui_password_not_valid.error_message_run(self, "Your password must contain at least one number")
                checking = False
                return
            
            #Updatinf informations in database by creating a object from custumer class
            if checking :
                mydb_cursor.execute(f"UPDATE customer SET first_name = '{first_name}', last_name = '{last_name}', phone_number = '{phone_number}', email = '{cemail}', id_number = '{id_number}', password = '{password}', picture_path = '{picture_path}' WHERE email = '{self.email}'")
                mydb.commit()
                #opening the dashboard again
                Ui_dashboard.dashboard_run(self)
        self.submit_btn.clicked.connect(submit)
 
        self.horizontalLayout_9.addWidget(self.submit_btn)
        self.verticalLayout_5.addWidget(self.submit_btn_frame)
        self.verticalLayout_2.addWidget(self.infoframe)
        self.horizontalLayout.addWidget(self.profileframe)
        MainWindow.setCentralWidget(self.edit_profile_widget)

        self.retranslateUi(MainWindow, customer_object)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, customer_object):
        _translate = QtCore.QCoreApplication.translate
        self.email = customer_object.email
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "First Name :"))
        self.first_name_input.setText(_translate("MainWindow", f"{customer_object.first_name}"))
        self.label_6.setText(_translate("MainWindow", "Last Name :"))
        self.last_name_input.setText(_translate("MainWindow", f"{customer_object.last_name}"))
        self.label_2.setText(_translate("MainWindow", "Phone number :"))
        self.phonenumber_input.setText(_translate("MainWindow", f"{customer_object.phone_number}"))
        self.label_3.setText(_translate("MainWindow", "Email :"))
        self.email_input.setText(_translate("MainWindow", f"{customer_object.email}"))
        self.label_4.setText(_translate("MainWindow", "ID number :"))
        self.id_number_input.setText(_translate("MainWindow", f"{customer_object.Id_number}"))
        self.label_8.setText(_translate("MainWindow", "Password : "))
        self.password_input.setText(_translate("MainWindow", f"{customer_object.password}"))
        self.label_10.setText(_translate("MainWindow", "Picture Path : "))
        self.picture_path_input.setText(_translate("MainWindow", f"{customer_object.picture_path}"))
        self.submit_btn.setText(_translate("MainWindow", "Submit"))

    def edit_page_runner(self, customer_object) :
        self.MainWindow = QtWidgets.QMainWindow()
        ui = Ui_edit_page()
        ui.setupUi(self.MainWindow, customer_object)
        self.MainWindow.show()