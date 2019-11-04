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

# Load dataset
url = "datasets/estabComp.csv"
names = ['CO_UNIDADE', 'CO_CNES', 'TP_PFPJ', 'NIVEL_DEP', 'CO_REGIAO_SAUDE', 'CO_ATIVIDADE', 'CO_CLIENTELA', 'TP_UNIDADE', 'CO_TURNO_ATENDIMENTO', 'CO_ESTADO_GESTOR', 'CO_MUNICIPIO_GESTOR', 'CO_CPFDIRETORCLN', 'CO_MOTIVO_DESAB', 'CO_NATUREZA_JUR', 'TP_ESTAB_SEMPRE_ABERTO', 'ST_CONEXAO_INTERNET', 'CO_TIPO_ESTABELECIMENTO', 'CO_ATIVIDADE_PRINCIPAL', 'ST_CONTRATO_FORMALIZADO', 'TP_GESTAO']
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset (separação do array em X(
array = dataset.values
X = array[:,0:-1]
Y = array[:,-1]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
print('jhgg')
# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print('accuracy_score',accuracy_score(Y_validation, predictions))
print('\n\nconfusion_matrix\n',confusion_matrix(Y_validation, predictions))
print('\n\nclassification_report\n',classification_report(Y_validation, predictions))

