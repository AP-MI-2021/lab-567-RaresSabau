from Domain.Librarie import get_id, creeaza_librarie, get_gen, get_titlu, get_pret, get_reducere
from Logic.crud import add_librarie, get_by_id, modifica_librarie, stergere_librarie


def discount(lista):
    """
    da un discount de 5% respectiv 10% pentru toate cartiile ce au tipul de reducere silver respectiv gold
    :param lista: lista de carti
    :return: lista de carti cu preturile modificate
    h
    """
    listaNoua = []
    for librarie in lista:
        if get_reducere(librarie) == "silver":
            librarieNoua = creeaza_librarie(
                get_id(librarie),
                get_titlu(librarie),
                get_gen(librarie),
                get_pret(librarie) - (0.05 * get_pret(librarie)),
                get_reducere(librarie)
            )
            listaNoua.append(librarieNoua)
        elif get_reducere(librarie) == "gold":
            librarieNoua = creeaza_librarie(
                get_id(librarie),
                get_titlu(librarie),
                get_gen(librarie),
                get_pret(librarie) - (0.1 * get_pret(librarie)),
                get_reducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua


def command_line_console(comand,lista):
    list_comand = comand.split(",")
    for x in range(len(list_comand)):
        if list_comand[x] == "add":
            try:
                if get_by_id(list_comand[x+1], lista) is not None:
                 raise ValueError("Id-ul "+list_comand[x+1]+" exista deja")
                lista=add_librarie(list_comand[x+1], list_comand[x+2], list_comand[x+3], list_comand[x+4], list_comand[x+5], lista)
            except ValueError as ve:
                print("Error: {}".format(ve))
        if list_comand[x] == "show all":
            from UI.Consola import show_all
            show_all(lista)
        if list_comand[x] == "delete":
            lista=stergere_librarie(list_comand[x+1], lista)
        if list_comand[x] == "edit":
            try:
                if get_by_id(list_comand[x+1], lista) is None:
                    raise ValueError("Nu exista o librarie cu id-ul "+list_comand[x+1])
                lista=modifica_librarie(list_comand[x+1], list_comand[x+2], list_comand[x+3], list_comand[x+4], list_comand[x+5], lista)
            except ValueError as ve:
                print("Error: {}" .format(ve))
    return lista


def modificare_gen(nume_initial, nume_schimbat, lista):
    """
        modifica genul unei carti care are titlul dat
        :param nume_initial:
        :param noulGen:
        :param lista:
        :return:
        """
    lista_noua = []
    for librarie in lista:
        if get_titlu(librarie) == nume_initial:
            librarie_noua = creeaza_librarie(
                get_id(librarie),
                get_titlu(librarie),
                nume_schimbat,
                get_pret(librarie),
                get_reducere(librarie)
            )
            lista_noua.append(librarie_noua)
        else:
            lista_noua.append(librarie)
    return lista_noua


def pret_minim(lista):
    rezultat = {}
    for librarie in lista:
        gen = get_gen(librarie)
        pret = get_pret(librarie)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat


def nr_titluri(lista):
    rezultat = {}
    aux = []
    for librarie in lista:
        gen = get_gen(librarie)
        ok = 0
        titlu = get_titlu(librarie)
        for p in aux:
            if titlu == p:
                ok = 1
        aux.append(titlu)
        if gen in rezultat and ok == 0:
            rezultat[gen] = rezultat[gen] + 1
        else:
            rezultat[gen] = 1
    return rezultat


def ordonare_pret(lista):
    return sorted(lista, key=lambda librarie: get_pret(librarie))
