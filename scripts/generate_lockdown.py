import random
import pandas as pd
from datetime import date

AGES_REMAINING = [1,2,9,10,11,12,13,14,15,16,17,18,19,20]

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
        'mother/father': generate_mother_father(),
        'child age': generate_child_age(),
        'child sex': generate_child_sex(), 
        'ASD diagnosis': generate_asd_diagnosis(),
        'language competences': generate_language_competences(),
        'cognitive functioning': generate_cognitive_functioning(),
        'language and communication': generate_language_and_communication(),
        'emotional regulation': generate_emotional_regulation(),
        'social interaction': generate_social_interaction(),
        'stereotypes': generate_stereotypes(),
        'behavioral problems': generate_behavioral_problems(),
        'restricted interests': generate_restricted_interests(),
        'autonomies': generate_autonomies(),
        'tv': generate_tv(),
        'video-games': generate_video_games(),
        'play with frinds online': generate_play_with_friends_online(),
        'social networks': generate_social_networks()
    }

def generate_file_csv(data_list, file_date):
    path = f'generated-data\\{file_date}-lockdown-generate.csv'
    df = pd.DataFrame(data_list)
    df.to_csv(path, index=False)
    
def generate_mother_father():
    mother_father_choose = random.randint(1, 101)
    mother_father = None
    
    if(mother_father_choose <= 91):
        mother_father = 1
    elif(mother_father_choose <= 100):
        mother_father = 2
    else:
        mother_father = None 
        
    return mother_father

def generate_child_age():
    age_part = random.randint(1, 4) 
    child_age = None
    if(age_part <= 2):
        age_choose = random.randint(1, 51)
        if(age_choose <= 20):
            child_age = 5
        elif(age_choose <= 35):
            child_age = 4
        elif(age_choose <= 50):
            child_age = 6   
        else:
            child_age = None         
    elif(age_part == 3):
        age_choose = random.randint(1, 26)
        if(age_choose <= 11):
            child_age = 7
        elif(age_choose <= 18):
            child_age = 8
        elif(age_choose <= 25):
            child_age = 3 
        else:
            child_age = None                       
    else:
        child_age = random.choice(AGES_REMAINING)    
    
    return child_age

def generate_child_sex():
    child_sex_choose = random.randint(1, 101)
    child_sex = None
    
    if(child_sex_choose <= 86):
        child_sex = 0
    elif(child_sex_choose <= 100):
        child_sex = 1
    else:
        child_sex = None 
        
    return child_sex

def generate_asd_diagnosis():
    asd_diagnosis_choose = random.randint(1, 101)
    asd_diagnosis = None
    
    if(asd_diagnosis_choose <= 45):
        asd_diagnosis = 2
    elif(asd_diagnosis_choose <= 73):
        asd_diagnosis = 1
    elif(asd_diagnosis_choose <= 100):
        asd_diagnosis = 3       
    else:
        asd_diagnosis = None 
        
    return asd_diagnosis    

def generate_language_competences():
    language_competences_choose = random.randint(1, 101)
    language_competences = None
    
    if(language_competences_choose <= 38):
        language_competences = 2
    elif(language_competences_choose <= 61):
        language_competences = 0
    elif(language_competences_choose <= 81):
        language_competences = 3  
    elif(language_competences_choose <= 100):
        language_competences = 1               
    else:
        language_competences = None 
        
    return language_competences        

def generate_cognitive_functioning():
    cognitive_functioning_choose = random.randint(1, 101)
    cognitive_functioning = None 
    
    if(cognitive_functioning_choose <= 47):
        cognitive_functioning = 2
    elif(cognitive_functioning_choose <= 80):
        cognitive_functioning = 3
    elif(cognitive_functioning_choose <= 100):
        cognitive_functioning = 1   
    else:
        cognitive_functioning = None 
        
    return cognitive_functioning    

def generate_language_and_communication():
    language_and_communication_choose = random.randint(1, 100)
    language_and_communication = None
    
    if(language_and_communication_choose <= 62):
        language_and_communication = 3
    elif(language_and_communication_choose <= 86):
        language_and_communication = 2
    elif(language_and_communication_choose <= 99):
        language_and_communication = 1  
    elif(language_and_communication_choose == 100):
        language_and_communication = None               
        
    return language_and_communication 

