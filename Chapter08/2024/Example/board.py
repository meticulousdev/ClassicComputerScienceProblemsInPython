from __future__ import annotations
from typing import NewType, List
from abc import ABC, abstractmethod

Move = NewType('Move', int)


class Piece:
    @property
    def opposite(self) -> Piece:
        raise NotImplementedError("서브클래스로 구현해야 합니다.")


class Board(ABC):
    @property
    @abstractmethod
    def turn(self) -> Piece:
        ...
    
    @abstractmethod
    def move(self, location: Move) -> Board:
        ...
    
    @property
    @abstractmethod
    def is_win(self) -> bool:
        ...

    @property
    def is_draw(self) -> bool:
        return (not self.is_win) and (len(self.legal_moves) == 0)

    @abstractmethod
    def evaluate(self, player: Piece) -> float:
        ...
