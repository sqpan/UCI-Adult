#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:11:17 2018

@author: shaopan
"""
import pandas as pd
import numpy as np

# import file
file = 'adult_data.csv'
df = pd.read_csv(file, header = None)

print(df.head())