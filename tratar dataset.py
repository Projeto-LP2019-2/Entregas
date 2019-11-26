def tratar(dataset):
    dataset = dataset_tratar_genero(dataset)
    dataset = dataset_tratar_neighbourhood(dataset)
    #dataset = dataset_tratar_sms_received(dataset)

    return dataset

def dataset_tratar_genero(dataset):
    dataset = dataset.replace({"Gender": {"F": 0}})
    dataset = dataset.replace({"Gender": {"M": 1}})
    
    return dataset

def dataset_tratar_neighbourhood(dataset):
    bairros = dataset["Neighbourhood"].unique()
    for i in range(len(bairros)):
        dataset = dataset.replace({"Neighbourhood": {bairros[i]: i}})
    return dataset

def dataset_tratar_sms_received(dataset):
    dataset = dataset.replace({"SMS_received": {"Yes": 1}})
    dataset = dataset.replace({"SMS_received": {"No": 0}})
    return dataset
