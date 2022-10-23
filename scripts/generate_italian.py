import random
import pandas as pd
from datetime import date

excel_con = pd.read_excel('scripts\\base\\AUTISM-Brain sciences-Panerai et al-raw data.xlsx', sheet_name='ASD con probl alimentari') 
excel_no = pd.read_excel('scripts\\base\\AUTISM-Brain sciences-Panerai et al-raw data.xlsx', sheet_name='ASD- no problemi alimentari') 

def execute(entradas):
    # -g - é o script que será usado
    # -s - é o número de entradas
    # python main.py -s 100_000 -g 'lockdown'

    data_atual = date.today().strftime('%d-%m-%Y')
    data_list_con = []
    data_list_no = []

    for id in range(1, entradas):
        data_list_no.append(generate_data(identificador = id, prob_al = False)) 

    for id in range(1, entradas):
        data_list_con.append(generate_data(identificador = id, prob_al = True)) 
        
    generate_file_csv(data_list_no, data_atual, False)
    generate_file_csv(data_list_con, data_atual, True)

def generate_data(identificador, prob_al):
    if(prob_al == False): 
        return {
            'codice ': identificador,
            'genere M/F': generate_column1(),
            'diagnosi (inserire anche il livello di supporto e la compromissione intellettiva e del linguaggio)': generate_column2(prob_al),
            'istruzione padre/madre': generate_column3(), 
            'Lavoro padre / madre': generate_column4(),
            'età cronologica in anni e mesi': generate_column5(),
            'età cronologica in mesi': generate_column6(),
            'età di sviluppo ': generate_column7(),
            'test usato per l\'età di sviluppo (PEP-3 ; Brunet Lézine; griffith; altri)': generate_column8(),
            'QI': generate_column9(),
            'test usato per il QI': generate_column10(),
            'ados*': generate_column11(),
            'cars 2*': generate_column12(),
            'CASD*': generate_column13(),
            'BAMBI  (max punteggio 90; cut-off 34)': generate_column14(),
            'Food selectivity (max punteggio 20) items 10-11-13-15': generate_column15(),
            'Disruptive mealtime behav (max 25) item 1-3-5-6-7': generate_column16(),
            'food refusal (max 15) items 2-4-8': generate_column17(),
            'mealtime rigidity (max 15) items 9-16-18': generate_column18(),
            'SEQ: totale': generate_column19(),
            'SEQ: totale HY': generate_column20(),
            'SEQ: sub-totale HY-S': generate_column21(),
            'SEQ: sub-totale HY-NS': generate_column22(),
            'SEQ: totale HO': generate_column23(),
            'SEQ: sub-totale HO-S': generate_column24(),
            'SEQ: sub-totale HO-NS': generate_column25(),
            'CEBQ totale': generate_column26(),
            'CEBQ: risposta al cibo': generate_column27(),
            'CEBQ: sovra-alimentaz. Emozionale': generate_column28(),
            'CEBQ: gradimento del cibo': generate_column29(),
            'CEBQ: desiderio di bere ': generate_column30(),
            'CEBQ: risposta sazietà': generate_column31(),
            'CEBQ: lentezza nell\'alimentarsi': generate_column32(),
            'CEBQ: sotto-alimentazione emozionale': generate_column33(),
            'CEBQ: selettività verso il cibo': generate_column34(),
            'SSP (short sensory profile): TOTALE': generate_column35(),
            'SSP: sensibilità tattile': generate_column36(),
            'SSP: sensibilità olfattiva-gustativa': generate_column37(),
            'SSP: sensibilità motoria': generate_column38(),
            'SSP: ipo-risposta /ricerca di sensazioni': generate_column39(),
            'SSP: filtro uditivo': generate_column40(),
            'SSP: bassa energia/debolezza': generate_column41(),
            'SSP: sensibilità visiva-uditiva': generate_column42()
        }
    elif(prob_al == True):
        return {        
            'CODICE ': identificador,
            'genere M/F': generate_column1(),
            'diagnosi (inserire anche il livello di supporto e la compromissione intellettiva e del linguaggio)': generate_column2(prob_al),
            'istruzione padre/madre': generate_column3(), 
            'Lavoro padre / madre': generate_column4(),
            'età cronologica in anni e mesi': generate_column5(),
            'età cronologica in mesi': generate_column6(),
            'età di sviluppo (in mesi)** ': generate_column7(),
            'test usato per l\'età di sviluppo (PEP-3 ; Brunet Lézine; griffith; altri)': generate_column8(),
            'QI**': generate_column9(),
            'test usato per il QI': generate_column10(),
            'ados*': generate_column11(),
            'cars 2*': generate_column12(),
            'CASD*': generate_column13(),
            'BAMBI  (max punteggio 90; cut-off 34)': generate_column14(),
            'Food selectivity (max punteggio 20) items 10-11-13-15': generate_column15(),
            'Disruptive mealtime behav (max 25) item 1-3-5-6-7': generate_column16(),
            'food refusal (max 15) items 2-4-8': generate_column17(),
            'mealtime rigidity (max 15) items 9-16-18': generate_column18(),
            'SEQ: totale': generate_column19(),
            'SEQ: totale HY': generate_column20(),
            'SEQ: sub-totale HY-S': generate_column21(),
            'SEQ: sub-totale HY-NS': generate_column22(),
            'SEQ: totale HO': generate_column23(),
            'SEQ: sub-totale HO-S': generate_column24(),
            'SEQ: sub-totale HO-NS': generate_column25(),
            'CEBQ totale': generate_column26(),
            'CEBQ: risposta al cibo': generate_column27(),
            'CEBQ: sovra-alimentaz. Emozionale': generate_column28(),
            'CEBQ: gradimento del cibo': generate_column29(),
            'CEBQ: desiderio di bere ': generate_column30(),
            'CEBQ: risposta sazietà': generate_column31(),
            'CEBQ: lentezza nell\'alimentarsi': generate_column32(),
            'CEBQ: sotto-alimentazione emozionale': generate_column33(),
            'CEBQ: selettività verso il cibo': generate_column34(),
            'SSP (short sensory profile): TOTALE': generate_column35(),
            'SSP: sensibilità tattile': generate_column36(),
            'SSP: sensibilità olfattiva-gustativa': generate_column37(),
            'SSP: sensibilità motoria': generate_column38(),
            'SSP: ipo-risposta /ricerca di sensazioni': generate_column39(),
            'SSP: filtro uditivo': generate_column40(),
            'SSP: bassa energia/debolezza': generate_column41(),
            'SSP: sensibilità visiva-uditiva': generate_column42()        
        }
        
