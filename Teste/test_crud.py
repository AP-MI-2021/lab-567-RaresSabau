from Logic.crud import add_carte
from Domain.Librarie import  get_id, get_gen, get_titlu, get_pret
def test_add_carte():
    librarie = []
    add_carte(librarie, '26c', 'Ion', 'Realism', 30)
    assert len(librarie) == 1
    assert  get_id(librarie[0]) == '26c'
    assert  get_pret(librarie[0]) == 30
    assert  get_gen(librarie[0]) == 'Realism'
    assert get_titlu(librarie[0]) == 'Ion'