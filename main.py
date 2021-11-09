from Logic.crud import add_librarie
from UI.Consola import run_menu
from Teste.run_tests import run_all_tests

def main():
    lista = []
    lista = add_librarie("1", "Moara cu noroc", "Psihologic", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 30, "silver", lista)
    lista = add_librarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)
    run_menu(lista)

if __name__ == '__main__':
    main()