def generate_file_csv(data_list, file_date, prob_al):
    if(prob_al == True):
        path = f'generated-data\\{file_date}-asd_con_probl_alimentari-generate.csv'    
    elif(prob_al == False):
        path = f'generated-data\\{file_date}-asd_no_probl_alimentari-generate.csv'
        
    df = pd.DataFrame(data_list)
    df.to_csv(path, index=False)
    
def generate_column1():
    genere_choose = random.randint(1, 101)
    genere = None
    
    if(genere_choose <= 80):
        genere = 'M'
    elif(genere_choose <= 100):
        genere = 'F'
    else:
        genere = None 
        
    return genere

def generate_column2(prob_al):
    most_commum = []
    if(prob_al == False):
        most_commum = ['Disturbo dello Spettro dell’Autismo, livello 3, con compromissione del linguaggio ed intellettiva associata.','Disturbo dello Spettro dell\'Autismo, livello 3, con compromissione intellettiva e del linguaggio associate','Disturbo dello spettro dell\'Autismo, livello di supporto 3, con ritardo globale dello sviluppo e compromissione del linguaggio associata', 'Disturbo dello sprettro dell\'autismo, livello 3. compromissione cognitiva', 'Disturbo dello sprettro dell\'autismo, livello 3compromissione cognitiva']
        excel = excel_no
    else:
        most_commum = ['ASD 3 e RGS', 'Disturbo dello sprettro dell\'autismo, livello 3. Compromissione intellettiva', 'ASD 3, DI NAS, assenza di linguaggio']
        excel = excel_con
   
    part = random.randint(1, 4) 
    column_data = None
    if(part == 1):  
        choose = random.randint(1, 22)
        if(choose <= 7):
            column_data = most_commum[0]
        else:
            column_data = random.choice(most_commum)                             
    else:
        column_data = random.choice(excel['diagnosi (inserire anche il livello di supporto e la compromissione intellettiva e del linguaggio)'].drop_duplicates().dropna().sort_values().tolist())    
    
    return column_data

