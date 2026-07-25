from abc import ABC, abstractmethod


class BaseSkill(ABC):

    @abstractmethod
    def can_handle(self, texto: str) -> bool:
        pass

    @abstractmethod
    def execute(self, texto: str) -> bool:
        pass