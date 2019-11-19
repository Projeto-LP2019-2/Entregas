def read_to_text(name):
    file = open(name,encoding="ANSI")
    linhas = file.read()
    file.close()
    return linhas

def read_to_list(name):
    file = open(name,encoding="ANSI")
    linhas = file.readlines()
    file.close()
    return linhas

def save(name,text):
    file = open(name,'w')
    file.write(text)

def read_to_dict(name):
    linhas = read_to_list(name)
    dataset = {'linhas':[]}
    for linha in linhas:
        linha = linha.replace('\n','')
        linha_lst = linha.split(',')
        reg = {'PatientId':linha_lst[0],
               'AppointmentID':linha_lst[1],
               'Gender':linha_lst[2],
               'ScheduledDay':linha_lst[3],
               'AppointmentDay':linha_lst[4],
               'Age':linha_lst[5],
               'Neighbourhood':linha_lst[6],
               'Scholarship':linha_lst[7],
               'Hipertension':linha_lst[8],
               'Diabetes':linha_lst[9],
               'Alcoholism':linha_lst[10],
               'Handcap':linha_lst[11],
               'SMS_received':linha_lst[12],
               'No-show':linha_lst[13],
               }
        dataset['linhas'].append(reg)
    return dataset

def read_to_dict_sem_titulo(name):
    linhas = read_to_list(name)
    dataset = {'linhas':[]}
    for linha in linhas[1:]:
        linha = linha.replace('\n','')
        linha_lst = linha.split(',')
        reg = {'PatientId':linha_lst[0],
               'AppointmentID':linha_lst[1],
               'Gender':linha_lst[2],
               'ScheduledDay':linha_lst[3],
               'AppointmentDay':linha_lst[4],
               'Age':linha_lst[5],
               'Neighbourhood':linha_lst[6],
               'Scholarship':linha_lst[7],
               'Hipertension':linha_lst[8],
               'Diabetes':linha_lst[9],
               'Alcoholism':linha_lst[10],
               'Handcap':linha_lst[11],
               'SMS_received':linha_lst[12],
               'No-show':linha_lst[13],
               }
        dataset['linhas'].append(reg)
    return dataset

def dataset_tratar_genero(dataset):
    for linha in dataset['linhas']:
        if linha['Gender'].upper() == 'F':
            linha['Gender'] = '0'
        if linha['Gender'].upper() == 'M':
            linha['Gender'] = '1'
    return dataset


def dataset_tratar_scheduledday(dataset):
    for linha in dataset['linhas']:
        linha['ScheduledDay'] = linha['ScheduledDay'].replace('-','')
        linha['ScheduledDay'] = linha['ScheduledDay'].replace('T','')
        linha['ScheduledDay'] = linha['ScheduledDay'].replace(':','')
        linha['ScheduledDay'] = linha['ScheduledDay'].replace('Z','')
    return dataset

def dataset_tratar_appointmentday(dataset):
    for linha in dataset['linhas']:
        linha['AppointmentDay'] = linha['AppointmentDay'].replace('-','')
        linha['AppointmentDay'] = linha['AppointmentDay'].replace('T','')
        linha['AppointmentDay'] = linha['AppointmentDay'].replace(':','')
        linha['AppointmentDay'] = linha['AppointmentDay'].replace('Z','')
    return dataset

