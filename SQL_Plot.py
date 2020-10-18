# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:25:08 2020

@author: jiveland
"""

import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import numpy as np

#connection conditions
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=servername;DATABASE=dbname;Integrated Security=True;Connection Timeout=3')
#table selection

SQL= f"select*from[tablename]"

#generate dataframe from SQL table
df = pd.read_sql(SQL,conn)

##generate an SQL string to select some sub-set of a table based on a list

for idx,i in enumerate(example_list,0):
    if idx==0:
        string=f"'%{i}%'"
    else:
        string = string + 'OR EXAMPLETABLE LIKE' f"'%{i}'"


## creaate a DF based on some table list
table_list=['TABLE1','TABLE2']
df = pd.DataFrame()
for table in table_list:
    SQL = f"select* from[{table}] WHERE (EXAMPLE_TABLE LIKE {something}) AND EXAMPLE_TABLE2 LIKE {somethingelse})"
    df2= pd.read_sql(SQL,conn)
    dfout = df.append(df2)
    
    
#plot something from a table
    
x_list= ['X1','X2','X3']
y_list= ['Y1','Y2','Y3']
#dfin can be a sub-set of df for loob before this loop if that is the case

##iterate over x and y as tuples
for x,y in zip(x_list,y_list):
    dfplt = dfin
    plt.plot(x,y,data=dfplt,label=f'{y}',linestye='-',marker='o')
    plt.title('title')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(which='both',axis='both',color='black',linestyle='-',linewidth=0.1)
    #if limits need to be set
    plt.ylim(0,.5)
    #setup legend and plt size
    plt.gca().legend(loc='best')
    plt.gcf().set_size_inches(6,6)
    #save plot and display plot
    plt.savefig(f'./name.png',dpi=200)
    plt.show()
    
    