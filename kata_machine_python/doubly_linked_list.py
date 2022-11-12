from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from kata_machine_python.linked_list import T, LinkedList


T = TypeVar('T')

@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None
    prior: Optional[Node[T]] = None

class DoublyLinkedList(LinkedList, Generic[T]):
    length: int
    __head: Optional[Node[T]]

    def __init__(self):
        self.length = 0
        self.__head = None

    def __debug(self, message: str) -> None:
        items = []
        item = self.__head
        while item:
            v = item.value
            n = item.next.value if item.next else None
            p = item.prior.value if item.prior else None
            items.append({"v": v, "n": n, "p": p})
            item = item.next

        print({
            "message": message,
            "length": self.length,
            "items": items,
            })

    def prepend(self, item: T) -> None:
        if not self.__head:
            self.append(item)
        else:
            node = self.__head
            self.__head = Node(value=item, next=node)
            node.prior = self.__head
            self.length += 1

    def insert_at(self, item: T, idx: int) -> None:
        pass

    def append(self, item: T) -> None:
        new_node = Node(value=item)
        if not self.__head:
            self.__head = new_node
            self.length += 1
        else:
            node = self.__get_node_by_idx()
            if node:
                node.next = new_node
                new_node.prior = node
                self.length += 1

    def __get_node_by_idx(self, idx: int = -1) -> Optional[Node[T]]:
        if idx == -1:
            position = self.length - 1
        else:
            position = idx

        node = self.__head
        for _ in range(position):
            if node:
                node = node.next
        return node

    def __get_node_by_item(self, item: T) -> Optional[Node[T]]:
        found = None
        node = self.__head
        for _ in range(self.length):
            if node and node.value == item:
                found = node
                break
            elif node:
                node = node.next
        return found

    def get(self, idx: int) -> Optional[T]:
        node = self.__get_node_by_idx(idx)
        return node.value if node else None

    def __remove_head(self) -> Optional[T]:
        if self.__head:
            node = self.__head
            self.__head = self.__head.next
            if self.__head:
                self.__head.prior = None
            self.length -= 1
            return node.value

    def __remove_node(self, node: Node[T]) -> Optional[T]:
        if node.prior:
            node.prior.next = node.next
        if node.next:
            node.next.prior = node.prior
        self.length -= 1

    def remove(self, item: T) -> Optional[T]:
        self.__debug("before remove")
        if not self.__head:
            return

        if self.__head.value == item:
            return self.__remove_head()

        node = self.__get_node_by_item(item)
        if node:
            self.__remove_node(node)
        self.__debug("after remove")
        return node.value if node else None


    def remove_at(self, idx: int) -> Optional[T]:
        if not self.__head:
            return

        if idx == 0:
            return self.__remove_head()

        node = self.__get_node_by_idx(idx)
        if node:
            self.__remove_node(node)
        return node.value if node else None

