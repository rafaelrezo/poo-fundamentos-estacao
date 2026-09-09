from dataclasses import dataclass

@dataclass(frozen=True, eq=False)
class IdSensor:
    valor: str
    def __post_init__(self):
        if not self.valor:
            raise ValueError("identificador vazio")
    def __eq__(self, outro):
        if not isinstance(outro, IdSensor):
            return NotImplemented
        return False  # TODO 12: igualdade logica.
    def __lt__(self, outro):
        if not isinstance(outro, IdSensor):
            return NotImplemented
        return False  # TODO 12: ordem lexicografica.
    def __hash__(self):
        return hash(self.valor)
