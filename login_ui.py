from PyQt5 import QtWidgets
import sys


class LoginUi(QtWidgets.QDialog):
    def __init__(self):
        super(LoginUi, self).__init__()
        self.label_user = QtWidgets.QLabel()
        self.label_password = QtWidgets.QLabel()
        self.lineEdit_user = QtWidgets.QLineEdit()
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.pussButton_signin = QtWidgets.QPushButton()
        self.pussButton_signup = QtWidgets.QPushButton()

        self.h_layout_user = QtWidgets.QHBoxLayout()
        self.h_layout_password = QtWidgets.QHBoxLayout()
        self.h_layout_button = QtWidgets.QHBoxLayout()
        self.v_layout_all = QtWidgets.QVBoxLayout()

        self.h_layout_user.addWidget(self.label_user)
        self.h_layout_user.addWidget(self.lineEdit_user)
        self.h_layout_password.addWidget(self.label_password)
        self.h_layout_password.addWidget(self.lineEdit_password)
        self.h_layout_button.addWidget(self.pussButton_signin)
        self.h_layout_button.addWidget(self.pussButton_signup)
        self.v_layout_all.addLayout(self.h_layout_user)
        self.v_layout_all.addLayout(self.h_layout_password)
        self.v_layout_all.addLayout(self.h_layout_button)

        self.setLayout(self.v_layout_all)

        self.setWindowTitle("登陆界面")
        self.label_user.setText("用户名:")
        self.label_password.setText("密码:  ")
        self.pussButton_signin.setText("登陆")
        self.pussButton_signup.setText("注册")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginUi()
    ui.show()
    sys.exit(app.exec_())