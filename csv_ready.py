import csv
 
def contar_coluna(coluna):
    arquivo = open('ubs.csv', encoding="utf8")

    ubs = csv.DictReader(arquivo)
    acima_media=0
    mediano_abaixo=0
    muito_acima=0
    for ubs in ubs:
      if ubs[coluna]=="Desempenho acima da média":
            acima_media=acima_media+1

      elif ubs[coluna]=="Desempenho muito acima da média":
            muito_acima=muito_acima+1
	     
      elif ubs[coluna]=="Desempenho mediano ou  um pouco abaixo da média":
            mediano_abaixo=mediano_abaixo+1
	        
    valor_acima_media=acima_media/(acima_media+muito_acima+mediano_abaixo)*100
    valor_muito_acima=muito_acima/(acima_media+muito_acima+mediano_abaixo)*100
    valor_mediano_abaixo=mediano_abaixo/(acima_media+muito_acima+mediano_abaixo)*100
    
    return valor_acima_media, valor_muito_acima, valor_mediano_abaixo


med=contar_coluna("dsc_medicamentos")
equip=contar_coluna("dsc_equipamentos")
fisido=contar_coluna("dsc_adap_defic_fisic_idosos")
infra=contar_coluna("dsc_estrut_fisic_ambiencia")

print("                                 |   Medicamentos    |      Equipamento       | DEFICIENTE e FÍSICO IDOSO  |  Estrutura Fisica |")
print("                  acima da média:|  %.2f"%med[0],"%","         |     %.2f"%equip[0],"%","           |     %.2f"%fisido[0],"%","               |     %.2f"%infra[0],"%")
print("            muito acima da média:|  %.2f"%med[1],"%","         |     %.2f"%equip[1],"%","            |     %.2f"%fisido[1],"%","               |     %.2f"%infra[1],"%")
print("mediano um pouco abaixo da média:|  %.2f"%med[2],"%","         |     %.2f"%equip[2],"%","           |     %.2f"%fisido[2],"%","               |     %.2f"%infra[2],"%")


