#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:11:17 2018

@author: shaopan
"""
import pandas as pd
import numpy as np

# import file
file = 'no_questionMark.csv'
df = pd.read_csv(file)
print(df.head(10))
print(df.shape)
# origin dataframe shape (32561, 15)

# clean miss value row 
df_dropNull = df.dropna()
# clean useless column (Maybe)
#df_short = df_dropNull.drop(['], axis = 1)
print(df_dropNull.shape)
print(df_dropNull.head(10))
# dataframe shape after take out row with missing value (32561, 15)

