import sys
from TriCalculatorUi.CalculatorUi import UiMainWindow
from TriFunctions.sin import sin
from TriFunctions.cos import cos
from TriFunctions.arcsin import asin
from TriFunctions.arctan import atan
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
        self.ui.sin_button.clicked.connect(self.computer_sin)
        self.ui.cos_button.clicked.connect(self.computer_cos)
        self.ui.arcsin_button.clicked.connect(self.computer_arcsin)
        self.ui.arctan_button.clicked.connect(self.computer_arctan)

    def str_to_number(self):
        """
        将显示框的文本转为对应的数值
        :return: number，字符串对应的值
        """
        return eval(self.ui.display_box.text())

    def display_to_box(self, content):
        """
        在显示框上显示内容
        :param content: str，要的显示内容；
        :return: None
        """
        self.ui.display_box.setText(content)

    def computer_sin(self):
        """
        计算输入值的sin值
        :return: None
        """
        input_value = self.str_to_number()  # 获取用户输入
        result = sin(input_value)  # 计算
        self.display_to_box(str(result))  # 显示结果

    def computer_cos(self):
        """
        计算输入值的cos值
        :return: None
        """
        input_value = self.str_to_number()  # 获取用户输入
        result = cos(input_value)  # 计算
        self.display_to_box(str(result))  # 显示结果

    def computer_arcsin(self):
        """
        计算输入值的arcsin值
        :return: None
        """
        input_value = self.str_to_number()  # 获取用户输入
        result = asin(input_value)
        if isinstance(result, bool):
            # 返回一个bool值说明输入有误，显示提示信息
            result = "无效输入"
        self.display_to_box(str(result))    # 显示结果

    def computer_arctan(self):
        """
        计算输入值的arctan值
        :return: None
        """
        input_value = self.str_to_number()  # 获取用户输入
        result = atan(input_value)  # 计算
        self.display_to_box(str(result))  # 显示结果

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
        self.display_to_box(display_content)  # 回显内容

    def display_dot(self):
        """
        在显示框上显示一个小数点.
        :return: None
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if "." in display_content:
            return
        else:
            display_content += "."  # 追加一个小数点
            self.display_to_box(display_content)  # 回显内容

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
        self.display_to_box(display_content)  # 回显内容

    def display_reset(self):
        """
        重置显示框上的内容为0
        :return:None
        """
        self.display_to_box("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
