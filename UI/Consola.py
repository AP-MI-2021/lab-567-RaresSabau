from Domain.Librarie import to_str
from Logic.crud import add_librarie, stergere_librarie, modifica_librarie
from Logic.Operatiuni import discount, modificare_gen, command_line_console, nr_titluri, ordonare_pret, pret_minim


def printMenu():
    print('''
    1. Adaugare carte
    2. Stergere carte
    3. Modificare carte
    4. Aplicare discount
    5. Modificare gen dupa titlu
    6. Cel mai mic pret pentru fiecare gen
    7. Ordonarea vanzarilor crescator dupa pret
    8. Numarul de titluri pentru fiecare gen
    u. Undo
    r. Redo
    a. Afisare carti
    c.Command console
    x. Iesire
    ''')

def handle_add_librarie(lista, undo_list, redo_list):
    try:
        id = input("Introduceti id-ul: ")
        titlu = input("Introduceti titlul: ")
        gen = input("Introduceti genul: ")
        pret = float(input('Introduceti pretul: '))
        reducere = input("Introduceti tipul de reducere: ")
        librarie_adaugata=add_librarie(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return librarie_adaugata
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def handle_stergere_librarie(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul cartii de sters: ")
        rezultat = stergere_librarie(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def handle_modifica_librarie(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul cartii de modificat: ")
        titlu = input("Dati noul titlu: ")
        gen = input("Dati noul gen: ")
        pret = float(input('Dati noul pret: '))
        reducere =input("Dati noul tip de reducere: ")
        librarie_modificata= modifica_librarie(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return librarie_modificata
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def handle_discount(lista, undo_list, redo_list):
    rezultat = discount(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def handle_pret_minim(lista):
    rezultat = pret_minim(lista)
    for gen in rezultat:
        print("Genul {} are cel mai mic pret {}".format(gen, rezultat[gen]))

def handle_ordonare_pret(lista, undo_list, redo_list):
    rezultat = ordonare_pret(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def handle_nr_titluri(lista):
    rezultat = nr_titluri(lista)
    for gen in rezultat:
        print("Genul {} are {} titluri".format(gen, rezultat[gen]))

def handle_modificare_gen(lista, undo_list, redo_list):
    nume_original=input("Dati titlul operei al carei gen se va modifica: ")
    nume_schimbat=input("Dati genul cu care se va inlocui: ")
    rezultat = modificare_gen(nume_original, nume_schimbat, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def show_all(lista):
    for librarie in lista:
        print(to_str(librarie))


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = handle_add_librarie(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = handle_stergere_librarie(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = handle_modifica_librarie(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = handle_discount(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = handle_modificare_gen(lista, undo_list, redo_list)
        elif optiune == "6":
            handle_pret_minim(lista)
        elif optiune == "7":
            lista = handle_ordonare_pret(lista, undo_list, redo_list)
        elif optiune == "8":
            handle_nr_titluri(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "c":
            UI_command_console()
            command=input("Dati comenzile despartite prin , :")
            lista=command_line_console(command,lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
def UI_command_console():
    print("Ati intrat in consola de tip command line")
    print("Comenzile suportate la momentul actual sunt : add , delete , show all , edit")