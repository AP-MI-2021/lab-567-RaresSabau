from Domain.Librarie import to_str
from Logic.Operatiuni import aplicare_discount
from Logic.crud import add_carte, stergere_librarie

def print_menu():
    print ('''
    Meniu Principal
    1. Crud
    2. Aplicare discount
    3. Modificarea genului pentru un titlu dat.
    4. Determinarea prețului minim pentru fiecare gen
    5. Ordonarea vânzărilor crescător după preț
    6. Afișarea numărului de titluri distincte pentru fiecare gen
    7. Undo
    8. Afisare lista
    9. Stergere
    x. Iesire''')



def handle_add_carte_UI(librarie):
    id = input ("Introduceti id-ul: ")
    titlu = input("Introduceti titlul: ")
    gen = input("Introduceti genul: ")
    pret = float(input("Introduceti pretul: "))
    reducere = input ("Introduceti tipul de reducere (none, silver, gold): ")
    add_carte(librarie, id, titlu, gen, pret, reducere)
    print("Cartea a fost adaugata! ")


def handle_sterge_carte_UI(librarie):
    id = input("Introduceti id-ul cartii ce urmeaza sa fie stearsa ")
    print("Cartea cu id-ul respectiv a fost stearsa din lista! ")
    return stergere_librarie(id, librarie)


def handle_show(librarie):
        '''
        Afisare lista carti
        :param librarie: lista de carti
        :return:
        '''
        for carte in librarie:
            print(to_str(carte))


def run_undo_UI(librarie):
    pass


def run_console(librarie):
    '''

    :param librarie: lista de carti
    :return:
    '''
    while True:
        print_menu()
        cmd = input ("Comanda dvs: ")
        if cmd == '1':
            handle_add_carte_UI(librarie)
        elif cmd == '2':
            print("Lista a fost modificata! ")
            librarie = aplicare_discount(librarie)
        elif cmd == '3':
            run_modif_gen_UI(librarie)
        elif cmd == '4':
            run_pret_minim_UI(librarie)
        elif cmd == '5':
            run_ord_vanzari_UI(librarie)
        elif cmd == '6':
            run_nr_titluri_UI(librarie)
        elif cmd == '7':
            run_undo_UI(librarie)
        elif cmd =='8':
            print("Cartea cu id-ul dat a fost stearsa: ")
            handle_show(librarie)
        elif cmd == '9':
            librarie = handle_sterge_carte_UI(librarie)
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida")
