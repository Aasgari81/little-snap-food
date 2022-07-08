from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as msc
from functools import partial
from error_ui import *

class Ui_order_amount(object):
    """
    This class will create a ui that will finallize the cosen food and get the amount of food
    from the user and creates a row for that order in order table
    """
    mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
    mydb_cursor = mydb.cursor()
    mydb_cursor.execute("select order_number from orders ORDER BY order_number DESC LIMIT 1")
    order_nubmer = mydb_cursor.fetchall()[0][0] + 1

    def setupUi(self, order_amount , restaurant_id, customer_id, food_id, price):
        self.price = price
        self.mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = self.mydb.cursor()
        mydb_cursor.execute(f"SELECT food_inventory FROM foodsofrestaurant WHERE food_id = {food_id}")
        inventory = mydb_cursor.fetchall()
        self.inventory = inventory[0][0]
        self.food_id = food_id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        order_amount.setObjectName("order_amount")
        order_amount.resize(410, 209)
        self.centralwidget = QtWidgets.QWidget(order_amount)
        self.centralwidget.setStyleSheet("* {\n"
"    color :#f7c55d;\n"
"    }\n"
"#centralwidget {\n"
"    background-color :#0f0f0f;\n"
"    }\n"
"#number_of_order_spinbox {\n"
"    background-color :#292929;\n"
"    }\n"
"#order_btn_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius : 10px;\n"
"    }\n"
"    \n"
"#order_btn{\n"
"    background-color :#f7c55d;\n"
"    border : none;\n"
"    color :#0f0f0f,\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.amount_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amount_frame.sizePolicy().hasHeightForWidth())
        self.amount_frame.setSizePolicy(sizePolicy)
        self.amount_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.amount_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.amount_frame.setObjectName("amount_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.amount_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.amount_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.amount_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.number_of_order_spinbox = QtWidgets.QSpinBox(self.frame)
        self.number_of_order_spinbox.setObjectName("number_of_order_spinbox")
        self.horizontalLayout.addWidget(self.number_of_order_spinbox)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.amount_frame)
        self.order_btn_frame = QtWidgets.QFrame(self.centralwidget)
        self.order_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.order_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.order_btn_frame.setObjectName("order_btn_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.order_btn_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.order_btn = QtWidgets.QPushButton(self.order_btn_frame)
        self.order_btn.clicked.connect(self.ordering_proccess)
        self.order_btn.setObjectName("order_btn")
        self.verticalLayout_3.addWidget(self.order_btn)
        self.verticalLayout.addWidget(self.order_btn_frame)
        order_amount.setCentralWidget(self.centralwidget)

        self.retranslateUi(order_amount)
        QtCore.QMetaObject.connectSlotsByName(order_amount)

    def retranslateUi(self, order_amount):
        _translate = QtCore.QCoreApplication.translate
        order_amount.setWindowTitle(_translate("order_amount", "Order amount"))
        self.label.setText(_translate("order_amount", "Enter the amount you want : "))
        self.order_btn.setText(_translate("order_amount", "Order"))


    def order_amount_runner (self, restaurant_id, customer_id, food_id, price) :    
        self.order_amount = QtWidgets.QMainWindow()
        self.ui = Ui_order_amount()
        self.ui.setupUi(self.order_amount, restaurant_id, customer_id, food_id, price)
        self.order_amount.show()
    def ordering_proccess (self) :
        """
        This function will set the order in orders table
        """
        print("clicked")
        price = self.price
        amount_of_order = self.number_of_order_spinbox.value()
        if amount_of_order == 0 :
            Ui_password_not_valid.error_message_run(self, "The input amount is zero try it with a number")
            return
        elif self.inventory - amount_of_order < 0 :
            Ui_password_not_valid.error_message_run(self, "The inventory of food is not enough")
            return
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        mydb_cursor.execute(f"INSERT INTO orders VALUES ( {Ui_order_amount.order_nubmer}, {self.restaurant_id}, {self.customer_id}, {self.food_id}, 'waiting', {amount_of_order}, {price})")
        mydb.commit()
        mydb_cursor.execute(f"UPDATE foodsofrestaurant SET food_inventory = {self.inventory - amount_of_order} WHERE food_id = {self.food_id}")
        mydb.commit()
        Ui_password_not_valid.error_message_run(self, "The order was successfully placed")
        Ui_order_amount.order_nubmer += 1
class Ui_order_from_restaurant(object):
    """
    This class creates a ui that displayes the menuof restaurant and enabled the user to order
    """
    def setupUi(self, MainWindow, restaurant_id, customer_id):
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        #getting the foods of restaurant 
        mydb_cursor.execute(f"SELECT * FROM foodsofrestaurant WHERE  restuarant_id = {restaurant_id} ")
        foods_result = mydb_cursor.fetchall()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(852, 693)
        self.order_from_restaurant_widget = QtWidgets.QWidget(MainWindow)
        self.order_from_restaurant_widget.setStyleSheet("*{\n"
"    color :#f7c55d;\n"
"    }\n"
"#order_from_restaurant_widget{\n"
"    background-color :#0f0f0f;\n"
"    }\n"
"#comment_scrollarea, #food_scrollarea, #comment_text_browser, #explanation_text_browser, #ingredient_text_browser, #comments_text_browser {\n"
"        background-color : #292929;\n"
"    }\n"
"#order_btn_frame {\n"
"    background-color :#f7c55d;\n"
"    border-radius  : 10px;\n"
"    }\n"
"#order_this_food_btn {\n"
"    background-color :#f7c55d;\n"
"    color :#292929;\n"
"    border:none;\n"
"    }")
        self.order_from_restaurant_widget.setObjectName("order_from_restaurant_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.order_from_restaurant_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.order_from_restaurant_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.food_scrollarea = QtWidgets.QWidget()
        self.food_scrollarea.setGeometry(QtCore.QRect(0, 0, 1392, 835))
        self.food_scrollarea.setObjectName("food_scrollarea")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.food_scrollarea)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        #iterating through the founded informatioin
        for i in foods_result :
                self.food_id = i[1]
                self.frame = QtWidgets.QFrame(self.food_scrollarea)
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.frame_3 = QtWidgets.QFrame(self.frame)
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.food_info_frame = QtWidgets.QFrame(self.frame_3)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.food_info_frame.sizePolicy().hasHeightForWidth())
                self.food_info_frame.setSizePolicy(sizePolicy)
                self.food_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.food_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.food_info_frame.setObjectName("food_info_frame")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.food_info_frame)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.name_frame = QtWidgets.QFrame(self.food_info_frame)
                self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.name_frame.setObjectName("name_frame")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.name_frame)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label = QtWidgets.QLabel(self.name_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.horizontalLayout_3.addWidget(self.label)
                self.name_label = QtWidgets.QLabel(self.name_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                self.name_label.setFont(font)
                self.name_label.setObjectName("name_label")
                self.horizontalLayout_3.addWidget(self.name_label)
                self.verticalLayout_3.addWidget(self.name_frame, 0, QtCore.Qt.AlignLeft)
                self.price_frame = QtWidgets.QFrame(self.food_info_frame)
                self.price_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.price_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.price_frame.setObjectName("price_frame")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.price_frame)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.label_3 = QtWidgets.QLabel(self.price_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.horizontalLayout_4.addWidget(self.label_3)
                self.price_label = QtWidgets.QLabel(self.price_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                self.price_label.setFont(font)
                self.price_label.setObjectName("price_label")
                self.horizontalLayout_4.addWidget(self.price_label)
                self.verticalLayout_3.addWidget(self.price_frame, 0, QtCore.Qt.AlignLeft)
                self.ingredient_frame = QtWidgets.QFrame(self.food_info_frame)
                self.ingredient_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.ingredient_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.ingredient_frame.setObjectName("ingredient_frame")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.ingredient_frame)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.label_5 = QtWidgets.QLabel(self.ingredient_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.horizontalLayout_5.addWidget(self.label_5)
                self.ingredient_text_browser = QtWidgets.QTextBrowser(self.ingredient_frame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.ingredient_text_browser.sizePolicy().hasHeightForWidth())
                self.ingredient_text_browser.setSizePolicy(sizePolicy)
                self.ingredient_text_browser.setObjectName("ingredient_text_browser")
                self.horizontalLayout_5.addWidget(self.ingredient_text_browser)
                self.verticalLayout_3.addWidget(self.ingredient_frame, 0, QtCore.Qt.AlignLeft)
                self.category_frame = QtWidgets.QFrame(self.food_info_frame)
                self.category_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.category_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.category_frame.setObjectName("category_frame")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.category_frame)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.label_7 = QtWidgets.QLabel(self.category_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_7.setFont(font)
                self.label_7.setObjectName("label_7")
                self.horizontalLayout_6.addWidget(self.label_7)
                self.category_label = QtWidgets.QLabel(self.category_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                self.category_label.setFont(font)
                self.category_label.setObjectName("category_label")
                self.horizontalLayout_6.addWidget(self.category_label)
                self.verticalLayout_3.addWidget(self.category_frame, 0, QtCore.Qt.AlignLeft)
                self.explanation_frame = QtWidgets.QFrame(self.food_info_frame)
                self.explanation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.explanation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.explanation_frame.setObjectName("explanation_frame")
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.explanation_frame)
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.label_10 = QtWidgets.QLabel(self.explanation_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_10.setFont(font)
                self.label_10.setObjectName("label_10")
                self.horizontalLayout_7.addWidget(self.label_10)
                self.explanation_text_browser = QtWidgets.QTextBrowser(self.explanation_frame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.explanation_text_browser.sizePolicy().hasHeightForWidth())
                self.explanation_text_browser.setSizePolicy(sizePolicy)
                self.explanation_text_browser.setObjectName("explanation_text_browser")
                self.horizontalLayout_7.addWidget(self.explanation_text_browser)
                self.verticalLayout_3.addWidget(self.explanation_frame, 0, QtCore.Qt.AlignLeft)
                self.comments_frame = QtWidgets.QFrame(self.food_info_frame)
                self.comments_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.comments_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.comments_frame.setObjectName("comments_frame")
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.comments_frame)
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                self.label_9 = QtWidgets.QLabel(self.comments_frame)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.label_9.setFont(font)
                self.label_9.setObjectName("label_9")
                self.horizontalLayout_8.addWidget(self.label_9)
                self.comments_text_browser = QtWidgets.QTextBrowser(self.comments_frame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.comments_text_browser.sizePolicy().hasHeightForWidth())
                self.comments_text_browser.setSizePolicy(sizePolicy)
                self.comments_text_browser.setObjectName("comments_text_browser")
                self.horizontalLayout_8.addWidget(self.comments_text_browser)
                self.verticalLayout_3.addWidget(self.comments_frame, 0, QtCore.Qt.AlignLeft)
                self.order_btn_frame = QtWidgets.QFrame(self.food_info_frame)
                self.order_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.order_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.order_btn_frame.setObjectName("order_btn_frame")
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.order_btn_frame)
                self.horizontalLayout_10.setContentsMargins(5, 10, 5, 10)
                self.horizontalLayout_10.setSpacing(0)
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                self.order_this_food_btn = QtWidgets.QPushButton(self.order_btn_frame)
                self.order_this_food_btn.clicked.connect(partial(Ui_order_from_restaurant.food_order_runner, self, restaurant_id, customer_id, i[1], i[7]))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.order_this_food_btn.sizePolicy().hasHeightForWidth())
                self.order_this_food_btn.setSizePolicy(sizePolicy)
                self.order_this_food_btn.setObjectName("order_this_food_btn")
                self.horizontalLayout_10.addWidget(self.order_this_food_btn)
                self.verticalLayout_3.addWidget(self.order_btn_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.verticalLayout_6.addWidget(self.food_info_frame)
                self.horizontalLayout.addWidget(self.frame_3)
                self.verticalLayout_5.addWidget(self.frame)
                self.scrollArea.setWidget(self.food_scrollarea)
                self.verticalLayout.addWidget(self.scrollArea)
                MainWindow.setCentralWidget(self.order_from_restaurant_widget)

                self.retranslateUi(MainWindow, i)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, info):
        comments = info[8]
        comments = comments.replace("/", "\n-------------------------------\n")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Order from tehran restaurant"))
        self.label.setText(_translate("MainWindow", "Name of food :"))
        self.name_label.setText(_translate("MainWindow", f"{info[3]}"))
        self.label_3.setText(_translate("MainWindow", "Price :"))
        self.price_label.setText(_translate("MainWindow", f"{info[7]}$"))
        self.label_5.setText(_translate("MainWindow", "Ingredient :"))
        self.ingredient_text_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{info[5]}</span></p>\n"
"</body></html>"))
        self.label_7.setText(_translate("MainWindow", "Category :"))
        self.category_label.setText(_translate("MainWindow", "Sandwich"))
        self.label_10.setText(_translate("MainWindow", "Explanation :"))
        self.explanation_text_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">{info[9]}</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Comments :"))
        self.comments_text_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{comments}</span></p></body></html>"))
        self.order_this_food_btn.setText(_translate("MainWindow", "Order This food"))


    def order_from_restauranu_runner(self, restaurant_id) :
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_order_from_restaurant()
        self.ui.setupUi(self.MainWindow, restaurant_id, self.customer_id)
        self.MainWindow.show()
    def food_order_runner (self, restaurant_id, customer_id, food_id, price) :
        """
        this will run the ui of ordering the food
        """
        Ui_order_amount.order_amount_runner(self, restaurant_id, customer_id, food_id, price)



