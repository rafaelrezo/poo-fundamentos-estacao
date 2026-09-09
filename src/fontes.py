from abc import ABC, abstractmethod

class IFonteLeitura(ABC):
    # TODO 10: declarar como abstratas as operacoes exigidas.
    def valor(self):
        return 0
    def unidade(self):
        return "PENDENTE"

class FonteNivel(IFonteLeitura):
    def __init__(self, sensor):
        self._sensor = sensor
    def valor(self):
        return 0  # TODO 10
    def unidade(self):
        return "PENDENTE"  # TODO 10

class FonteConstante(IFonteLeitura):
    def __init__(self, valor, unidade):
        self._valor, self._unidade = valor, unidade
    def valor(self):
        return 0  # TODO 10
    def unidade(self):
        return "PENDENTE"  # TODO 10

def ler_fonte(fonte: IFonteLeitura):
    return 0  # TODO 10
