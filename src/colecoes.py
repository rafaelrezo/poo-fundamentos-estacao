from dataclasses import dataclass
from typing import Generic, TypeVar
from identidade import IdSensor

T = TypeVar("T")

@dataclass(frozen=True)
class Medicao:
    valor: float
    unidade: str

class Catalogo(Generic[T]):
    def __init__(self):
        self._itens: dict[IdSensor, T] = {}
    def inserir(self, id: IdSensor, item: T) -> bool:
        return False  # TODO 13
    def buscar(self, id: IdSensor) -> T | None:
        return None  # TODO 13
    def remover(self, id: IdSensor) -> bool:
        return False  # TODO 13
    def quantidade(self):
        return len(self._itens)
    def ids(self):
        return set()  # TODO 13

def somar_percentuais(fontes):
    return 0  # TODO 13
