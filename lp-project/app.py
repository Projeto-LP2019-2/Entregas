import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


pathTransform = './transforms/'
pathDataSets = './datasets/'
pathImagens = './imagens/'

def getUFIBGE():
    data = pd.read_csv(pathDataSets+"ibge_ufs.csv", sep=',')
    return data

def getUbs():
    data = pd.read_csv(pathDataSets+"ubs.csv", sep=',')
    data.rename(columns={'vlr_latitude': 'lat', 'vlr_longitude': 'long', 'cod_cnes': 'cnes', 'cod_munic': 'cod_municipio'}, inplace=True)
    return data

def getUbsNotasDesempenho():
    data = pd.read_csv(pathTransform+"notas_ubs.csv", sep=',')
    data.rename(columns={'vlr_latitude': 'lat', 'vlr_longitude': 'long', 'cod_cnes': 'cnes', 'cod_munic': 'cod_municipio'}, inplace=True)
    return data

def getNotaDesempenho(strDesempenho):
    notas = {"Desempenho acima da media":2,"Desempenho mediano ou  um pouco abaixo da media":1,"Desempenho muito acima da media":3}
    return notas[strDesempenho]

def montaNotas(notas):
    data = pd.DataFrame(notas, columns = ['nt_dsc_estrut_fisic_ambiencia',
                                          'nt_dsc_adap_defic_fisic_idosos',
                                          'nt_dsc_equipamentos',
                                          'nt_dsc_medicamentos'])
    return data

def makeUbsNotasDesempenho():
    ubs = getUbs()
    notas = []
    for index, row in ubs.iterrows():
        notas.append((getNotaDesempenho(row['dsc_estrut_fisic_ambiencia']),
                     getNotaDesempenho(row['dsc_adap_defic_fisic_idosos']),
                     getNotaDesempenho(row['dsc_equipamentos']),
                     getNotaDesempenho(row['dsc_medicamentos'])))
    data = montaNotas(notas)
    data.to_csv(path_or_buf=pathTransform+"notas_ubs.csv")

    
def getUbsAtivas():
    data = pd.read_csv(pathDataSets+"ubs_ativas.csv", sep=';')
    data.rename(columns={'ibge': 'cod_municipio'}, inplace=True)
    return data

def makeUbsAtivasPorUF():
    data = pd.merge(getUbs(), getUbsAtivas(), how='inner')
    data = pd.merge(DFUbsAtivas, getUFIBGE(), how='inner')
    data.to_csv(path_or_buf=pathTransform+"ubs_ativas_com_estado.csv")
    
def getUbsAtivasPorUF():
    data = pd.read_csv(pathDataSets+"ubs_ativas.csv", sep=';')
    return data
    
def getInvestimentos(ano=None):
    data = pd.read_csv(pathDataSets+"investimentos.csv", sep=',')
    data.rename(columns={'estado_ibge': 'cod_estado'}, inplace=True)
    if ano:
        return data.query("ano == "+ano)  
    else:
        return data    

def makeInvestimentosAno(ano):
    data = pd.merge(getInvestimentos(ano), getUFIBGE(), how="inner")
    data.to_csv(path_or_buf=pathTransform+"investimentos_"+ano+".csv")
    
def getInvestimentosAno(ano):
    data = pd.read_csv(pathTransform+"investimentos_"+ano+".csv", sep=',')
    return data  

def getUnidadesPorEstado():
    data = pd.read_csv(pathTransform+"ubs_grouped_uf.csv", sep=',')
    return data

def graficoInvestimentosAno(ano,save=None):
    grafico = getInvestimentosAno(ano).plot(x='uf', y='valor',kind='bar', label="Investimentos")
    if save == True:
        grafico.get_figure().savefig(pathImagens+"invest-estado.png")
        
def graficoUnidadesPorEstado(save=None):
    data = getUnidadesPorEstado().plot(x='uf', y='count', kind='bar', label="Número de unidades")
    if save == True:
        data.get_figure().savefig(pathImagens+"ubs_uf.png")

def menu():
    print('comando')
    print('Deseja exibir os gráficos?')
    command = input(">> ")
    show = False
    if command.lower() == 'true':
        show = True
        matplotlib.use("WebAgg")
    elif command.lower() == 'false':
        matplotlib.use("Agg")
    print('Deseja salvar além de exibir os gráficos?')
    command = input(">> ")

    getUbsAtivas()
    makeInvestimentosAno('2014')
    graficoInvestimentosAno('2014',bool(command))
    graficoUnidadesPorEstado(bool(command))
    if show == True:
        plt.show()
