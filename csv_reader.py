import csv

arquivo = open('ubs.csv', encoding="utf8")

ubs = csv.DictReader(arquivo)
med_acima_media=0
med_mediano_abaixo=0
for ubs in ubs:
    if ubs["dsc_medicamentos"]=="Desempenho acima da média":
        med_acima_media=med_acima_media+1
        
    elif ubs["dsc_medicamentos"]=="Desempenho mediano ou  um pouco abaixo da média":
        med_mediano_abaixo=med_mediano_abaixo+1
        


print(med_acima_media)

print(med_mediano_abaixo)  
