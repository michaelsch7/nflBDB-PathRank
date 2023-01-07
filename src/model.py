import numpy as np
import pandas as pd
from DrawPath import drawPath


modelTrainData = pd.read_csv('nflFinalData/out2.csv')
modelTestData = pd.read_csv('nflFinalData/out3.csv')
# print(len(modelTestData)) 
# print(len(modelTrainData))

# print(modelTestData[['hurry', 'hit', 'sack']].value_counts())
# print(modelTrainData[['hurry', 'hit', 'sack']].value_counts())

totalData = pd.concat([modelTrainData, modelTestData], ignore_index=True)

totalData = totalData.query('(hurry == 1) or (hurry == 0)')
from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()

totalData['coverage'] = lab.fit_transform(totalData['coverage'])
totalData['pos'] = lab.fit_transform(totalData['pos'])
totalData['xVal'] = lab.fit_transform(totalData['xVal'])
totalData['yVal'] = lab.fit_transform(totalData['yVal'])

import seaborn as sns
import matplotlib as plt

# Heatmap for correlation 
heatM = sns.heatmap(totalData.corr())
fig = heatM.get_figure()
fig.savefig('heatmap3.png')

X = totalData[['playerId', 'pos', 'coverage', 'q', 'qb', 'avgSpeed', 'avgAcc', 'xVal', 'yVal']]
y = totalData[['hurry']]  

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = MultinomialNB().fit(X_train, y_train)

y_pred = model.predict(X_test)
print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
print('F1 score:', metrics.f1_score(y_test, y_pred, average="macro"))
