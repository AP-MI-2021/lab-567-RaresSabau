def creeaza_librarie(id, titlu, gen, pret, reducere):
    """
    creeaza o lista de vanzari de carti (librarie)
    :param id:int
    :param titlu:string
    :param gen:string
    :param pret:float
    :param reducere:silver,    gold,   none
    :return:o lista de vanzari
    """
    list=[]
    list.append(id)
    list.append(titlu)
    list.append(gen)
    list.append(pret)
    list.append(reducere)
    return list



def get_id(librarie):
    return librarie[0]

def get_titlu(librarie):
    return librarie[1]

def get_gen(librarie):
    return librarie[2]

def get_pret(librarie):
    return librarie[3]

def get_reducere(librarie):
    return librarie[4]

def to_str(librarie):
    """
    conversteste un dictionar/o lista la string
    :param librarie: lista
    :return: string
    """
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Reducere: {}".format(
        get_id(librarie),
        get_titlu(librarie),
        get_gen(librarie),
        get_pret(librarie),
        get_reducere(librarie),
    )