class Ui_order_page(object):
    """
    Thid will create ui which contains the proper restaurant 
    """
    def setupUi(self, MainWindow, food_kind, customer_id):
        self.customer_id = customer_id
        #connecting to database
        mydb = msc.connect(host = "localhost", user = "root", password = "Aliasgari@1381", database = "little_snap_food")
        mydb_cursor = mydb.cursor()
        food_restaurant = {"PIZZA" : "SELECT * FROM restuarantinfo WHERE pizza = 'yes'", "HAMBURGER" : "SELECT * FROM restuarantinfo WHERE hamburger = 'yes'", "KEBAB" : "SELECT * FROM restuarantinfo WHERE kebab = 'yes'", "OTHERS" : "SELECT * FROM restuarantinfo"}
        mydb_cursor.execute(food_restaurant[food_kind])
        #getting proper restaurant from database
        restaurants = mydb_cursor.fetchall() 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 860)
        self.order_widget = QtWidgets.QWidget(MainWindow)
        self.order_widget.setStyleSheet("*{\n"
"    color :#f7c55d;\n"
"    }\n"
"#order_widget {\n"
"    background-color: #0f0f0f;\n"
"    }\n"
"#scrollarea_for_order, #scrollAreaWidgetContents{\n"
"    background-color : #292929;\n"
"    }\n"
"#order_btn, #order_btn_2,#order_btn_3{\n"
"    border : none;\n"
"    background-color :#f7c55d;\n"
"    color : #292929;\n"
"    }\n"
"#order_btn_frame, #order_btn_frame_2, #order_btn_frame_3 {\n"
"    background-color : #f7c55d;;\n"
"    border-radius : 10px;\n"
"    }\n"
"")
        self.order_widget.setObjectName("order_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.order_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollarea_for_order = QtWidgets.QScrollArea(self.order_widget)
        self.scrollarea_for_order.setWidgetResizable(True)
        self.scrollarea_for_order.setObjectName("scrollarea_for_order")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1227, 836))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #iterating through fonded restaurant
        for i in restaurants :
            restaurant = Restaurant(i[1], i[2], i[3], i[4], i[5], i[0])
            self.restaurant_id = restaurant.restaurant_id
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
            self.order_btn.clicked.connect(partial(Ui_order_page.restaurant_menu, self, self.restaurant_id, self.customer_id))
            self.order_btn.setObjectName("order_btn")
            self.horizontalLayout_5.addWidget(self.order_btn)
            self.verticalLayout_4.addWidget(self.order_btn_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.horizontalLayout.addWidget(self.info_frame)
            self.verticalLayout_2.addWidget(self.fast_food_frame)
            self.scrollarea_for_order.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.scrollarea_for_order)
            MainWindow.setCentralWidget(self.order_widget)
            self.retranslateUi(MainWindow, i)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)


       

    
    
    def retranslateUi(self, MainWindow, i):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Order"))
        self.label_2.setText(_translate("MainWindow", "Restaurant name :"))
        self.restaurant_label.setText(_translate("MainWindow", f"{i[1]}"))
        self.label_4.setText(_translate("MainWindow", "category :"))
        self.category_label.setText(_translate("MainWindow", f"{i[3]}"))
        self.label_6.setText(_translate("MainWindow", "District :"))
        self.district_label.setText(_translate("MainWindow", f"{i[2]}"))
        self.order_btn.setText(_translate("MainWindow", "Order from this restaurant"))
    def order_page_runner(self, food_kind : str) :
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_order_page()
        self.ui.setupUi(self.MainWindow, food_kind, self.customer_id)
        self.MainWindow.show()
    
    def restaurant_menu (self, restaurant_id, customer_id) :
        Ui_order_from_restaurant.order_from_restauranu_runner(self, restaurant_id)