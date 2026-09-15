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
        return self.valor == outro.valor
    def __lt__(self, outro):
        if not isinstance(outro, IdSensor):
            return NotImplemented
        return self.valor < outro.valor
    def __hash__(self):
        return hash(self.valor)
