#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:39:39 2018

@author: shaopan
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
import seaborn as sb

# import file
file = 'all_number.csv'
df = pd.read_csv(file)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print("The following is summary of dataset:")
print("this is the dataframe size:")
print(df.shape)
# (30162, 14)
#print(df.head(5))
columns = list(df.columns.values)
columns.pop(0)
columns = columns[0:12]
print("This are the independent variable name: ")
print(columns)
print "The variable size is: ", len(columns)
dependent = df["revenue"]
independent = df.drop("revenue", axis = 1)
independent = independent.drop("Unnamed: 0", axis = 1)
print "The variable dataframe size is: ", independent.shape
df = pd.read_csv(file)

print("The following is the chart of some key variables, the have signifcant impact on model")
#columns: ['Age', 'workclass', 'fnlwgt', 'education num', 'marital-status', 
#           'Occuption', 'race', 'sex', 'capital gain', 'capital loss', 'hours per week']
sb.countplot(x = "workclass", hue = "revenue", data = df)
sb.countplot(x = "education num", hue = "revenue", data = df)
sb.countplot(x = "marital-status", hue = "revenue", data = df)
# class 2:  Married-civ-spouse married civilian spouse have obviou higher rate of high revenue
sb.countplot(x = "Occuption", hue = "revenue", data = df)
# class 3 & 9 have higher rate
sb.countplot(x = "sex", hue = "revenue", data = df)
# class 1: men has higher rate
independent["education num"].plot.hist()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print("Split dataframe into train set and test set")
# train independent variable trainI
# train dependent variable trainD 
# test independent variable testI 
# test dependent variable testD 
trainI, testI, trainD, testD = train_test_split(independent, dependent, test_size = 0.5)
print("")
print(trainI.shape)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("The following is logistic regression model")
# fit the model
logmodel = LogisticRegression()
logmodel.fit(trainI, trainD)
print("Train Done")

# predict
prediction = logmodel.predict(testI)
print("Test Done")

# report the test result
print(classification_report(testD, prediction))
print ("The following is the confusion matrix: ")
print(confusion_matrix(testD, prediction))
print("report done")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print("This is for Naive Bayes")
multiNB = MultinomialNB()
multiNB.fit(trainI, trianD)


