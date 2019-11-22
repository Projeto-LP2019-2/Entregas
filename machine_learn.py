import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from datasets.tratar_dataset import *

def getInfoContent():
    url = "datasets/noshowappointments_tratado.csv"
    cols = ['PatientId','AppointmentID','Gender','ScheduledDay','AppointmentDay','Age','Neighbourhood','Scholarship','Hipertension','Diabetes','Alcoholism','Handcap','SMS_received']
    return {"url":url,"cols":cols}

def getInfoComparator():
    url = "datasets/noshowappointments_tratado.csv"
    cols = ['No-show']
    return {"url":url,"cols":cols}

def run():
    X = pd.read_csv(getInfoContent()['url'], usecols=getInfoContent()['cols'], header=0)
    Y = pd.read_csv(getInfoComparator()['url'], usecols=getInfoComparator()['cols'], header=0)
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

    # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train.values.ravel())
    predictions = knn.predict(X_validation)
    print('accuracy_score',accuracy_score(Y_validation, predictions))
    print('\n\nconfusion_matrix\n',confusion_matrix(Y_validation, predictions))
    print('\n\nclassification_report\n',classification_report(Y_validation, predictions))

def runExcluindoColuna():
    def rodarKNN(dataset, col):
        array = dataset.values
        X = array[:,0:-1]
        Y = array[:,-1]
        validation_size = 0.20
        seed = 7
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
        
        # Make predictions on validation dataset
        knn = KNeighborsClassifier()
        knn.fit(X_train, Y_train)
        predictions = knn.predict(X_validation)
        acuracia = accuracy_score(Y_validation, predictions)
        return acuracia

    url = "datasets/noshowappointments_tratado.csv"

    dataset = pd.read_csv(url)
    dataset = dataset.drop(columns = ['PatientId','ScheduledDay','AppointmentDay','AppointmentID'])

    cols = (dataset.columns).delete(-1)

    resultados = {}
    i = 'padrao'
    resultado = rodarKNN(dataset, i)
    resultados[i] = resultado
    print(i + '   ', resultado)

    for i in cols:
        '''resultados['removido  ' + i]'''
        resultado = rodarKNN(dataset.drop(i, axis = 1), i)
        print('removido  ' + i + '   ', resultado)

    ordenar = sorted(resultados.items(), key=lambda kv: kv[1])

    for i in ordenar:
            print(i)


def tratarDataset():
    arquivoOrigem  = 'datasets/noshowappointments.csv'
    arquivoDestino = 'datasets/noshowappointments_tratado.csv'
    limitNumber    = 200
    limitPercent   = None
    salvar_dataset(arquivoDestino,tratar_dataset_all(arquivoOrigem),limitNumber=limitNumber,limitPercent=limitPercent)

tratarDataset()
run()
