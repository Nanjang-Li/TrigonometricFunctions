import sys
from CalculatorUi import UiMainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.ui.number_0_button.clicked.connect(lambda: self.display_number(0))
        self.ui.number_1_button.clicked.connect(lambda: self.display_number(1))
        self.ui.number_2_button.clicked.connect(lambda: self.display_number(2))
        self.ui.number_3_button.clicked.connect(lambda: self.display_number(3))
        self.ui.number_4_button.clicked.connect(lambda: self.display_number(4))
        self.ui.number_5_button.clicked.connect(lambda: self.display_number(5))
        self.ui.number_6_button.clicked.connect(lambda: self.display_number(6))
        self.ui.number_7_button.clicked.connect(lambda: self.display_number(7))
        self.ui.number_8_button.clicked.connect(lambda: self.display_number(8))
        self.ui.number_9_button.clicked.connect(lambda: self.display_number(9))
        self.ui.del_button.clicked.connect(self.display_delete_one_number)
        self.ui.reset_button.clicked.connect(self.display_reset)
        self.ui.dot_button.clicked.connect(self.display_dot)

    def display_number(self, number):
        """
        在显示框上显示按钮对应的值
        :param number: 按钮对应的值
        :return: None
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if display_content == "0":
            display_content = str(number)  # 当前内容为0，直接更新为的按钮数字
        else:
            display_content += str(number)  # 当前内容不为0，追加数字
        self.ui.display_box.setText(display_content)    # 回显内容

    def display_dot(self):
        """
        在显示框上显示一个小数点.
        :return: None
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        display_content += "."  # 追加一个小数点
        self.ui.display_box.setText(display_content)    # 回显内容

    def display_delete_one_number(self):
        """
        清除当前显示框上数值最右侧的一位数；
        当显示框上的数值只有一位时，再次按清除按钮显示0；
        :return: None;
        """
        display_content = self.ui.display_box.text()  # 获取显示框文本
        if len(display_content) == 1:
            display_content = "0"  # 当显示框上的数值只有一位时，再次按清除按钮显示0；
        else:
            display_content = display_content[:-1]  # 清除当前显示框上数值最右侧的一位数
        self.ui.display_box.setText(display_content)    # 回显内容

    def display_reset(self):
        """
        重置显示框上的内容为0
        :return:None
        """
        self.ui.display_box.setText("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
