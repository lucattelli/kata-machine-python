from kata_machine_python.singly_linked_list import SinglyLinkedList
from test.util.list_tests import run_list_tests


def test_singly_linked_list():
    list = SinglyLinkedList()
    run_list_tests(list)