# def generate_child_sex():
#     child_sex_choose = random.randint(1, 101)
#     child_sex = None
    
#     if(child_sex_choose <= 86):
#         child_sex = 0
#     elif(child_sex_choose <= 100):
#         child_sex = 1
#     else:
#         child_sex = None 
        
#     return child_sex

# def generate_asd_diagnosis():
#     asd_diagnosis_choose = random.randint(1, 101)
#     asd_diagnosis = None
    
#     if(asd_diagnosis_choose <= 45):
#         asd_diagnosis = 2
#     elif(asd_diagnosis_choose <= 73):
#         asd_diagnosis = 1
#     elif(asd_diagnosis_choose <= 100):
#         asd_diagnosis = 3       
#     else:
#         asd_diagnosis = None 
        
#     return asd_diagnosis    

# def generate_language_competences():
#     language_competences_choose = random.randint(1, 101)
#     language_competences = None
    
#     if(language_competences_choose <= 38):
#         language_competences = 2
#     elif(language_competences_choose <= 61):
#         language_competences = 0
#     elif(language_competences_choose <= 81):
#         language_competences = 3  
#     elif(language_competences_choose <= 100):
#         language_competences = 1               
#     else:
#         language_competences = None 
        
#     return language_competences        

# def generate_cognitive_functioning():
#     cognitive_functioning_choose = random.randint(1, 101)
#     cognitive_functioning = None 
    
#     if(cognitive_functioning_choose <= 47):
#         cognitive_functioning = 2
#     elif(cognitive_functioning_choose <= 80):
#         cognitive_functioning = 3
#     elif(cognitive_functioning_choose <= 100):
#         cognitive_functioning = 1   
#     else:
#         cognitive_functioning = None 
        
#     return cognitive_functioning    

# def generate_language_and_communication():
#     language_and_communication_choose = random.randint(1, 100)
#     language_and_communication = None
    
#     if(language_and_communication_choose <= 62):
#         language_and_communication = 3
#     elif(language_and_communication_choose <= 86):
#         language_and_communication = 2
#     elif(language_and_communication_choose <= 99):
#         language_and_communication = 1  
#     elif(language_and_communication_choose == 100):
#         language_and_communication = None               
        
#     return language_and_communication 

# def generate_emotional_regulation():
#     emotional_regulation_choose = random.randint(1, 100)
#     emotional_regulation = None
    
#     if(emotional_regulation_choose <= 40):
#         emotional_regulation = 3
#     elif(emotional_regulation_choose <= 71):
#         emotional_regulation = 2
#     elif(emotional_regulation_choose <= 98):
#         emotional_regulation = 1  
#     elif(emotional_regulation_choose <= 100):
#         emotional_regulation = None               
        
#     return emotional_regulation        

# def generate_social_interaction():
#     social_interaction_choose = random.randint(1, 100)
#     social_interaction = None
    
#     if(social_interaction_choose <= 36):
#         social_interaction = 3
#     elif(social_interaction_choose <= 68):
#         social_interaction = 1
#     elif(social_interaction_choose <= 97):
#         social_interaction = 2 
#     elif(social_interaction_choose <= 100):
#         social_interaction = None               
        
