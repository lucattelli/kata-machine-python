from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, Tuple, TypeVar

from kata_machine_python.linked_list import T, LinkedList


T = TypeVar('T')

@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None

class SinglyLinkedList(LinkedList, Generic[T]):
    length: int
    __head: Optional[Node[T]]

    def __init__(self):
        self.length = 0
        self.__head = None

    def prepend(self, item: T) -> None:
        next_node = self.__head
        self.__head = Node(value=item, next=next_node)
        self.length += 1

    def insert_at(self, item: T, idx: int) -> None:
        if idx == self.length:
            self.append(item)
        elif idx < self.length:
            node, _ = self.__get_by_idx(idx)
            if node:
                new_node = Node(value=item, next=node.next)
                node.next = new_node
                self.length += 1

    def append(self, item: T) -> None:
        new_node = Node(value=item)
        if not self.__head:
            self.__head = new_node
        else:
            node = self.__head
            while node.next:
                node = node.next
            node.next = new_node
        self.length += 1

    def remove(self, item: T) -> Optional[T]:
        _, idx = self.__get_by_item(item)
        return self.remove_at(idx)

    def get(self, idx: int) -> Optional[T]:
        node, _ = self.__get_by_idx(idx)
        return node.value if node else None

    def remove_at(self, idx: int) -> Optional[T]:
        if not self.__head:
            return

        if idx == 0:
            match = self.__head.value
            self.__head = self.__head.next
            self.length -= 1
            return match

        previous_node, _ = self.__get_by_idx(idx - 1)
        if previous_node and previous_node.next:
            match = previous_node.next.value
            previous_node.next = previous_node.next.next
            self.length -= 1
            return match

    def __get_by_idx(self, idx: int) -> Tuple[Optional[Node[T]], int]:
        node = None
        if idx >= 0 and self.length > idx and self.__head:
            node = self.__head
            for _ in range(idx):
                if node:
                    node = node.next
        return node, idx if node else -1

    def __get_by_item(self, item: T) -> Tuple[Optional[Node[T]], int]:
        match = None
        match_idx = -1

        if self.__head and self.__head.value == item:
            match = self.__head
            match_idx = 0
            return match, match_idx

        if self.__head:
            node = self.__head
            idx = 0
            while node and match is None:
                idx += 1
                if node.next and node.next.value == item:
                    match = node.next
                    match_idx = idx
                else:
                    node = node.next

        return match, match_idx

