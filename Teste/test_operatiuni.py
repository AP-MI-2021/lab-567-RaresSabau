from Domain.Librarie import get_pret, get_gen
from Logic.crud import get_by_id, add_librarie
from Logic.Operatiuni import discount, modificare_gen, command_line_console


def test_discount():
    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = add_librarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = discount(lista)

    assert get_pret(get_by_id("1", lista)) == 15
    assert get_pret(get_by_id("2", lista)) == 19
    assert get_pret(get_by_id("3", lista)) == 22.5

def test_modificare_gen():
    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = add_librarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = modificare_gen("Realism", "Interbelic", lista)

    assert get_gen(get_by_id("1", lista)) == "Traditionalism"
    assert get_gen(get_by_id("2", lista)) == "Interbelic"
    assert get_gen(get_by_id("3", lista)) == "Interbelic"

def test_command_line():
    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = add_librarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)
    lista=command_line_console("add,4,O scrisoare pierduta,Drama,40,none", lista)
    assert len(lista) == 4
    lista = command_line_console("edit,3,O scrisoare pierduta,Drama,40,none", lista)
    assert get_gen(get_by_id("3",lista)) == "Drama"