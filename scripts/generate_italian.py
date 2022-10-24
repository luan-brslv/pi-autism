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
            'genere M/F': generate_column1(prob_al),
            'diagnosi (inserire anche il livello di supporto e la compromissione intellettiva e del linguaggio)': generate_column2(prob_al),
            'istruzione padre/madre': generate_column3(prob_al), 
            'Lavoro padre / madre': generate_column4(prob_al),
            'età cronologica in anni e mesi': generate_column5(prob_al),
            'età cronologica in mesi': generate_column6(prob_al),
            'età di sviluppo ': generate_column7(prob_al),
            'test usato per l\'età di sviluppo (PEP-3 ; Brunet Lézine; griffith; altri)': generate_column8(prob_al),
            'QI': generate_column9(prob_al),
            'test usato per il QI': generate_column10(prob_al),
            'ados*': generate_column11(prob_al),
            'cars 2*': generate_column12(prob_al),
            'CASD*': generate_column13(prob_al),
            'BAMBI  (max punteggio 90; cut-off 34)': generate_column14(prob_al),
            'Food selectivity (max punteggio 20) items 10-11-13-15': generate_column15(prob_al),
            'Disruptive mealtime behav (max 25) item 1-3-5-6-7': generate_column16(prob_al),
            'food refusal (max 15) items 2-4-8': generate_column17(prob_al),
            'mealtime rigidity (max 15) items 9-16-18': generate_column18(prob_al),
            'SEQ: totale': generate_column19(prob_al),
            'SEQ: totale HY': generate_column20(prob_al),
            'SEQ: sub-totale HY-S': generate_column21(prob_al),
            'SEQ: sub-totale HY-NS': generate_column22(prob_al),
            'SEQ: totale HO': generate_column23(prob_al),
            'SEQ: sub-totale HO-S': generate_column24(prob_al),
            'SEQ: sub-totale HO-NS': generate_column25(prob_al),
            'CEBQ totale': generate_column26(prob_al),
            'CEBQ: risposta al cibo': generate_column27(prob_al),
            'CEBQ: sovra-alimentaz. Emozionale': generate_column28(prob_al),
            'CEBQ: gradimento del cibo': generate_column29(prob_al),
            'CEBQ: desiderio di bere ': generate_column30(prob_al),
            'CEBQ: risposta sazietà': generate_column31(prob_al),
            'CEBQ: lentezza nell\'alimentarsi': generate_column32(prob_al),
            'CEBQ: sotto-alimentazione emozionale': generate_column33(prob_al),
            'CEBQ: selettività verso il cibo': generate_column34(prob_al),
            'SSP (short sensory profile): TOTALE': generate_column35(prob_al),
            'SSP: sensibilità tattile': generate_column36(prob_al),
            'SSP: sensibilità olfattiva-gustativa': generate_column37(prob_al),
            'SSP: sensibilità motoria': generate_column38(prob_al),
            'SSP: ipo-risposta /ricerca di sensazioni': generate_column39(prob_al),
            'SSP: filtro uditivo': generate_column40(prob_al),
            'SSP: bassa energia/debolezza': generate_column41(prob_al),
            'SSP: sensibilità visiva-uditiva': generate_column42(prob_al)
        }
    elif(prob_al == True):
        return {        
            'CODICE ': identificador,
            'genere M/F': generate_column1(prob_al),
            'diagnosi (inserire anche il livello di supporto e la compromissione intellettiva e del linguaggio)': generate_column2(prob_al),
            'istruzione padre/madre': generate_column3(prob_al), 
            'Lavoro padre / madre': generate_column4(prob_al),
            'età cronologica in anni e mesi': generate_column5(prob_al),
            'età cronologica in mesi': generate_column6(prob_al),
            'età di sviluppo (in mesi)** ': generate_column7(prob_al),
            'test usato per l\'età di sviluppo (PEP-3 ; Brunet Lézine; griffith; altri)': generate_column8(prob_al),
            'QI**': generate_column9(prob_al),
            'test usato per il QI': generate_column10(prob_al),
            'ados*': generate_column11(prob_al),
            'cars 2*': generate_column12(prob_al),
            'CASD*': generate_column13(prob_al),
            'BAMBI  (max punteggio 90; cut-off 34)': generate_column14(prob_al),
            'Food selectivity (max punteggio 20) items 10-11-13-15': generate_column15(prob_al),
            'Disruptive mealtime behav (max 25) item 1-3-5-6-7': generate_column16(prob_al),
            'food refusal (max 15) items 2-4-8': generate_column17(prob_al),
            'mealtime rigidity (max 15) items 9-16-18': generate_column18(prob_al),
            'SEQ: totale': generate_column19(prob_al),
            'SEQ: totale HY': generate_column20(prob_al),
            'SEQ: sub-totale HY-S': generate_column21(prob_al),
            'SEQ: sub-totale HY-NS': generate_column22(prob_al),
            'SEQ: totale HO': generate_column23(prob_al),
            'SEQ: sub-totale HO-S': generate_column24(prob_al),
            'SEQ: sub-totale HO-NS': generate_column25(prob_al),
            'CEBQ totale': generate_column26(prob_al),
            'CEBQ: risposta al cibo': generate_column27(prob_al),
            'CEBQ: sovra-alimentaz. Emozionale': generate_column28(prob_al),
            'CEBQ: gradimento del cibo': generate_column29(prob_al),
            'CEBQ: desiderio di bere ': generate_column30(prob_al),
            'CEBQ: risposta sazietà': generate_column31(prob_al),
            'CEBQ: lentezza nell\'alimentarsi': generate_column32(prob_al),
            'CEBQ: sotto-alimentazione emozionale': generate_column33(prob_al),
            'CEBQ: selettività verso il cibo': generate_column34(prob_al),
            'SSP (short sensory profile): TOTALE': generate_column35(prob_al),
            'SSP: sensibilità tattile': generate_column36(prob_al),
            'SSP: sensibilità olfattiva-gustativa': generate_column37(prob_al),
            'SSP: sensibilità motoria': generate_column38(prob_al),
            'SSP: ipo-risposta /ricerca di sensazioni': generate_column39(prob_al),
            'SSP: filtro uditivo': generate_column40(prob_al),
            'SSP: bassa energia/debolezza': generate_column41(prob_al),
            'SSP: sensibilità visiva-uditiva': generate_column42(prob_al)        
        }
        
