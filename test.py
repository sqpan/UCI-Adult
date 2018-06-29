#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:05:35 2018

@author: shaopan
"""

import pandas as pd
import numpy as np
import sklearn

# import file
file = 'no_questionMark.csv'
df = pd.read_csv(file)
#print(df.head(10))
print(df.shape)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# origin dataframe shape (32561, 15)



# clean miss value row 
df_dropNull = df.dropna()
df_dropNull.reset_index(drop=True, inplace=True)
print(df_dropNull.shape)
print(df_dropNull[0:20])
df_dropNull.to_csv('nomissing.csv', sep=',')
#print(df_dropNull.head(20))
# dataframe shape after take out row with missing value (32561, 15)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print("The following is the naive bayes algorithm")

# take out correlated data column (education level and education number of years)
# choose to take out education level, because education number of year is quantitive data
# and education level can be generate by education numnber of year 
# ex. 1 to 5 in number of education number of year represent elementary school
nb = df_dropNull.drop(['education','relationship'], axis = 1)
nb.reset_index(drop=True, inplace=True)
#print(nb.head(20))
#print(nb.shape)
nb1 = nb[0:20]
#print(nb1)


def transfer_nativeCountry():
    country_list = []
    for i in range(nb.shape[0]):
        if (nb.iloc[i][11] in country_list):
            nb.at[i,'native country num'] = country_list.index(nb.iloc[i]['native country'])
        else :
            country_list.append(nb.iloc[i]['native country'])
            nb.at[i,'native country num'] = len(country_list) - 1

transfer_nativeCountry()
print(nb.head(10))
nb.to_csv('all_number.csv', sep=',')
'''


def transfer_nativeCountry():
    country_list = []
    for i in range(nb1.shape[0]):
        if (nb1.iloc[i][11] in country_list):
            nb1.at[i,'native country num'] = country_list.index(nb1.iloc[i]['native country'])
            print("Country: " + nb1.iloc[i]['native country'] + "\n")
            print(country_list)
            print("list size: ")
            print(len(country_list))
        else :
            country_list.append(nb1.iloc[i]['native country'])
            nb1.at[i,'native country num'] = len(country_list) - 1
            print("Country: " + nb1.iloc[i]['native country'] + "\n")
            print(country_list)
            print("list size: ")
            print(len(country_list))
'''
transfer_nativeCountry()
print(nb)
nb.to_csv('all_number.csv', sep=',')
