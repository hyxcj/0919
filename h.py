import pandas as pd

path = 'C:\\0919\\lw.R'
a = pd.read_csv(path,encoding="gbk",header=None,sep='\s+')
b=pd.DataFrame(a,ignore_index=False,sep='\s+')
print(a)
print(b)