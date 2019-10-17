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
url = "datasets/ubs_por_estado.csv"
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['ambiencia', 'idosos', 'equipamentos', 'medicamentos', 'estado']
dataset = pandas.read_csv(url, names=names)

dataset.ambiencia[dataset.ambiencia == 'Desempenho mediano ou  um pouco abaixo da média'] = 1
dataset.ambiencia[dataset.ambiencia == 'Desempenho acima da média'] = 2
dataset.ambiencia[dataset.ambiencia == 'Desempenho muito acima da média'] = 3

dataset.idosos[dataset.idosos == 'Desempenho mediano ou  um pouco abaixo da média'] = 1
dataset.idosos[dataset.idosos == 'Desempenho acima da média'] = 2
dataset.idosos[dataset.idosos == 'Desempenho muito acima da média'] = 3

dataset.equipamentos[dataset.equipamentos == 'Desempenho mediano ou  um pouco abaixo da média'] = 1
dataset.equipamentos[dataset.equipamentos == 'Desempenho acima da média'] = 2
dataset.equipamentos[dataset.equipamentos == 'Desempenho muito acima da média'] = 3

dataset.medicamentos[dataset.medicamentos == 'Desempenho mediano ou  um pouco abaixo da média'] = 1
dataset.medicamentos[dataset.medicamentos == 'Desempenho acima da média'] = 2
dataset.medicamentos[dataset.medicamentos == 'Desempenho muito acima da média'] = 3

# shape (tamanho (linhas, colunas) do dataset)
'''print('shape   ', dataset.shape)
print('\n\n')'''

# head ( primeiras n linhas do dataset)
'''n = 2
print(dataset.head(n))
print('\n\n')'''

# class distribution (quantidade de linhas por estado)
'''print(dataset.groupby('estado').size())
print('\n\n')'''

# box and whisker plots
'''dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()'''

# Split-out validation dataset (separação do array em X(
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

'''# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)'''

'''# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()'''

# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print('accuracy_score',accuracy_score(Y_validation, predictions))
print('\n\nconfusion_matrix\n',confusion_matrix(Y_validation, predictions))
print('\n\nclassification_report\n',classification_report(Y_validation, predictions))

'''a = len(predictions)

while a > 0:
    a -= 1
    print(X_validation[a],Y_validation[a])
    print(predictions[a])
    if Y_validation[a] == predictions[a]:
        print(True)
    else: print(False)'''

