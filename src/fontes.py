from abc import ABC, abstractmethod


class IFonteLeitura(ABC):
    @abstractmethod
    def valor(self):
        raise NotImplementedError

    @abstractmethod
    def unidade(self):
        raise NotImplementedError


class FonteNivel(IFonteLeitura):
    def __init__(self, sensor):
        self._sensor = sensor

    def valor(self):
        return self._sensor.valor()

    def unidade(self):
        return self._sensor.unidade()


class FonteConstante(IFonteLeitura):
    def __init__(self, valor, unidade):
        self._valor, self._unidade = valor, unidade

    def valor(self):
        return self._valor

    def unidade(self):
        return self._unidade


def ler_fonte(fonte: IFonteLeitura):
    return fonte.valor()
