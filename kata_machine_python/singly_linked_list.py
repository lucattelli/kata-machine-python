from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class LinkedList(ABC, Generic[T]):
    length: int

    @abstractmethod
    def prepend(self, item: T) -> None:
        pass

    @abstractmethod
    def insert_at(self, item: T, idx: int) -> None:
        pass

    @abstractmethod
    def append(self, item: T) -> None:
        pass

    @abstractmethod
    def remove(self, item: T) -> Optional[T]:
        pass

    @abstractmethod
    def get(self, idx: int) -> Optional[T]:
        pass

    @abstractmethod
    def remove_at(self, idx: int) -> Optional[T]:
        pass



class SinglyLinkedList(LinkedList, Generic[T]):
    def __init__(self):
        pass

    def prepend(self, item: T) -> None:
        pass

    def insert_at(self, item: T, idx: int) -> None:
        pass

    def append(self, item: T) -> None:
        pass

    def remove(self, item: T) -> Optional[T]:
        pass

    def get(self, idx: int) -> Optional[T]:
        pass

    def remove_at(self, idx: int) -> Optional[T]:
        pass

