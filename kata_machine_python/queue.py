from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

@dataclass
class Node(Generic[T]):
    value: T
    next: Optional[Node[T]] = None

class Queue(Generic[T]):
    length: int
    __head: Optional[Node[T]]
    __tail: Optional[Node[T]]

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.length = 0

    def enqueue(self, item: T) -> None:
        node = Node(value=item)
        self.length += 1
        if not self.__tail:
            self.__tail = self.__head = node
            return

        self.__tail.next = node
        self.__tail = node

    def deque(self) -> Optional[T]:
        if not self.__head:
            return None

        self.length -= 1

        head = self.__head
        self.__head = self.__head.next
        head.next = None

        if self.length == 0:
            self.__tail = None

        return head.value

    def peek(self) -> Optional[T]:
        if self.__head:
            return self.__head.value