def generate_file_csv(data_list, file_date, prob_al):
    if(prob_al == True):
        path = f'generated-data\\{file_date}-asd_con_probl_alimentari-generate.csv'    
    elif(prob_al == False):
        path = f'generated-data\\{file_date}-asd_no_probl_alimentari-generate.csv'
        
    df = pd.DataFrame(data_list)
    df.to_csv(path, sep=';', index=False)
    
def generate_column1(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['genere M/F'].tolist())    
    else:
        column_data = random.choice(excel_con['genere M/F'].tolist())    
        
    return column_data

def generate_column2(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['diagnosi (inserire anche il livello di supporto e la compromissione intellettiva e del linguaggio)'].tolist())    
    else:
        column_data = random.choice(excel_con['diagnosi (inserire anche il livello di supporto e la compromissione intellettiva e del linguaggio)'].tolist())    
        
    return column_data

def generate_column3(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['istruzione padre/madre'].tolist())    
    else:
        column_data = random.choice(excel_con['istruzione padre/madre'].tolist())    
        
    return column_data

def generate_column4(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['Lavoro padre / madre'].tolist())    
    else:
        column_data = random.choice(excel_con['Lavoro padre / madre'].tolist())    
        
    return column_data

def generate_column5(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['età cronologica in anni e mesi'].tolist())    
    else:
        column_data = random.choice(excel_con['età cronologica in anni e mesi'].tolist())    
        
    return column_data

def generate_column6(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['età cronologica in mesi'].tolist())    
    else:
        column_data = random.choice(excel_con['età cronologica in mesi'].tolist())    
        
    return column_data

def generate_column7(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['età di sviluppo '].tolist())    
    else:
        column_data = random.choice(excel_con['età di sviluppo (in mesi)**'].tolist())    
        
    return column_data

def generate_column8(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['test usato per l\'età di sviluppo (PEP-3 ; Brunet Lézine; griffith; altri)'].tolist())    
    else:
        column_data = random.choice(excel_con['test usato per l\'età di sviluppo (PEP-3 ; Brunet Lézine; griffith; altri)'].tolist())    
        
    return column_data

def generate_column9(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['QI'].tolist())    
    else:
        column_data = random.choice(excel_con['QI**'].tolist())    
        
    return column_data

def generate_column10(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['test usato per il QI'].tolist())    
    else:
        column_data = random.choice(excel_con['test usato per il QI'].tolist())    
        
    return column_data

def generate_column11(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['età cronologica in anni e mesi'].tolist())    
    else:
        column_data = random.choice(excel_con['età cronologica in anni e mesi'].tolist())    
        
    return column_data

def generate_column12(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['ados*'].tolist())    
    else:
        column_data = random.choice(excel_con['ados*'].tolist())    
        
    return column_data

def generate_column13(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['cars 2*'].tolist())    
    else:
        column_data = random.choice(excel_con['cars 2*'].tolist())    
        
    return column_data

