def create_librarie(id, titlu_carte, gen_carte, pret, tip_reducere_client):
    '''

    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string (none, silver, gold)
    :return: Dict
    '''
    return {
    "id" : id,
    "titlu" : titlu_carte,
    "gen" : gen_carte,
    "pret" : pret,
    "reducere" : tip_reducere_client,
    }

def get_id (librarie):
    '''

    :param librarie: Dict
    :return: id - string
    '''
    return librarie['id']

def get_titlu (librarie):
    '''

    :param librarie: Dict
    :return: titlu - string
    '''
    return librarie['titlu']

def get_gen(librarie):
    '''

    :param librarie: Dict
    :return: gen - string
    '''
    return librarie['gen']

def get_pret(librarie):
    '''

    :param librarie: Dict
    :return: pret - float
    '''
    return librarie['pret']

def get_reducere(librarie):
    '''

    :param librarie: Dict
    :return: reducere - string
    '''
    return librarie['reducere']

def to_str(librarie):
    return f'id = {get_id(librarie)}, titlu = {get_titlu(librarie)}, gen = {get_gen(librarie)}' \
           f' pret = {get_pret(librarie)}, reducere = {get_reducere(librarie)}'

