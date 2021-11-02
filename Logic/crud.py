from Domain.Librarie import create_librarie

def add_carte(librarie, id, titlu, gen, pret):
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
    carte = create_librarie (id, titlu, gen, pret)
    librarie.append(carte)
