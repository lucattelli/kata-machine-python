from kata_machine_python.doubly_linked_list import DoublyLinkedList
from test.util.list_tests import run_list_tests


def test_doubly_linked_list():
    list = DoublyLinkedList()
    run_list_tests(list)
