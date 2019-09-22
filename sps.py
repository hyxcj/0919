import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import islice
# path = '2dfb.txt'
class Sps_sr():
    def __init__(self,path):
        self.path=path
        self.RecordId = []
        self.LineName = []
        self.PointNumber = []
        self.PointIndex = []
        self.PointCode = []
        self.StacoRrect = []
        self.PointDepth = []
        self.SeiDatum = []
        self.UpHoleTime = []
        self.WaterDepth = []
        self.X = []
        self.Y = []
        self.Z = []
        self.Day = []
        self.Time = []
        file = open(path)
        for line in file:
            self.RecordId.append(line[0])
            self.LineName.append(float(line[1:11]))
            self.PointNumber.append(float(line[11:21]))
            self.PointIndex.append(int(line[23]))
            self.PointCode.append(line[24:26])
            self.StacoRrect.append(line[26:30])
            self.PointDepth.append(line[30:34])
            self.SeiDatum.append(line[34:38])
            self.UpHoleTime.append(line[38:40])
            self.WaterDepth.append(line[40:46])
            self.X.append(float(line[46:55]))
            self.Y.append(float(line[55:65]))
            self.Z.append(float(line[65:71]))
            self.Day.append(line[71:74])
            self.Time.append(line[74:80])
    def show(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        ax = plt.gca()
        ax.xaxis.get_major_formatter().set_powerlimits((0, 10))
        plt.xticks(np.linspace(min(x), max(x), 5))
        plt.yticks(np.linspace(min(y), max(y), 5))
        # plt.xlim((min(x) * 0.9999, max(x) * 1.0001))
        # plt.ylim((min(y) * 0.9999, max(y) * 1.0001))

        plt.scatter(x,y, s=1, c=z, cmap='rainbow')
        plt.colorbar()

        plt.show()

############准备初至数据####
# with open(path) as fb_file:
#     ShotLine = []
#     ShotStation = []
#     ShotIdx = []
#     RcvLine = []
#     RcvStation = []
#     FileNo = []
#     ChannelNo = []
#     fb = []
#     Rcv=[]
#     Shot = []
#     of = []
#     for line in islice(fb_file, 1, None):
#         ShotLine.append(float(line[8:15]))
#         ShotStation.append(float(line[23:30]))
#         ShotIdx.append(int(line[43:45]))
#         RcvLine.append(float(line[53:60]))
#         RcvStation.append(float(line[68:75]))
#         FileNo.append(int(line[83:91]))
#         ChannelNo.append(float(line[99:106]))
#         fb.append(float(line[112:121]))
#         Rcv.append(int(float(line[53:60]))*10000+int(float(line[68:75])))
#         Shot.append(int(float(line[8:15]))*10000+float(line[23:30]))
#         of.append(abs((float(line[68:75])-float(line[23:30])))*40)
#
#     fb_file = {'ShotLine':ShotLine,
#              'ShotStation':ShotStation,
#              'ShotIdx':ShotIdx,
#              'RcvLine':RcvLine,
#              'RcvStation':RcvStation,
#              'FileNo':FileNo,
#              'ChannelNo':ChannelNo,
#              'fb':fb,
#              'Rcv':Rcv,
#              'Shot':Shot,
#              'of':of
#              }
#
#
# #拟合
# def nh(file):
#     x = file['of']
#     y = file['fb']
#     z1 = np.polyfit(x, y, 3) # 用3次多项式拟合
#     p1 = np.poly1d(z1)
#     #print(p1) # 在屏幕上打印拟合多项式
#     yvals=p1(x) # 也可以使用yvals=np.polyval(z1,x)
#     # print(len(yvals))
#
#     # plot1=plt.scatter(file['ChannelNo'], y,c='black',s = 0.2)
#     # plot2=plt.scatter(file['ChannelNo'], yvals,c='red',s = 0.2)
#     # plt.xlabel('ChannelNo')
#     # plt.ylabel('fb')
#     # plt.show()
#     return yvals
#
# ##单炮炮域拟合
# def dppynh(file):
#     fb_file1 = file
#     b = fb_file1.drop_duplicates('RcvLine','first',inplace=False)
#     c = b['RcvLine'].values
#     sy = []
#     for i in c:
#
#         a =fb_file1[fb_file1['RcvLine']==i]
#         sy.extend(nh(a))
#     # plot1=plt.scatter(file['ChannelNo'], file['fb'],c='black',s = 0.2)
#     # plot2=plt.scatter(file['ChannelNo'], sy,c='red',s = 0.2)
#     # plt.show()
#     return sy
#
#
# #炮域拟合
# def pynh():
#     fb_file1 = pd.DataFrame(fb_file)
#     b = fb_file1.drop_duplicates('Shot', 'first', inplace=False)
#     c = b['Shot'].values
#     sy = []
#     for n in c:
#         f = fb_file1[fb_file1['Shot'] == n]
#         sy.extend(dppynh(f))
#     return sy
# sy = pynh()
# # a = pd.DataFrame(sy)
# # a.to_csv('111.csv')
# # print(len(sy))
#
#
# fb_file_sy =pd.DataFrame( {
#              'Rcv':Rcv,
#              'sy':sy,
#              'fb':fb
#              })
#
# sy_sort = fb_file_sy.sort_values(by=['Rcv'])
# b = sy_sort.drop_duplicates('Rcv', 'first', inplace=False)
# c = b['Rcv'].values
# sy_sy = []
# fb_sy = []
# for n in c:
#     f = sy_sort[sy_sort['Rcv'] == n]
#     cz = f['sy']-f['fb']
#     a = f['fb']
#     b = cz.mean()
#     c = [i + b for i in a]
#     fb_sy.extend(c)
#     sy_sy.append(cz.mean())
# # print(fb_sy)
# #
# #
# # print(len(fb_sy))
#
#
#
#
#
# #ffid显示初至
# def fbffid(ffid):
#
#     #ffid = 510334  #文件号
#     fb_file1 = pd.DataFrame(fb_file)
#     ffid_file = pd.DataFrame(np.ones(1) * ffid, columns=['FileNo'])
#     fb_ffid = pd.merge(fb_file1, ffid_file, on=['FileNo'])
#
#
#     plt.plot(fb_ffid['ChannelNo'],fb_ffid['fb'],'x')
#     plt.show()
#
# #炮点号显示初至
# def fbshot(shot):
#
#     #Shot = 510334  #文件号
#     fb_file1 = pd.DataFrame(fb_file)
#     shot_file = pd.DataFrame(np.ones(1) * shot, columns=['Shot'])
#     fb_ffid = pd.merge(fb_file1, shot_file, on=['Shot'])
#
#
#     plt.plot(fb_ffid['Rcv'],fb_ffid['fb'],'--')
#     plt.show()
#
# #运行
# S=Sps_sr('lw.s')
# R=Sps_sr('lw.r')
# S.show(S.X,S.Y,S.Z)
# fbshot(22013.5)
# fbffid(510122)
# dppynh()
#













