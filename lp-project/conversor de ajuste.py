import csv
import pandas

url = "datasets/ubs_por_investimento.csv"
arquivo = open(url)
linhas = csv.reader(arquivo)


url = "datasets/ubs_por_estado.csv"
arquivo = open(url)
linhas2 = csv.reader(arquivo)

ubs = []
for linha in linhas2:
    temp = []
    for j in linha:
        if j =='Desempenho mediano ou  um pouco abaixo da mÃ©dia':
            temp.append(1)
        elif j == 'Desempenho acima da mÃ©dia':
            temp.append(2)
        elif j == 'Desempenho muito acima da mÃ©dia':
            temp.append(3)
        else:
            temp.append(j)
    ubs.append(temp)
    
valores = []
estados = []
for linha in linhas:
    estados.append(linha[1])
    valores.append(float(linha[0]))
soma = sum(valores)
n = len(valores)

media = soma/n

cont = 0
while cont < n:
    i = valores[cont]
    if i > (media+media/2):
        subs = 'muito maior que a media'
    elif i > media:
        subs = 'maior que a media'
    elif i < (media-media/2):
        subs = 'muito menor que a media'
    else:
        subs = 'menor ou igual a media'

    for j in ubs:
        if j[-1] == estados[cont]:
            j[-1] = subs
            
    cont +=1
    

with open("datasets/ubs_nivel_investimento.csv", 'w', newline='') as csvfile:
     writer = csv.writer(csvfile, delimiter=',')
     for i in ubs:
         
         writer.writerow(i)
