from Logic.Operatiuni import aplicare_discount
from Logic.crud import add_carte, get_by_id
from Domain.Librarie import  get_id, get_gen, get_titlu, get_pret, get_reducere

def test_aplicare_discount():
        librarie = []
        add_carte(librarie, '26c', 'Ion', 'Realism', 100, 'silver')
        add_carte(librarie, '27c', 'Ion', 'Realism', 200, 'gold')
        add_carte(librarie, '28c', 'Ion', 'Realism', 50, 'none')

        librarie = aplicare_discount(librarie)

        assert get_pret(get_by_id("26c", librarie)) == 95
        assert get_pret(get_by_id("27c", librarie)) == 180
        assert get_pret(get_by_id("28c", librarie)) == 50