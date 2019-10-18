#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import transform

validation_size = 0.20
seed = 7
scoring = 'accuracy'

def init():
  # transform.show()
  dataset = pandas.read_csv('./transforms/notas_ubs.csv')
  print dataset.shape
  X = dataset.values[:, 1:4]
  Y = dataset.values[:, 5]

  # print X
  # print
  # print Y[0]
  X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

  algorythmAnalysis(X_train, X_validation, Y_train, Y_validation, True)
  # transform.getUbsAtivasPorUF().plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
  # transform.getUbsAtivasPorUF().hist()
  # scatter_matrix(transform.getUbsAtivasPorUF())
  # plt.show()

def algorythmAnalysis(X_train, X_validation, Y_train, Y_validation, saveFig=False):
  models = []
  results = []
  names = []
  models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
  models.append(('LDA', LinearDiscriminantAnalysis()))
  models.append(('KNN', KNeighborsClassifier()))
  models.append(('CART', DecisionTreeClassifier()))
  models.append(('NB', GaussianNB()))
  models.append(('SVM', SVC(gamma='auto')))

  for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

  fig = plt.figure()
  fig.suptitle('Algorithm Comparison')
  ax = fig.add_subplot(111)
  plt.boxplot(results)
  ax.set_xticklabels(names)
  plt.show()