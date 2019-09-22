import sys
import os

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
from dialog import Ui_Form  # 计算
from sps_ui import Ui_sps       # 加载sps ui


class Qmydialog(QDialog,Ui_Form):
    def __init__(self):
        super(Qmydialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("自定义消息对话框：登录窗口")

class Qmydialog_sps(QDialog,Ui_sps):
    Signal_OneParameter = pyqtSignal(list)
    def __init__(self):
        super(Qmydialog_sps, self).__init__()
        self.setupUi(self)
        self.data = []
        self.edit_emit = QLineEdit(self)
        self.edit_emit.connect(self.emit_signal)

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





        self.data  = pd.read_csv(filename[0],header=None, sep='\s+')
        # return self.data
        #print(self.data)
    def open_sps(self):
        print(self.data)
    @pyqtSlot()  ##"打开sps"
    def on_pushButton_sure_clicked(self):
        # print(self.open_sps())
        self.open_sps()
        self.close()

    @pyqtSlot()  ##"退出"
    def on_pushButton_quit_clicked(self):
        self.close()


#Qmydialog_sps().open_sps()

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
        self.data1 =Qmydialog_sps().open_sps()



        self.__createFigure()  # 创建Figure和FigureCanvas对象，初始化界面
        #self.__drawFig2X1()  # 绘图



    ##  ==============自定义功能函数========================
    def __createFigure(self):
        ##      self.__fig=mpl.figure.Figure(figsize=(8, 5),constrained_layout=True, tight_layout=None)  #单位英寸
        #self.__fig = mpl.figure.Figure(figsize=(4, 2))  #单位英寸
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

        # splitter2 = QSplitter(Qt.Vertical)
        # splitter2.addWidget(splitter1)
        # splitter2.addWidget(bottom)

        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)
        splitter.addWidget(splitter1)  # 左侧控制面板
        splitter.addWidget(figCanvas)  # 右侧FigureCanvas对象
        self.setCentralWidget(splitter)

    def __drawFB(self):  ##初始化绘图
        ##      gs=self.__fig.add_gridspec(2,1)  #2行，1列
        ##
        ##      ax1=self.__fig.add_subplot(gs[0,0],label="sin-cos plot")  #子图1

        ax1 = self.__fig.add_subplot(1, 1, 1, label="FB")  # 子图1
        ax1.cla()
        x1 = self.data['RcvLine']*10000
        x2 = self.data['RcvStation']
        x = x1+x2
        #print(x)
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
        #self.__curAxes = ax1  # 当前操作的Axes对象

    def __drawSPS(self):  ##初始化绘图
        ax1 = self.__fig.add_subplot(1, 1, 1, label="sps")  # 子图1
        ax1.cla()
        x = self.data1['1']
        #print(x)
        y = self.data1['2']
        # x = np.random.normal(size=1000000)
        # y = np.random.normal(size=1000000)
        ax1.scatter(x,y, c = 'r',marker = 'x' ,label="sps",s=4)  # 绘制一条曲线
        ax1.set_xlabel('X 轴')  # X轴标题
        ax1.set_ylabel('Y 轴')  # Y轴标题
        # ax1.set_xlim([0, 10])  # X轴坐标范围
        # ax1.set_ylim([-1.5, 1.5])  # Y轴坐标范围
        ax1.set_title("观测系统")
        ax1.legend()  # 自动创建图例
        #self.__curAxes = ax1  # 当前操作的Axes对象

    @pyqtSlot()  ##子图是否可见
    def on_pushButton_2_clicked(self):

        self. __drawFB()
        self.__fig.canvas.draw()

    @pyqtSlot()  ##子图是否可见
    def on_pushButton_7_clicked(self):
        self.a=Qmydialog_sps().data
        print(self.a)
        #self.__drawSPS()
        #self.__fig.canvas.draw()

    @pyqtSlot()  ##"打开一个文件"
    def on_pushButton_clicked(self):
        curPath = QDir.currentPath()  # 获取系统当前目录
        dlgTitle = "选择一个文件"  # 对话框标题
        filt = "文本文件(*.txt);;"  # 文件过滤器

        # filename = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        #self.ui.plainTextEdit.appendPlainText(filename)
        #self.ui.plainTextEdit.appendPlainText("\n" + filtUsed)

        filenam = QFileDialog()

        filenam.setFileMode(QFileDialog.AnyFile)
        #设置过滤器
        filenam.setFilter( QDir.Files  )

        if filenam.exec_():
            filenames= filenam.selectedFiles()
            f = pd.read_csv(filenames[0], sep='\s+')

            # with f:
            #     data = f.read()
            #     #self.contents.setText(data)
            #     print(data)
            self.data = f
            print(self.data)
            # self.x = f['RcvStation']
            # self.y = f['fb(ms)']
            # print(self.x)
        # sx = []
        # sy = []
        # sz = []
        # sl = []
        # sp = []
        #
        # for line in filename:
        #     sx.append(float(line[47:55]))
        #     sy.append(float(line[56:65]))
        #     # sz.append(float(line[65:70]))
        #     sl.append(float(line[2:11]))
        #     sp.append(float(line[16:21]))
        # return sx, sy, sz, sl, sp
        # print(sx)

    @pyqtSlot()  ##"打开一个文件"
    def on_pushButton_3_clicked(self):
        self.newDialog = Qmydialog()
        self.newDialog.show()
    @pyqtSlot()  ##"打开一个文件"
    def on_pushButton_4_clicked(self):
        self.newDialog = Qmydialog_sps()
        self.newDialog.show()

if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.show()
   sys.exit(app.exec_())
