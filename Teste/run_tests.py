from Teste.test_crud import test_get_by_id, test_add_librarie, test_modifica_librarie, test_sterge_librarie
from Teste.test_operatiuni import test_discount, test_command_line


def run_all_tests():
    test_add_librarie()
    test_discount()
    test_get_by_id()
    test_modifica_librarie()
    test_command_line()
    test_sterge_librarie()