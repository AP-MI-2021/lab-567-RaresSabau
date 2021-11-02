from Domain.Librarie import to_str

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
    x. Iesire''')

def print_menu_crud():
    print('''
    
    Meniu Crud
    1. Adaugare
    2. Stergere
    3. Modificare Vanzare
    4. Afisare lista carti
    5. Inapoi la Meniul Principal
    
    ''')

def run_crud_UI(librarie):

    def handle_add_carte_UI(librarie):
        pass

    def handle_show(librarie):
        '''
        Afisare lista carti
        :param librarie: lista de carti
        :return:
        '''
        for carte in librarie:
            to_str(prajitura)


    while True:
        print_menu_crud()
        cmd = input ("Comanda dvs: ")
        if cmd == '1':
            handle_add_carte_UI(librarie)
        elif cmd == '2':
            pass
        elif cmd =='3':
            pass
        elif cmd == '4':
            handle_show(librarie)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida")


def run_aplicare_discount_UI(librarie):
    pass


def run_modif_gen_UI(librarie):
    pass


def run_pret_minim_UI(librarie):
    pass


def run_ord_vanzari_UI(librarie):
    pass


def run_nr_titluri_UI(librarie):
    pass


def run_undo_UI(librarie):
    pass


def run_console (librarie):
    '''

    :param librarie: lista de carti
    :return:
    '''
    while True:
        print_menu()
        cmd = input ("Comanda dvs: ")
        if cmd == '1':
            run_crud_UI(librarie)
        elif cmd == '2':
            run_aplicare_discount_UI(librarie)
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
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida")
