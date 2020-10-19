# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:29:57 2020

@author: jiveland
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import cvs file as pandas data frame
dftest = pd.read_csv('./file.csv')

#get the # of columns
nc = len(dftest.columns)
#print pairwise correlation
print(dftest.corr())

#set fig size
plt.figure(figsize = (10,10))
#plot heatmap of pairwise correlation
sns.heatmap(dftest.corr(),annot=False)
plt.ylim(nc,0)

#if you want to drop columns in the single  feature bar plot
drop_col = ['COL1','COL2']

dftest.corr()['FIXEDCOL'].sort_values().drop(drop_col).plot(kind='bar')

##scatter plot

sns.scatterplot(x='COL1',y='COL2',data-dftest,hue='TYPE')
