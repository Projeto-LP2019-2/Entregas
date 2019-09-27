import pandas as pd
import matplotlib

matplotlib.use("Agg")

datasetUbs = pd.read_csv('./ubs.csv', sep=',')
datasetUbsAtivas = pd.read_csv('./ubs_ativas.csv', sep=';')
investimentos = pd.read_csv('./investimentos.csv', sep=',')
ibge_ufs = pd.read_csv('./ibge_ufs.csv', sep=',')

datasetUbs.rename(columns={'vlr_latitude': 'lat', 'vlr_longitude': 'long', 'cod_cnes': 'cnes', 'cod_munic': 'cod_municipio'}, inplace=True)
datasetUbsAtivas.rename(columns={'ibge': 'cod_municipio'}, inplace=True)

investimentos.rename(columns={'estado_ibge': 'cod_estado'}, inplace=True)

ubs_ativas_2014 = pd.merge(datasetUbs, datasetUbsAtivas, how='inner')
ubs_ativas_com_estado = pd.merge(ubs_ativas_2014, ibge_ufs, how="inner")
ubs_ativas_com_estado.to_csv(path_or_buf="./transforms/ubs_ativas_com_estado.csv")

investimentos_2014 = pd.merge(investimentos.query("ano == 2014"), ibge_ufs, how="inner")
investimentos_2014.to_csv(path_or_buf="./transforms/investimentos_2014.csv")
plot = investimentos_2014.plot(x="uf", y="valor", kind="bar")
plot.get_figure().savefig("./imagens/invest-estado.png")

ubs_grouped_uf = ubs_ativas_com_estado.groupby(by=['uf'])

df_ubs_uf = pd.read_csv('./transforms/ubs_grouped_uf.csv', sep=',')
plot_uf = df_ubs_uf.plot(x='uf', y='count', kind="bar")
plot_uf.get_figure().savefig("./imagens/ubs_uf.png")
