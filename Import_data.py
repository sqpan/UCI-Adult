#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:11:17 2018

@author: shaopan
"""
import pandas as pd
import numpy as np
import sklearn

# import file
file = 'no_questionMark.csv'
df = pd.read_csv(file)
print(df.head(10))
print(df.shape)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# origin dataframe shape (32561, 15)

# clean miss value row 
df_dropNull = df.dropna()
print(df_dropNull.shape)
print(df_dropNull.head(10))
# dataframe shape after take out row with missing value (32561, 15)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print("The following is the naive bayes algorithm")

# take out correlated data column (education level and education number of years)
# choose to take out education level, because education number of year is quantitive data
# and education level can be generate by education numnber of year 
# ex. 1 to 5 in number of education number of year represent elementary school
nb = df_dropNull.drop(['education','relationship'], axis = 1)
print(nb.head())
print(nb.shape)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# change category data into numerical data
# chagnge work class
def transfer_workclass(x):
    if (x == ' Federal-gov'):
        return 0
    elif (x == ' State-gov'):
        return 1
    elif (x == ' Local-gov'):
        return 2
    elif (x == ' Private'):
        return 3
    elif (x == ' Self-emp-inc'):
        return 4
    elif (x == ' Self-emp-not-inc'):
        return 5
    elif (x == ' Without-pay'):
        return 6 
    elif (x == ' Never-worked'):
        return 7
# end of transfer_workclass

# chagnge marital status        
def transfer_marital(x):
    if (x == ' Divorced'):
        return 0
    elif (x == ' Married-AF-spouse'):
        return 1
    elif (x == ' Married-civ-spouse'):
        return 2
    elif (x == ' Married-spouse-absent'):
        return 3
    elif (x == ' Never-married'):
        return 4
    elif (x == ' Separated'):
        return 5
    elif (x == ' Widowed'):
        return 6
# end of transfer_marital
 
# chagnge occuption    
def transfer_occuption(x):
    if (x == ' Adm-clerical'):
        return 0
    elif (x == ' Armed-Forces'):
        return 1
    elif (x == ' Craft-repair'):
        return 2
    elif (x == ' Exec-managerial'):
        return 3
    elif (x == ' Farming-fishing'):
        return 4
    elif (x == ' Handlers-cleaners'):
        return 5
    elif (x == ' Machine-op-inspct'):
        return 6
    elif (x == ' Other-service'):
        return 7
    elif (x == ' Priv-house-serv'):
        return 8
    elif (x == ' Prof-specialty'):
        return 9
    elif (x == ' Protective-serv'):
        return 10
    elif (x == ' Sales'):
        return 11
    elif (x == ' Tech-support'):
        return 12
    elif (x == ' Transport-moving'):
        return 13
# end of occuption

# chagnge race        
def transfer_race(x):
    if (x == ' White'):
        return 0
    elif (x == ' Amer-Indian-Eskimo'):
        return 1
    elif (x == ' Asian-Pac-Islander'):
        return 2
    elif (x == ' Black'):
        return 3
    elif (x == ' Other'):
        return 4
# end of transfer_race

# chagnge work class
def transfer_sex(x):
    if (x == ' Female'):
        return 0
    else:
        return 1   
# end of transfer_sex

'''
# chagnge native country
def transfer_nativeCountry(x):
    if (x == ' Canada' || x == ' United-States'):
        return 0
    elif (x == ' Married-AF-spouse'):
        return 1
    elif (x == ' Married-civ-spouse'):
        return 2
    elif (x == ' Married-spouse-absent'):
        return 3
    elif (x == ' Never-married'):
        return 4
    elif (x == ' Separated'):
        return 5
    elif (x == ' Widowed'):
        return 6
# end of transfer_nativeCountry
'''

# chagnge revenue
def transfer_revenue(x):
    if (x == ' <=50K'):
        return 0
    else:
        return 1   
# end of transfer_revenue

# Apply all the functions on data frame, and transfer all category data into numerical data
nb['workclass'] = nb['workclass'].apply(transfer_workclass)
nb['marital-status'] = nb['marital-status'].apply(transfer_marital)
nb['Occuption'] = nb['Occuption'].apply(transfer_occuption)
nb['race'] = nb['race'].apply(transfer_race)
nb['sex'] = nb['sex'].apply(transfer_sex)
#nb['native country'] = nb['native country'].apply(transfer_nativeCountry)
nb['revenue'] = nb['revenue'].apply(transfer_revenue)
print(nb.head(20))

