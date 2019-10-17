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

def init():
  transform.makeUbsNotasDesempenho()
  # transform.getUbsAtivasPorUF().plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
  # transform.getUbsAtivasPorUF().hist()
  # scatter_matrix(transform.getUbsAtivasPorUF())
  # plt.show()