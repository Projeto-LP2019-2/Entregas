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

def getInfoTabelao():
    url = "datasets/TABELAO_numerico.csv"
    cols = ['CO_CNES','TP_PFPJ','NIVEL_DEP','CO_CEP','CO_REGIAO_SAUDE','NU_CNPJ','CO_ATIVIDADE','CO_CLIENTELA','TP_ORGAO_EXPEDIDOR','TP_UNIDADE','CO_TURNO_ATENDIMENTO','CO_ESTADO_GESTOR','CO_MUNICIPIO_GESTOR','CO_CPFDIRETORCLN','REG_DIRETORCLN','CO_NATUREZA_JUR','TP_ESTAB_SEMPRE_ABERTO','ST_CONEXAO_INTERNET','TP_GESTAO','CO_TIPO_ESTABELECIMENTO','CO_ATIVIDADE_PRINCIPAL','CO_LEITO','CO_TIPO_LEITO','QT_EXIST','QT_SUS','ST_NMPROF_CADSUS','CO_CBO','TP_SUS_NAO_SUS','IND_VINCULACAO','TP_TERCEIRO_SIH','QT_CARGA_HORARIA_AMBULATORIAL','CO_CONSELHO_CLASSE','SG_UF_CRM','TP_PRECEPTOR','TP_RESIDENTE']
    return {"url":url,"cols":cols}

def load_dataset(url,colunas):
    dataset = pandas.read_csv(url, names=colunas)
    return dataset

def run():
    array = load_dataset(getInfoTabelao()['url'],getInfoTabelao()['cols']).values
    X = array
    Y = array[:,2]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

    # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_validation)
    print('accuracy_score',accuracy_score(Y_validation, predictions))
    print('\n\nconfusion_matrix\n',confusion_matrix(Y_validation, predictions))
    print('\n\nclassification_report\n',classification_report(Y_validation, predictions))

run()
