import sys 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from managerlatestversion import Ui_MainWindow


class MainWindow:
    def __init__(self, restaurant_id):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
         
        self.ui.setupUi(self.main_win, restaurant_id)

        self.ui.stackedWidget.setCurrentWidget(self.ui.profile_page)
        self.ui.edit_restaurant_info_btn.clicked.connect(self.ui.open_edit_ui)


    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