def generate_column14(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CASD*'].tolist())    
    else:
        column_data = random.choice(excel_con['CASD*'].tolist())    
        
    return column_data

def generate_column15(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['BAMBI  (max punteggio 90; cut-off 34)'].tolist())    
    else:
        column_data = random.choice(excel_con['BAMBI  (max punteggio 90; cut-off 34)'].tolist())    
        
    return column_data

def generate_column16(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['Food selectivity (max punteggio 20) items 10-11-13-15'].tolist())    
    else:
        column_data = random.choice(excel_con['Food selectivity (max punteggio 20) items 10-11-13-15'].tolist())    
        
    return column_data

def generate_column17(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['Disruptive mealtime behav (max 25) item 1-3-5-6-7'].tolist())    
    else:
        column_data = random.choice(excel_con['Disruptive mealtime behav (max 25) item 1-3-5-6-7'].tolist())    
        
    return column_data

def generate_column18(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['food refusal (max 15) items 2-4-8'].tolist())    
    else:
        column_data = random.choice(excel_con['food refusal (max 15) items 2-4-8'].tolist())    
        
    return column_data

def generate_column19(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['mealtime rigidity (max 15) items 9-16-18'].tolist())    
    else:
        column_data = random.choice(excel_con['mealtime rigidity (max 15) items 9-16-18'].tolist())    
        
    return column_data

def generate_column20(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SEQ: totale'].tolist())    
    else:
        column_data = random.choice(excel_con['SEQ: totale'].tolist())    
        
    return column_data

def generate_column21(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SEQ: totale HY'].tolist())    
    else:
        column_data = random.choice(excel_con['SEQ: totale HY'].tolist())    
        
    return column_data

def generate_column22(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SEQ: sub-totale HY-S'].tolist())    
    else:
        column_data = random.choice(excel_con['SEQ: sub-totale HY-S'].tolist())    
        
    return column_data

def generate_column23(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SEQ: sub-totale HY-NS'].tolist())    
    else:
        column_data = random.choice(excel_con['SEQ: sub-totale HY-NS'].tolist())    
        
    return column_data

def generate_column24(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SEQ: sub-totale HO-S'].tolist())    
    else:
        column_data = random.choice(excel_con['SEQ: sub-totale HO-S'].tolist())    
        
    return column_data

def generate_column25(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SEQ: sub-totale HO-NS'].tolist())    
    else:
        column_data = random.choice(excel_con['SEQ: sub-totale HO-NS'].tolist())    
        
    return column_data

def generate_column26(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ totale'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ totale'].tolist())    
        
    return column_data

def generate_column27(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: risposta al cibo'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: risposta al cibo'].tolist())    
        
    return column_data

def generate_column28(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: sovra-alimentaz. Emozionale'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: sovra-alimentaz. Emozionale'].tolist())    
        
    return column_data

def generate_column29(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: gradimento del cibo'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: gradimento del cibo'].tolist())    
        
    return column_data

def generate_column30(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: desiderio di bere '].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: desiderio di bere '].tolist())    
        
    return column_data

def generate_column31(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: risposta sazietà'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: risposta sazietà'].tolist())    
        
    return column_data

def generate_column32(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: lentezza nell\'alimentarsi'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: lentezza nell\'alimentarsi'].tolist())    
        
    return column_data

def generate_column33(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: sotto-alimentazione emozionale'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: sotto-alimentazione emozionale'].tolist())    
        
    return column_data

def generate_column34(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['CEBQ: selettività verso il cibo'].tolist())    
    else:
        column_data = random.choice(excel_con['CEBQ: selettività verso il cibo'].tolist())    
        
    return column_data

def generate_column35(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP (short sensory profile): TOTALE'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP (short sensory profile): TOTALE'].tolist())    
        
    return column_data

def generate_column36(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP: sensibilità tattile'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP: sensibilità tattile'].tolist())    
        
    return column_data

def generate_column37(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP: sensibilità olfattiva-gustativa'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP: sensibilità olfattiva-gustativa'].tolist())    
        
    return column_data

def generate_column38(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP: sensibilità motoria'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP: sensibilità motoria'].tolist())    
        
    return column_data

def generate_column39(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP: ipo-risposta /ricerca di sensazioni'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP: ipo-risposta /ricerca di sensazioni'].tolist())    
        
    return column_data

def generate_column40(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP: filtro uditivo'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP: filtro uditivo'].tolist())    
        
    return column_data

def generate_column41(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP: bassa energia/debolezza'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP: bassa energia/debolezza'].tolist())    
        
    return column_data

def generate_column42(prob_al):
    if(prob_al == False):
        column_data = random.choice(excel_no['SSP: sensibilità visiva-uditiva'].tolist())    
    else:
        column_data = random.choice(excel_con['SSP: sensibilità visiva-uditiva'].tolist())    
        
    return column_data