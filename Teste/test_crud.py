from Logic.crud import add_carte, get_by_id, stergere_librarie, modificare_librarie
from Domain.Librarie import  get_id, get_gen, get_titlu, get_pret, get_reducere

def test_add_carte():

    librarie = []
    add_carte(librarie, '26c', 'Ion', 'Realism', 30, 'silver')

    assert len(librarie) == 1
    assert  get_id(librarie[0]) == '26c'
    assert  get_pret(librarie[0]) == 30
    assert  get_gen(librarie[0]) == 'Realism'
    assert get_titlu(librarie[0]) == 'Ion'
    assert get_reducere(librarie[0]) == 'silver'

def test_get_by_id():
    librarie = []
    add_carte(librarie, "1", "Plumb", "Poezii", 17, "gold")
    add_carte(librarie, "2", "Moara", "Roman", 58, "silver")

    assert get_by_id("1", librarie) is not None
    assert get_by_id("5", librarie) is None
    assert get_by_id("2", librarie) == librarie[1]
    assert get_by_id("1", librarie) == librarie[0]

def test_stergere_librarie():
    librarie = []
    add_carte(librarie, "1", "Plumb", "Poezii", 17, "gold")
    add_carte(librarie, "2", "Moara", "Roman", 58, "silver")

    lista = stergere_librarie("1", librarie)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

def test_modificare_librarie():
    librarie = []
    add_carte(librarie, "1", "Plumb", "Poezii", 17, "gold")
    add_carte(librarie, "2", "Moara", "Roman", 58, "silver")

    librarie = modificare_librarie(librarie, "1", "Ion", "Realism", 25, "gold")

    librarie_modificata = get_by_id("1", lista)
    assert get_id(librarie_modificata) == "1"
    assert get_titlu(librarie_modificata) == "Ion"
    assert get_gen(librarie_modificata) == "Roman"
    assert get_pret(librarie_modificata) == 25
    assert get_reducere(librarie_modificata) == "gold"

    librarie_nemodificata = get_by_id("2", lista)
    assert get_id(librarie_nemodificata) == "2"
    assert get_titlu(librarie_nemodificata) == "Moara"
    assert get_gen(librarie_nemodificata) == "Roman"
    assert get_pret(librarie_nemodificata) == 58
    assert get_reducere(librarie_nemodificata) == "silver"