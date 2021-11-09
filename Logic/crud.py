from Domain.Librarie import create_librarie, get_id

def add_carte(librarie, id, titlu, gen, pret, reducere):
    '''
    Adaugarea cartilor in lista librariei
    :param librarie: lista de carti
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: string
    :return:
    '''
    carte = create_librarie(id, titlu, gen, pret, reducere)
    librarie.append(carte)

def get_by_id(id, librarie):
    """
    Gaseste vanzarea cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de vanzari
    :return: returneaza vanzarea cu id-ul dat sau none daca nu exista
    """
    for carte in librarie:
        if get_id(carte) == id:
            return carte

def stergere_librarie(id, librarie):
    """
    sterge o carte din lista dupa un id dat
    :param id: id-ul cartii care se sterge , int
    :param librarie: lista din care se sterge , lista
    :return: lista fara cartea cu id-ul "id"
    """
    if get_by_id(id, librarie) is None:
        raise ValueError("Nu exista o carte cu id-ul dat")
    return [carte for carte in librarie if get_id(carte) != id]

def modificare_librarie(librarie, id, titlu, gen, pret, reducere):
    """
    modifica o carte aleasa
    :param id:id-ul cartii care urmeaza sa fie modificat, str
    :param titlu:noul titlu , str
    :param gen: noul gen , str
    :param pret:noul pret , float
    :param reducere: noul tip de reducere , string (gold,none,silver)
    :param librarie: lista cu cartea schimbata
    :return:lista noua
    """
    lista_noua = []
    for carte in librarie:
        if get_id(carte) == id:
            vanzare_noua = add_carte(id, titlu, gen, pret, reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(carte)
    return lista_noua
