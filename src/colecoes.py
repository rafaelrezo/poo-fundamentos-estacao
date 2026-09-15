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
        return False  # TODO B
    def buscar(self, id: IdSensor) -> T | None:
        return None  # TODO B
    def remover(self, id: IdSensor) -> bool:
        return False  # TODO B
    def quantidade(self):
        return len(self._itens)
    def ids(self):
        return set(self._itens)

def somar_percentuais(fontes):
    return sum(fonte.valor() for fonte in fontes)