#     return social_interaction        

# def generate_stereotypes():
#     stereotypes_choose = random.randint(1, 100)
#     stereotypes = None
    
#     if(stereotypes_choose <= 42):
#         stereotypes = 2
#     elif(stereotypes_choose <= 76):
#         stereotypes = 1
#     elif(stereotypes_choose <= 98):
#         stereotypes = 3
#     elif(stereotypes_choose <= 100):
#         stereotypes = None               
        
#     return stereotypes        

# def generate_behavioral_problems():
#     behavioral_problems_choose = random.randint(1, 100)
#     behavioral_problems = None
    
#     if(behavioral_problems_choose <= 39):
#         behavioral_problems = 2
#     elif(behavioral_problems_choose <= 72):
#         behavioral_problems = 1
#     elif(behavioral_problems_choose <= 98):
#         behavioral_problems = 3
#     elif(behavioral_problems_choose <= 100):
#         behavioral_problems = None               
        
#     return behavioral_problems        

# def generate_restricted_interests():
#     restricted_interests_choose = random.randint(1, 100)
#     restricted_interests = None
    
#     if(restricted_interests_choose <= 34):
#         restricted_interests = 1
#     elif(restricted_interests_choose <= 67):
#         restricted_interests = 2
#     elif(restricted_interests_choose <= 98):
#         restricted_interests = 3 
#     elif(restricted_interests_choose <= 100):
#         restricted_interests = None               
        
#     return restricted_interests      

# def generate_autonomies():
#     autonomies_choose = random.randint(1, 100)
#     autonomies = None
    
#     if(autonomies_choose <= 52):
#         autonomies = 3
#     elif(autonomies_choose <= 84):
#         autonomies = 2
#     elif(autonomies_choose <= 96):
#         autonomies = 1 
#     elif(autonomies_choose <= 99):
#         autonomies = None 
#     elif(autonomies_choose == 100):
#         autonomies = 0                       
        
#     return autonomies        

# def generate_tv():
#     tv_choose = random.randint(1, 101)
#     tv = None
    
#     if(tv_choose <= 63):
#         tv = 1
#     elif(tv_choose <= 93):
#         tv = 2
#     elif(tv_choose <= 100):
#         tv = 0
#     else:
#         tv = None 
        
#     return tv    

# def generate_video_games():
#     video_games_choose = random.randint(1, 101)
#     video_games = None
    
#     if(video_games_choose <= 48):
#         video_games = 1
#     elif(video_games_choose <= 76):
#         video_games = 2
#     elif(video_games_choose <= 100):
#         video_games = 0   
#     else:
#         video_games = None 
        
#     return video_games    

# def generate_play_with_friends_online():
#     play_with_friends_online_choose = random.randint(1, 100)
#     play_with_friends_online = None
    
#     if(play_with_friends_online_choose <= 70):
#         play_with_friends_online = 0
#     elif(play_with_friends_online_choose <= 89):
#         play_with_friends_online = 1
#     elif(play_with_friends_online_choose <= 96):
#         play_with_friends_online = None 
#     elif(play_with_friends_online_choose <= 98):
#         play_with_friends_online = 2 
#     elif(play_with_friends_online_choose == 99):
#         play_with_friends_online = 7         
#     elif(play_with_friends_online_choose == 100):
#         play_with_friends_online = 6                               
        
#     return play_with_friends_online        

# def generate_social_networks():
#     social_networks_choose = random.randint(1, 101)
#     social_networks = None
    
#     if(social_networks_choose <= 74):
#         social_networks = 0
#     elif(social_networks_choose <= 93):
#         social_networks = 1
#     elif(social_networks_choose <= 98):
#         social_networks = 2   
#     elif(social_networks_choose <= 100):
#         social_networks = 7           
#     else:
#         social_networks = None 
        
#     return social_networks    
