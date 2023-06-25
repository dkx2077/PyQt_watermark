# -*- coding = utf-8 -*-
# @time:2023-06-21 09:00
# Author:den999
# @File:main.py
#!/usr/bin/python
# coding:utf-8

from login_ui import LoginUi
import sqlite3
import hashlib
import change
import file_make
from PyQt5.QtWidgets import *
from PyQt5 import uic
import yulan
from PIL import Image, ImageQt
import time
import sys
from PyQt5 import QtCore, QtWidgets


class MyWindow(QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.text_img2 = None
        self.text_img = None
        self.user_input_light = None
        self.user_input_rotate = None
        self.user_input_size = None
        self.text = None
        self.file_src = None

    def init_ui(self):
        QApplication.processEvents()
        self.ui = uic.loadUi("./den999.ui")
        print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # # 提取要操作的控件
        self.ui.setWindowTitle("图片添加水印软件")
        self.file_src = ''
        self.file_choose_btn = self.ui.toolButton
        self.file_choose_btn.clicked.connect(self.getInfo)

        self.make_btn = self.ui.pushButton_2
        try:
            self.make_btn.clicked.connect(self.start)
        except:
            pass

        self.user_input_src = self.ui.lineEdit_6
        self.user_input_text = self.ui.lineEdit
        self.user_input_size = self.ui.lineEdit_2
        self.user_input_rotate = self.ui.lineEdit_3
        self.user_input_light = self.ui.lineEdit_5

        self.small_pic_show = self.ui.label_11
        self.big_pic_show = self.ui.label_9
        # 方法1代码
        ##############################
        # self.text = self.user_input_text.text()  # u'den999'
        self.text_img = yulan.small_pic('点刷新预览')
        pix = ImageQt.toqpixmap(self.text_img)
        #############################
        # qimage = ImageQt.ImageQt(image)
        self.small_pic_show.setPixmap(pix)
        self.small_pic_show.setStyleSheet("border: 2px solid blue")
        self.small_pic_show.setScaledContents(True)
        QApplication.processEvents()
        ##############################
        self.text_img2 = yulan.big_pic('点刷新预览')
        pix2 = ImageQt.toqpixmap(self.text_img2)
        self.big_pic_show.setPixmap(pix2)
        self.big_pic_show.setStyleSheet("border: 1px solid gray")
        self.big_pic_show.setScaledContents(True)
        ##############################
        self.reshow_btn = self.ui.pushButton
        self.reshow_btn.clicked.connect(self.reset_mes)

    def reset_mes(self):
        self.user_input_size = self.ui.lineEdit_2
        self.user_input_rotate = self.ui.lineEdit_3
        self.user_input_light = self.ui.lineEdit_5
        size = int(self.user_input_size.text())
        rotate = int(self.user_input_rotate.text())
        light = int(self.user_input_light.text())
        light = (int(light) % 11) * 25
        ##########################################
        self.text = self.user_input_text.text()
        self.text_img = yulan.small_pic(self.text, rotate, 120, light)
        pix = ImageQt.toqpixmap(self.text_img)
        self.small_pic_show.setPixmap(pix)
        self.small_pic_show.setStyleSheet("border: 2px solid blue")
        self.small_pic_show.setScaledContents(True)
        QApplication.processEvents()
        #############################################################
        self.text_img2 = yulan.big_pic(self.text, rotate, int(size / 2), light)
        pix2 = ImageQt.toqpixmap(self.text_img2)
        self.big_pic_show.setPixmap(pix2)
        self.big_pic_show.setStyleSheet("border: 1px solid gray")
        self.big_pic_show.setScaledContents(True)
        QApplication.processEvents()

    def getInfo(self):
        file = QFileDialog()  # 创建文件对话框
        file.setDirectory("D:\\")  # 设置初始路径为D盘
        self.file_src = file.getExistingDirectory(self, "请选择文件夹路径", "D:\\")
        self.ui.lineEdit_6.setText(self.file_src)
        QApplication.processEvents()

    def start(self):
        try:
            self.ui.textBrowser.setText('正在读取文件：' + self.file_src)
            self.file_src = self.ui.lineEdit_6.text()
            self.text = self.user_input_text.text()
            new_file = self.file_src + "./水印"  # 存放生成图片的文件夹路径
            file_make.mkdir(new_file)  # 调用函数
            old_path = self.file_src  # 存放旧图片的文件夹路径
            pic_name_list = file_make.find_all(old_path)
            rotate = self.user_input_rotate.text()  # rotate = -35
            text_size = self.user_input_size.text()  # text_size = 30
            light = self.user_input_light.text()
            light = (int(light) % 11) * 25
            # print(rotate, text_size,light)
            self.ui.textBrowser.append('正在处理：')
            for i in range(len(pic_name_list)):
                self.ui.textBrowser.append(pic_name_list[i])
            time.sleep(2)
            change.work_start(old_path, pic_name_list, self.text, new_file, int(rotate), int(text_size), int(light))

        except:
            self.ui.textBrowser.append('读取文件失败!\n请选择(.jpg/.png)等图片所在文件夹！！！（不要直接选择图片）')
            pass


class Login(LoginUi):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle('登录')

        self.conn = sqlite3.connect("user.db")  # 使用其他数据库的话此处和import模块需要修改

        # 此处改变密码输入框lineEdit_password的属性，使其不现实密码
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pussButton_signin.clicked.connect(self.sign_in)
        self.pussButton_signup.clicked.connect(self.sign_up)

    @staticmethod
    def hash(src):
        """
        哈希md5加密方法
        :param src: 字符串str
        :return:
        """
        src = (src + "请使用私钥加密").encode("utf-8")
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()

    def sign_in(self):
        """
        登陆方法
        :return:
        """
        self.setWindowTitle('登录')
        c_sqlite = self.conn.cursor()
        user_name = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        if user_name == "" or user_password == "":
            QMessageBox.information(self, "登录状态", "请输入用户名和密码", QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.Yes)
        else:
            c_sqlite.execute("""SELECT password FROM user WHERE name = ?""", (user_name,))
            password = c_sqlite.fetchall()
            if not password:
                QMessageBox.information(self, "登陆状态", "此用户未注册", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
            else:
                if self.hash(user_password) == password[0][0]:
                    QMessageBox.information(self, "登陆状态", "登陆成功", QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
                    self.switch_window.emit()
                else:
                    QMessageBox.information(self, "登陆状态", "密码不正确", QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)

    def sign_up(self):
        """
        注册方法
        :return:
        """
        self.setWindowTitle('注册')
        c_sqlite = self.conn.cursor()
        user_name = self.lineEdit_user.text()
        user_password = self.lineEdit_password.text()
        if user_name == "" or user_password == "":
            pass
        else:
            user_password = self.hash(user_password)
            c_sqlite.execute("""SELECT password FROM user WHERE name = ?""", (user_name,))
            if not c_sqlite.fetchall():
                c_sqlite.execute("""INSERT INTO user VALUES (NULL ,?,?)""", (user_name, user_password))
                self.conn.commit()
                QMessageBox.information(self, "注册状态", "注册成功", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            else:
                QMessageBox.information(self, "注册状态", "用户名重复", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)


class Controller:

    def __init__(self):
        self.window = None
        self.login = None

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MyWindow()
        self.login.close()
        self.window.ui.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