def dataset_tratar_neighbourhood(dataset):
    config = {'AEROPORTO' : 0, 
              'ANDORINHAS' : 1,
              'ANTÃ”NIO HONÃ“RIO' : 2,
              'ARIOVALDO FAVALESSA' : 3,
              'BARRO VERMELHO' : 4,
              'BELA VISTA' : 5,
              'BENTO FERREIRA' : 6,
              'BOA VISTA' : 7,
              'BONFIM' : 8,
              'CARATOÃ\x8dRA' : 9,
              'CENTRO' : 10,
              'COMDUSA' : 11,
              'CONQUISTA' : 12,
              'CONSOLAÃ‡ÃƒO' : 13,
              'CRUZAMENTO' : 14,
              'DA PENHA' : 15,
              'DE LOURDES' : 16,
              'DO CABRAL' : 17,
              'DO MOSCOSO' : 18,
              'DO QUADRO' : 19,
              'ENSEADA DO SUÃ\x81' : 20,
              'ESTRELINHA' : 21,
              'FONTE GRANDE' : 22,
              'FORTE SÃƒO JOÃƒO' : 23,
              'FRADINHOS' : 24,
              'GOIABEIRAS' : 25,
              'GRANDE VITÃ“RIA' : 26,
              'GURIGICA' : 27,
              'HORTO' : 28,
              'ILHA DAS CAIEIRAS' : 29,
              'ILHA DE SANTA MARIA' : 30,
              'ILHA DO BOI' : 31,
              'ILHA DO FRADE' : 32,
              'ILHA DO PRÃ\x8dNCIPE' : 33,
              'ILHAS OCEÃ‚NICAS DE TRINDADE' : 34,
              'INHANGUETÃ\x81' : 35,
              'ITARARÃ‰' : 36,
              'JABOUR' : 37,
              'JARDIM CAMBURI' : 38,
              'JARDIM DA PENHA' : 39,
              'JESUS DE NAZARETH' : 40,
              'JOANA DÂ´ARC' : 41,
              'JUCUTUQUARA' : 42,
              'MÃ\x81RIO CYPRESTE' : 43,
              'MARIA ORTIZ' : 44,
              'MARUÃ\x8dPE' : 45,
              'MATA DA PRAIA' : 46,
              'MONTE BELO' : 47,
              'MORADA DE CAMBURI' : 48,
              'NAZARETH' : 49,
              'NOVA PALESTINA' : 50,
              'PARQUE INDUSTRIAL' : 51,
              'PARQUE MOSCOSO' : 52,
              'PIEDADE' : 53,
              'PONTAL DE CAMBURI' : 54,
              'PRAIA DO CANTO' : 55,
              'PRAIA DO SUÃ\x81' : 56,
              'REDENÃ‡ÃƒO' : 57,
              'REPÃšBLICA' : 58,
              'RESISTÃŠNCIA' : 59,
              'ROMÃƒO' : 60,
              'SÃƒO BENEDITO' : 61,
              'SÃƒO CRISTÃ“VÃƒO' : 62,
              'SÃƒO JOSÃ‰' : 63,
              'SÃƒO PEDRO' : 64,
              'SANTA CECÃ\x8dLIA' : 65,
              'SANTA CLARA' : 66,
              'SANTA HELENA' : 67,
              'SANTA LÃšCIA' : 68,
              'SANTA LUÃ\x8dZA' : 69,
              'SANTA MARTHA' : 70,
              'SANTA TEREZA' : 71,
              'SANTO ANDRÃ‰' : 72,
              'SANTO ANTÃ”NIO' : 73,
              'SANTOS DUMONT' : 74,
              'SANTOS REIS' : 75,
              'SEGURANÃ‡A DO LAR' : 76,
              'SOLON BORGES' : 77,
              'TABUAZEIRO' : 78,
              'UNIVERSITÃ\x81RIO' : 79,
              'VILA RUBIM': 80
    }
    for linha in dataset['linhas']:
        linha['Neighbourhood'] = config[linha['Neighbourhood']]
    return dataset

def dataset_tratar_sms_received(dataset):
    for linha in dataset['linhas']:
        if linha['Gender'].upper() == 'NO':
            linha['Gender'] = '0'
        if linha['Gender'].upper() == 'YES':
            linha['Gender'] = '1'
    return dataset

def tratar_dataset_all(name):
    dataset = read_to_dict_sem_titulo(name)
    dataset = dataset_tratar_genero(dataset)
    dataset = dataset_tratar_scheduledday(dataset)
    dataset = dataset_tratar_appointmentday(dataset)
    dataset = dataset_tratar_neighbourhood(dataset)
    dataset = dataset_tratar_sms_received(dataset)
    return dataset

def salvar_dataset(name,dataset,limit):
    texto = ''
    texto = texto + 'PatientId,AppointmentID,Gender,ScheduledDay,AppointmentDay,Age,Neighbourhood,Scholarship,Hipertension,Diabetes,Alcoholism,Handcap,SMS_received,No-show' + '\n'
    linha_str = ''
    concluido = 0
    for linha in dataset['linhas']:
        linha_str = linha_str + str(linha['PatientId']) + ','
        linha_str = linha_str + str(linha['AppointmentID']) + ','
        linha_str = linha_str + str(linha['Gender']) + ','
        linha_str = linha_str + str(linha['ScheduledDay']) + ','
        linha_str = linha_str + str(linha['AppointmentDay']) + ','
        linha_str = linha_str + str(linha['Age']) + ','
        linha_str = linha_str + str(linha['Neighbourhood']) + ','
        linha_str = linha_str + str(linha['Scholarship']) + ','
        linha_str = linha_str + str(linha['Hipertension']) + ','
        linha_str = linha_str + str(linha['Diabetes']) + ','
        linha_str = linha_str + str(linha['Alcoholism']) + ','
        linha_str = linha_str + str(linha['Handcap']) + ','
        linha_str = linha_str + str(linha['SMS_received']) + ','
        linha_str = linha_str + str(linha['No-show'])
        linha_str = linha_str + '\n'
        texto = texto + linha_str
        concluido += 1
        print(str((concluido/len(dataset['linhas']))*100)[0:4] + '%')
        print(linha_str)
        if(concluido == limit):
            break
    save(name,texto)

salvar_dataset('noshowappointments_tratado.csv',tratar_dataset_all('noshowappointments.csv'),50)

