def generate_emotional_regulation():
    emotional_regulation_choose = random.randint(1, 100)
    emotional_regulation = None
    
    if(emotional_regulation_choose <= 40):
        emotional_regulation = 3
    elif(emotional_regulation_choose <= 71):
        emotional_regulation = 2
    elif(emotional_regulation_choose <= 98):
        emotional_regulation = 1  
    elif(emotional_regulation_choose <= 100):
        emotional_regulation = None               
        
    return emotional_regulation        

def generate_social_interaction():
    social_interaction_choose = random.randint(1, 100)
    social_interaction = None
    
    if(social_interaction_choose <= 36):
        social_interaction = 3
    elif(social_interaction_choose <= 68):
        social_interaction = 1
    elif(social_interaction_choose <= 97):
        social_interaction = 2 
    elif(social_interaction_choose <= 100):
        social_interaction = None               
        
    return social_interaction        

def generate_stereotypes():
    stereotypes_choose = random.randint(1, 100)
    stereotypes = None
    
    if(stereotypes_choose <= 42):
        stereotypes = 2
    elif(stereotypes_choose <= 76):
        stereotypes = 1
    elif(stereotypes_choose <= 98):
        stereotypes = 3
    elif(stereotypes_choose <= 100):
        stereotypes = None               
        
    return stereotypes        

def generate_behavioral_problems():
    behavioral_problems_choose = random.randint(1, 100)
    behavioral_problems = None
    
    if(behavioral_problems_choose <= 39):
        behavioral_problems = 2
    elif(behavioral_problems_choose <= 72):
        behavioral_problems = 1
    elif(behavioral_problems_choose <= 98):
        behavioral_problems = 3
    elif(behavioral_problems_choose <= 100):
        behavioral_problems = None               
        
    return behavioral_problems        

def generate_restricted_interests():
    restricted_interests_choose = random.randint(1, 100)
    restricted_interests = None
    
    if(restricted_interests_choose <= 34):
        restricted_interests = 1
    elif(restricted_interests_choose <= 67):
        restricted_interests = 2
    elif(restricted_interests_choose <= 98):
        restricted_interests = 3 
    elif(restricted_interests_choose <= 100):
        restricted_interests = None               
        
    return restricted_interests      

def generate_autonomies():
    autonomies_choose = random.randint(1, 100)
    autonomies = None
    
    if(autonomies_choose <= 52):
        autonomies = 3
    elif(autonomies_choose <= 84):
        autonomies = 2
    elif(autonomies_choose <= 96):
        autonomies = 1 
    elif(autonomies_choose <= 99):
        autonomies = None 
    elif(autonomies_choose == 100):
        autonomies = 0                       
        
    return autonomies        

def generate_tv():
    tv_choose = random.randint(1, 101)
    tv = None
    
    if(tv_choose <= 63):
        tv = 1
    elif(tv_choose <= 93):
        tv = 2
    elif(tv_choose <= 100):
        tv = 0
    else:
        tv = None 
        
    return tv    

def generate_video_games():
    video_games_choose = random.randint(1, 101)
    video_games = None
    
    if(video_games_choose <= 48):
        video_games = 1
    elif(video_games_choose <= 76):
        video_games = 2
    elif(video_games_choose <= 100):
        video_games = 0   
    else:
        video_games = None 
        
    return video_games    

def generate_play_with_friends_online():
    play_with_friends_online_choose = random.randint(1, 100)
    play_with_friends_online = None
    
    if(play_with_friends_online_choose <= 70):
        play_with_friends_online = 0
    elif(play_with_friends_online_choose <= 89):
        play_with_friends_online = 1
    elif(play_with_friends_online_choose <= 96):
        play_with_friends_online = None 
    elif(play_with_friends_online_choose <= 98):
        play_with_friends_online = 2 
    elif(play_with_friends_online_choose == 99):
        play_with_friends_online = 7         
    elif(play_with_friends_online_choose == 100):
        play_with_friends_online = 6                               
        
    return play_with_friends_online        

def generate_social_networks():
    social_networks_choose = random.randint(1, 101)
    social_networks = None
    
    if(social_networks_choose <= 74):
        social_networks = 0
    elif(social_networks_choose <= 93):
        social_networks = 1
    elif(social_networks_choose <= 98):
        social_networks = 2   
    elif(social_networks_choose <= 100):
        social_networks = 7           
    else:
        social_networks = None 
        
    return social_networks    
