import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''notas = pd.Series([2,7,3,5,10,6], index=['a','b','c','d','e','f'])

print(notas)
print(notas**2)
print(notas.describe())
print(np.log(notas))'''


url1 = "BASE_DE_DADOS_CNES_201909\\tbEstabelecimento201909.csv"
df1 = pd.read_csv(url1,sep=';',engine='python')

#print(df.head(n=10))
#print(df[df["TP_GESTAO"] == 'E'])
#print(df["TP_GESTAO"].value_counts(normalize=True))
url2 = "BASE_DE_DADOS_CNES_201909\\rlEstabComplementar201909.csv"
df2 = pd.read_csv(url2,sep=',',engine='python')


'''df["ST_CONTRATO_FORMALIZADO"].fillna(99, inplace=True)
df2 = df2.replace({"ST_CONTRATO_FORMALIZADO": {np.nan: '0'}})
df.plot.scatter(x='CO_ATIVIDADE', y='TP_UNIDADE')
plt.show()'''

dfm = df1.merge(df2, left_on='CO_UNIDADE', right_on='CO_UNIDADE')
