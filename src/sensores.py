from math import isfinite

class Sensor:
    def __init__(self, tag: str):
        if not tag:
            raise ValueError("tag vazia")
        self._tag = tag
    @property
    def tag(self):
        return self._tag

class SensorNivel(Sensor):
    def __init__(self, tag: str, valor: float = 50):
        super().__init__("PENDENTE")  # TODO 07: inicializar a base com tag.
        if not isfinite(valor) or not 0 <= valor <= 100:
            raise ValueError("nivel fora da faixa")
        self._valor = valor
    def valor(self):
        return self._valor
    def unidade(self):
        return "%"
    def atualizar(self, valor):
        return False  # TODO 07

class SensorTemperatura(Sensor):
    def __init__(self, tag: str, valor: float = 25):
        super().__init__("PENDENTE")  # TODO 07
        if not isfinite(valor) or not -40 <= valor <= 125:
            raise ValueError("temperatura fora da faixa")
        self._valor = valor
    def valor(self):
        return self._valor
    def unidade(self):
        return "C"
    def atualizar(self, valor):
        return False  # TODO 07
