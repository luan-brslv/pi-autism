import random
import pandas as pd
from datetime import date

excel = pd.read_excel('scripts\\base\\Autism_Spectrum_Disorder_and_screentime_during_lockdown_copia.xlsx') 

def execute(entradas):
    # -g - é o script que será usado
    # -s - é o número de entradas
    # python main.py -s 100_000 -g 'lockdown'

    data_atual = date.today().strftime('%d-%m-%Y')
    data_list = []

    for id in range(1, entradas):
        data_list.append(generate_data(identificador = id)) 

    generate_file_csv(data_list, data_atual)

def generate_data(identificador):
    return {
        'ID': identificador,
        'mother/father ': random.choice(excel['mother/father '].tolist()),
        'child age ': random.choice(excel['child age '].tolist()),
        'child sex ': random.choice(excel['child sex '].tolist()), 
        'ASD diagnosis ': random.choice(excel['ASD diagnosis '].tolist()),
        'language competences ': random.choice(excel['language competences '].tolist()),
        'cognitive functioning': random.choice(excel['cognitive functioning'].tolist()),
        'language and communication ': random.choice(excel['language and communication '].tolist()),
        'emotional regulation ': random.choice(excel['emotional regulation '].tolist()),
        'social interaction ': random.choice(excel['social interaction '].tolist()),
        'stereotypes ': random.choice(excel['stereotypes '].tolist()),
        'behavioral problems ': random.choice(excel['behavioral problems '].tolist()),
        'restricted interests ': random.choice(excel['restricted interests '].tolist()),
        'autonomies ': random.choice(excel['autonomies '].tolist()),
        'tv': random.choice(excel['tv'].tolist()),
        'video-games': random.choice(excel['video-games'].tolist()),
        'play with frinds online ': random.choice(excel['play with frinds online '].tolist()),
        'social networks ': random.choice(excel['social networks '].tolist())
    }

def generate_file_csv(data_list, file_date):
    path = f'generated-data\\{file_date}-lockdown-generate.csv'
    df = pd.DataFrame(data_list)
    df.to_csv(path, sep=';', index=False)
    
