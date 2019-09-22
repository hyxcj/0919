# -*- coding: utf-8 -*-
import sys
import os
import sps
from itertools import islice
from PyQt5.QtWidgets import  (QApplication, QMainWindow,
               QSplitter, QColorDialog, QLabel, QComboBox)

from PyQt5.QtCore import  pyqtSlot,Qt

from PyQt5.QtGui import QColor

import numpy as np
import pandas as pd

import matplotlib as mpl

import matplotlib.style as mplStyle  #一个模块

from  matplotlib.backends.backend_qt5agg import (FigureCanvas,
            NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt

from test import Ui_MainWindow

from PyQt5.QtWidgets import  (QApplication, QDialog,QFileDialog,
                        QColorDialog,QFontDialog,QProgressDialog,
                        QLineEdit,QInputDialog,QMessageBox)

from PyQt5.QtCore import  *

from PyQt5.QtGui import *
from dialog import Ui_Form  # 计算
from sps_ui import Ui_sps       # 加载sps ui


class Qmydialog(QDialog,Ui_Form):
    def __init__(self):
        super(Qmydialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("自定义消息对话框：登录窗口")

class Qmydialog_sps(QDialog,Ui_sps):

    mySignal = pyqtSignal(str)
    def __init__(self):
        super(Qmydialog_sps, self).__init__()
        self.setupUi(self)
        self.data = []


    @pyqtSlot()  ##"选择sps"
    def on_pushButtonR_clicked(self):
        curPath = QDir.currentPath()  # 获取系统当前目录
        dlgTitle = "选择R文件"  # 对话框标题
        filt = "文本文件(*.R);;"  # 文件过滤器

        filename = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        portion = os.path.splitext(filename[0])
        self.lineEdit_R.setText(portion[0]+'.R')
        self.lineEdit_S.setText(portion[0]+'.S')
        self.lineEdit_X.setText(portion[0]+'.X')

    def sendEditContent(self): #发射信号
        content = self.lineEdit_R.text()
        self.mySignal.emit(content)

    @pyqtSlot()  ##"确认sps"
    def on_pushButton_sure_clicked(self):
        # print(self.open_sps())
        self.sendEditContent()

        self.close()


    @pyqtSlot()  ##"退出"
    def on_pushButton_quit_clicked(self):
        self.close()


class QmyMainWindow(QMainWindow):


    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle("hyx")
        mplStyle.use("classic")  # 使用样式，必须在绘图之前调用,修改字体后才可显示汉字
        mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei']  # 显示汉字为 楷体， 汉字不支持 粗体，斜体等设置
        mpl.rcParams['font.size'] = 12
        ##  Windows自带的一些字体
        ##  黑体：SimHei 宋体：SimSun 新宋体：NSimSun 仿宋：FangSong  楷体：KaiTi
        mpl.rcParams['axes.unicode_minus'] = False  # 减号unicode编码
        self.data = []
        self.__createFigure()  # 创建Figure和FigureCanvas对象，初始化界面


    ##  ==============自定义功能函数========================
    def __createFigure(self):           # 创建面板
        self.__fig = mpl.figure.Figure()
        figCanvas = FigureCanvas(self.__fig)  # 创建FigureCanvas对象，必须传递一个Figure对象
        self.__fig.suptitle("显示", fontsize=16, fontweight='bold')  # 总的图标题
        naviToolbar = NavigationToolbar(figCanvas, self)  # 创建工具栏
        naviToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # ToolButtonTextUnderIcon,ToolButtonTextBesideIcon

        self.addToolBar(naviToolbar)  # 添加工具栏到主窗口
        self.setCentralWidget(figCanvas)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.ui.verticalLayoutWidget)
        splitter1.addWidget(self.ui.horizontalLayoutWidget)

        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)
        splitter.addWidget(splitter1)  # 左侧控制面板
        splitter.addWidget(figCanvas)  # 右侧FigureCanvas对象
        self.setCentralWidget(splitter)

    def __createFigure1(self):           # 创建面板
        self.__fig = mpl.figure.Figure()
        figCanvas = FigureCanvas(self.__fig)  # 创建FigureCanvas对象，必须传递一个Figure对象
        self.__fig.suptitle("显示", fontsize=16, fontweight='bold')  # 总的图标题
        # naviToolbar = NavigationToolbar(figCanvas, self)  # 创建工具栏
        # naviToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # ToolButtonTextUnderIcon,ToolButtonTextBesideIcon
        #
        # self.addToolBar(naviToolbar)  # 添加工具栏到主窗口
        self.setCentralWidget(figCanvas)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.ui.verticalLayoutWidget)
        splitter1.addWidget(self.ui.horizontalLayoutWidget)

        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)
        splitter.addWidget(splitter1)  # 左侧控制面板
        splitter.addWidget(figCanvas)  # 右侧FigureCanvas对象
        self.setCentralWidget(splitter)

    @pyqtSlot()  ##"选择初至文件"
    def on_pushButton_clicked(self):
        curPath = QDir.currentPath()  # 获取系统当前目录
        dlgTitle = "选择初至文件"  # 对话框标题
        filt = "文本文件(*.txt);;"  # 文件过滤器
        filename = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        self.data = pd.read_csv(filename[0], sep='\s+')
        self.fbpath =filename[0]

    def __drawFB(self):  ##初始化绘图初至
        self.__createFigure1()
        ax1 = self.__fig.add_subplot(1, 1, 1, label="FB")  # 子图1
        ax1.cla()
        x1 = self.data['RcvLine']*10000
        x2 = self.data['RcvStation']
        x = x1+x2
        y = self.data['fb(ms)']
        # x = np.random.normal(size=1000000)
        # y = np.random.normal(size=1000000)
        ax1.scatter(x,y, c = 'r',marker = 'x' ,label="fb",s=4)  # 绘制一条曲线
        ax1.set_xlabel('X 轴')  # X轴标题
        ax1.set_ylabel('Y 轴')  # Y轴标题
        # ax1.set_xlim([0, 10])  # X轴坐标范围
        # ax1.set_ylim([-1.5, 1.5])  # Y轴坐标范围
        ax1.set_title("初至")
        ax1.legend()  # 自动创建图例

    @pyqtSlot()  ##点击绘制初至
    def on_pushButton_2_clicked(self):
        self.__drawFB()
        self.__fig.canvas.draw()

    @pyqtSlot()  ##"打开另一个ui，并连接新ui的信号与主窗口槽函数"
    def on_pushButton_4_clicked(self):
        self.newDialog = Qmydialog_sps()
        self.newDialog.mySignal.connect(self.__dqSPS)
        # self.newDialog.mySignal.connect(self.__drawSPS)
        self.newDialog.exec_()

    def __dqSPS(self, connect):   ##绘制sps

        self.portion = os.path.splitext(connect)

    def __drawSPS(self):
        # a = pd.read_csv(open(connect),header=None,sep='\s+',encoding="gbk")
        # b = pd.read_csv(open(portion[0] + '.S'),header=None,sep='\s+',encoding="gbk")
        R = sps.Sps_sr(self.portion[0] + '.R')
        S = sps.Sps_sr(self.portion[0] + '.S')
        # print(a)
        # print(b)
        ax2 = self.__fig.add_subplot(1, 1, 1, label="sps")  # 子图1
        ax2.cla()
        # x1 = a[1]
        # x2 = b[1]
        # y1 = a[2]
        # y2 = b[2]
        ax2.scatter(R.X, R.Y, c='b', marker='x', label="R", s=0.5)  # 绘制一条曲线
        ax2.scatter(S.X, S.Y, c='r', marker='x', label="S", s=0.5)  # 绘制一条曲线
        ax2.set_xlabel('X 轴')  # X轴标题
        ax2.set_ylabel('Y 轴')  # Y轴标题
        ax2.get_xaxis().get_major_formatter().set_useOffset(False)
        # ax1.set_xlim([0, 10])  # X轴坐标范围
        # ax1.set_ylim([-1.5, 1.5])  # Y轴坐标范围
        ax2.set_title("观测系统")
        ax2.legend()  # 自动创建图例

    @pyqtSlot()  ##点击绘制sps
    def on_pushButton_7_clicked(self):
        self.__createFigure1()
        self.__drawSPS()
        self.__fig.canvas.draw()


    @pyqtSlot()  ##"打开一个文件"
    def on_pushButton_3_clicked(self):
        self.newDialog = Qmydialog()
        self.newDialog.show()

    @pyqtSlot()  ##输入文件号显示初至
    def on_lineEdit_returnPressed(self):
        self.danpaochuzhi()
        self.__fig.canvas.draw()
    def danpaochuzhi(self):
        self.__createFigure1()
        ffid =int(self.ui.lineEdit.text())
        ax1 = self.__fig.add_subplot(1, 1, 1, label="FB")  # 子图1
        ax1.cla()
        with open(self.fbpath) as fb_file:
            ShotLine = []
            ShotStation = []
            ShotIdx = []
            RcvLine = []
            RcvStation = []
            FileNo = []
            ChannelNo = []
            fb = []
            Rcv = []
            Shot = []
            of = []

            for line in islice(fb_file, 1, None):
                ShotLine.append(float(line[8:15]))
                ShotStation.append(float(line[23:30]))
                ShotIdx.append(int(line[43:45]))
                RcvLine.append(float(line[53:60]))
                RcvStation.append(float(line[68:75]))
                FileNo.append(int(line[83:91]))
                ChannelNo.append(float(line[99:106]))
                fb.append(float(line[112:121]))
                Rcv.append(int(float(line[53:60])) * 10000 + int(float(line[68:75])))
                Shot.append(int(float(line[8:15])) * 10000 + float(line[23:30]))
                of.append(abs((float(line[68:75]) - float(line[23:30]))) * 40)

                fb_file = {'ShotLine': ShotLine,
                           'ShotStation': ShotStation,
                           'ShotIdx': ShotIdx,
                           'RcvLine': RcvLine,
                           'RcvStation': RcvStation,
                           'FileNo': FileNo,
                           'ChannelNo': ChannelNo,
                           'fb': fb,
                           'Rcv': Rcv,
                           'Shot': Shot,
                           'of': of
                           }
            fb_file1 = pd.DataFrame(fb_file)

            ffid_file = pd.DataFrame(np.ones(1) * ffid, columns=['FileNo'])
            fb_ffid = pd.merge(fb_file1, ffid_file, on=['FileNo'])
        ax1.scatter(fb_ffid['ChannelNo'], fb_ffid['fb'],marker ='x')  # 绘制一条曲线
        ax1.get_xaxis().get_major_formatter().set_useOffset(False)
        ax1.set_title("单炮初至")
        ax1.legend()  # 自动创建图例

    @pyqtSlot()  ##下一炮
    def on_pushButton_6_clicked(self):
        n=int(self.ui.lineEdit.text())
        m=str(n+1)
        self.ui.lineEdit.setText(m)
        self.danpaochuzhi()
        self.__fig.canvas.draw()\

    @pyqtSlot()  ##上一炮
    def on_pushButton_5_clicked(self):
        n=int(self.ui.lineEdit.text())
        m = str(n - 1)
        self.ui.lineEdit.setText(m)
        self.danpaochuzhi()
        self.__fig.canvas.draw()






if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.show()
   sys.exit(app.exec_())
