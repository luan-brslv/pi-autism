import argparse
def parse_arguments() -> dict:
    parser = argparse.ArgumentParser(description='')

    parser.add_argument(
        '-s','--samples', 
        action = 'store', 
        dest = 'samples', 
        type=int,
        required = False,
        help = 'O número de amostras.'
    )
    
    parser.add_argument(
        '-g','--generate', 
        required = True,
        help = 'Script de geração que será executado.'
    )
    
    parsed_args = vars(parser.parse_args())

    if len(parsed_args) > 0:
        return parsed_args
    else:
        raise ValueError('Argumentos inválidos!')

if __name__ == "__main__":
    args = parse_arguments()
    script = args['generate'].lower()
    if script == 'lockdown':
        from scripts.generate_lockdown import execute
        execute(args["samples"]) 
    elif script == 'italian':
        from scripts.generate_italian import execute
        execute(args["samples"]) 
    elif script == 'old-data':
        from scripts.generate_files import execute
        execute(args["samples"])   
    else:
        raise ValueError('Argumento inválido!')            

