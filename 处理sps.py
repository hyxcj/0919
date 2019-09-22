import pandas as pd
from itertools import islice
import numpy as np

with open('lw.txt') as fb_file:
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
    ffid_file = pd.DataFrame(np.ones(1) * 7, columns=['FileNo'])
    fb_ffid = pd.merge(fb_file1, ffid_file, on=['FileNo'])
    print(fb_ffid)