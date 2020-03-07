import pandas as pd
import numpy as np

#import dataframe
df=pd.read_excel('Example_Data.xlsx')
print(df.head(200))
dev = df['Device'].unique()
#list of device
print(dev_list)

dfout=pd.DataFrame()
dfout2 = pd.DataFrame()

time = [1.5,2.5]
# addrow= {}
data_list =['Data', 'Data Two']
sub_list = ['Data Sub','Data Two Sub']

# interpolation 
for d in dev:
    addrow_list = []
    for t in time:
        row={'Time':t,'Device':d}
        for data in data_list:
            dfin = df.loc[(df['Device']==d)]
            x=dfin['Time'].values
            y=dfin[data].values
            z = np.polyfit(x,y,2)
            ynew=np.polyval(z,t)
            row[data]=ynew
        addrow_list.append(row)
    add = dfin.append(addrow_list, ignore_index=True)
    
    dfout = dfout.append(add)
print(dfout.head(45))

#subtraction of 0 values
data_list = []
for d in dev:
    dfin2 = dfout.loc[(dfout['Device']==d)].copy()
    new_list=[]
    for data,sub in zip(data_list,sub_list):
        dfin2[sub] = dfin2[data]-dfin2.loc[dfin.Time.idxmin(),data]
    dfout2=dfout2.append(dfin2)
    
print(dfout2.head(20))


