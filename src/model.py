import numpy as np
import pandas as pd
from DrawPath import drawPath


week1 = pd.read_csv('nflFinalData/out1.csv')
week2 = pd.read_csv('nflFinalData/out2.csv')
week3 = pd.read_csv('nflFinalData/out3.csv')
week4 = pd.read_csv('nflFinalData/out4.csv')
week5 = pd.read_csv('nflFinalData/out5.csv')
week6 = pd.read_csv('nflFinalData/out6.csv')
week7 = pd.read_csv('nflFinalData/out7.csv')
week8 = pd.read_csv('nflFinalData/out8.csv')

totalData = pd.concat([week1, week2, week3, week4, week5, week6, week7, week8], ignore_index=True)

totalData = totalData.query('(hurry == 1) or (hurry == 0)')

from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()

totalData['coverage'] = lab.fit_transform(totalData['coverage'])
totalData['pos'] = lab.fit_transform(totalData['pos'])
totalData['xVal'] = lab.fit_transform(totalData['xVal'])
totalData['yVal'] = lab.fit_transform(totalData['yVal'])

print(totalData.hurry.value_counts())
compression_opts = dict(method='zip',
                        archive_name='finalData.csv')  
totalData.to_csv('fd.zip', index=False,
          compression=compression_opts) 
import seaborn as sns
import matplotlib as plt

# Heatmap for correlation 
heatM = sns.heatmap(totalData.corr())
fig = heatM.get_figure()
fig.savefig('heatmap3.png')

X = totalData[['playerId', 'pos', 'coverage', 'q', 'qb', 'avgSpeed', 'avgAcc', 'xVal', 'yVal']].copy()
y = totalData[['hurry']]


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(metrics.classification_report(y_test, y_pred))
print(clf.feature_importances_)
