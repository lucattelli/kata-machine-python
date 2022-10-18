from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

@dataclass
class Node(Generic[T]):
    value: T
    prev: Optional[Node[T]] = None

class Stack(Generic[T]):
    length: int
    __head: Optional[Node[T]]

    def __init__(self):
        self.__head = None
        self.length = 0

    def push(self, item: T) -> None:
        node = Node(value=item, prev=self.__head)
        self.length += 1
        self.__head = node

    def pop(self) -> Optional[T]:
        if not self.__head:
            return

        head = self.__head
        self.length -= 1
        self.__head = head.prev

        return head.value



    def peek(self) -> Optional[T]:
        if self.__head:
            return self.__head.value

