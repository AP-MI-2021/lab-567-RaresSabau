from Teste.test_crud import test_add_carte, test_get_by_id, test_stergere_librarie, test_modificare_librarie
from Teste.test_operatiuni import test_aplicare_discount

def run_tests():
    test_add_carte()
    test_aplicare_discount()
    test_get_by_id()
    test_stergere_librarie()
    test_modificare_librarie()

