# import sys
# from datetime import datetime
# from PyQt5.QtCore import QDate, Qt, QDateTime
# from PyQt5.QtWidgets import QLabel, QDateEdit, QMainWindow, QApplication, QCalendarWidget
#
#
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         current_year = datetime.now().year
#         current_month = datetime.now().month
#         current_day = datetime.now().day
#         min_date = (current_year, current_month, current_day)
#         max_date = QDate(current_year + 1, current_month, current_day)
#
#         # DateEdit widget
#         self.bg_create_expire_date = QDateEdit(calendarPopup=True)
#         self.bg_create_expire_date.setDisplayFormat("dd/MM/yyyy")
#         self.bg_create_expire_date.setMinimumDate(min_date)
#         self.bg_create_expire_date.setMaximumDate(max_date)
#         self.bg_create_expire_date.setDate(max_date)
#         self.bg_create_expire_date.setFixedWidth(105)
#
#         # Calendar widget
#         self.bg_create_expire_date = QCalendarWidget()
#         self.bg_create_expire_date.setGridVisible(True)
#         self.bg_create_expire_date.setMinimumDate(min_date)
#         self.bg_create_expire_date.setMaximumDate(max_date)
#         self.bg_create_expire_date.setSelectedDate(max_date)
#
#         self.menuBar().setCornerWidget(self.bg_create_expire_date, Qt.TopLeftCorner)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = MainWindow()
#     w.show()
#     sys.exit(app.exec_())
