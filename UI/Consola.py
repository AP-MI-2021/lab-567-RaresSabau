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

def handle_add_librarie(lista):
    try:
        id = input("Introduceti id-ul: ")
        titlu = input("Introduceti titlul: ")
        gen = input("Introduceti genul: ")
        pret = float(input('Introduceti pretul: '))
        reducere = input("Introduceti tipul de reducere: ")
        librarie_adaugata=add_librarie(id, titlu, gen, pret, reducere, lista)
        return librarie_adaugata
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def handle_stergere_librarie(lista):
    try:
        id = input("Introduceti id-ul cartii pe care doriti sa o stergeti: ")
        rezultat = stergere_librarie(id, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def handle_modificare_librarie(lista):
    try:
        id = input("Introduceti id-ul cartii de modificat: ")
        titlu = input("Introduceti noul titlu: ")
        gen = input("Introduceti noul gen: ")
        pret = float(input('Introduceti noul pret: '))
        reducere =input("Introduceti noul tip de reducere: ")
        librarie_modificata= modifica_librarie(id, titlu, gen, pret, reducere, lista)
        return librarie_modificata
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def handle_discount(lista):
    rezultat = discount(lista)
    return rezultat


def handle_pret_minim(lista):
    rezultat = pret_minim(lista)
    for gen in rezultat:
        print("Genul {} are cel mai mic pret {}".format(gen, rezultat[gen]))

def handle_ordonare_pret(lista):
    rezultat = ordonare_pret(lista)
    return rezultat

def handle_nr_titluri(lista):
    rezultat = nr_titluri(lista)
    for gen in rezultat:
        print("Genul {} are {} titluri".format(gen, rezultat[gen]))
def handle_modificare_gen(lista,):
    numeOriginal=input("Dati titlul operei al carei gen se va modifica: ")
    numeSchimbat=input("Dati genul cu care se va inlocui: ")
    rezultat = modificare_gen(numeOriginal, numeSchimbat, lista)
    return rezultat
def show_all(lista):
    for librarie in lista:
        print(to_str(librarie))


def run_menu(lista):
    while True:
        printMenu()
        optiune = input("Introduceti optiunea: ")

        if optiune == "1":
            lista = handle_add_librarie(lista)
        elif optiune == "2":
            lista = handle_stergere_librarie(lista)
        elif optiune == "3":
            lista = handle_modificare_librarie(lista)
        elif optiune == "4":
            lista = handle_discount(lista)
        elif optiune == "5":
            lista = handle_modificare_gen(lista)
        elif optiune == "6":
            handle_pret_minim(lista)
        elif optiune == "7":
            lista = handle_ordonare_pret(lista)
        elif optiune == "8":
            handle_nr_titluri(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "c":
            command_console()
            command=input("Introduceti comenzile despartite prin ,(de exemplu: add,id,titlu,gen,pret,reducere):")
            lista=command_line_console(command, lista)
        elif optiune == "x":
            break
        else:
            print("Optiune invalida! ")
def command_console():
    print("Ati intrat in consola de tip command line")
    print("Comenzile suportate la momentul actual sunt : add , show all , edit")