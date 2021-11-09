from Domain.Librarie import get_id, get_titlu, get_gen, get_reducere, get_pret
from Logic.crud import add_librarie, get_by_id, stergere_librarie, modifica_librarie

def test_get_by_id():
    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is None
    assert get_by_id("4", lista) is None

    lista2 = []
    lista2 = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista2)
    lista2 = add_librarie("3", "Ion", "Realism", 20, "silver", lista2)
    assert get_by_id("1", lista2) is not None
    assert get_by_id("2", lista2) is None
    assert get_by_id("3", lista2) is not None

def test_add_librarie():
    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)

    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_titlu(get_by_id("1", lista)) == "Baltagul"
    assert get_gen(get_by_id("1", lista)) == "Traditionalism"
    assert get_pret(get_by_id("1", lista)) == 15
    assert get_reducere(get_by_id("1", lista)) == "none"


    lista = []
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)

    assert len(lista) == 1
    assert get_id(get_by_id("2", lista)) == "2"
    assert get_titlu(get_by_id("2", lista)) == "Ion"
    assert get_gen(get_by_id("2", lista)) == "Realism"
    assert get_pret(get_by_id("2", lista)) == 20
    assert get_reducere(get_by_id("2", lista)) == "silver"

def test_sterge_librarie():
    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = stergere_librarie("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    try:
        lista = stergere_librarie("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert get_by_id("2", lista) is not None
    except Exception:
        assert False


    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = add_librarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = stergere_librarie("2", lista)

    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is not None

def test_modifica_librarie():
    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = modifica_librarie("1", "Enigma Otiliei", "Realism", 5, "gold", lista)

    libraria_modificata = get_by_id("1", lista)
    assert get_id(libraria_modificata) == "1"
    assert get_titlu(libraria_modificata) == "Enigma Otiliei"
    assert get_gen(libraria_modificata) == "Realism"
    assert get_pret(libraria_modificata) == 5
    assert get_reducere(libraria_modificata) == "gold"

    librarie_nemodificata = get_by_id("2", lista)
    assert get_id(librarie_nemodificata) == "2"
    assert get_titlu(librarie_nemodificata) == "Ion"
    assert get_gen(librarie_nemodificata) == "Realism"
    assert get_pret(librarie_nemodificata) == 20
    assert get_reducere(librarie_nemodificata) == "silver"


    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    try:
        lista = modifica_librarie("3", "Enigma Otiliei", "Realism", 5, "gold", lista)
    except ValueError:
        librarie_nemodificata = get_by_id("1", lista)
        assert get_id(librarie_nemodificata) == "1"
        assert get_titlu(librarie_nemodificata) == "Baltagul"
        assert get_gen(librarie_nemodificata) == "Traditionalism"
        assert get_pret(librarie_nemodificata) == 15
        assert get_reducere(librarie_nemodificata) == "none"
    except Exception:
        assert False

    lista = []
    lista = add_librarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = add_librarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = modifica_librarie("2", "Enigma Otiliei", "Realism", 5, "gold", lista)

    librarie_nemodificata = get_by_id("1", lista)
    assert get_id(librarie_nemodificata) == "1"
    assert get_titlu(librarie_nemodificata) == "Baltagul"
    assert get_gen(librarie_nemodificata) == "Traditionalism"
    assert get_pret(librarie_nemodificata) == 15
    assert get_reducere(librarie_nemodificata) == "none"

    libraria_modificata = get_by_id("2", lista)
    assert get_id(libraria_modificata) == "2"
    assert get_titlu(libraria_modificata) == "Enigma Otiliei"
    assert get_gen(libraria_modificata) == "Realism"
    assert get_pret(libraria_modificata) == 5
    assert get_reducere(libraria_modificata) == "gold"