class PainelFixo:
    def __init__(self, sensor):
        self._sensor = sensor
    def leitura(self):
        return 0  # TODO 09
    def conectar(self, sensor):
        pass  # TODO 09

class Bancada:
    def __init__(self):
        self.sensor = None
    def receber(self, sensor):
        pass  # TODO 09
    def liberar(self):
        self.sensor = None

def consultar_agora(sensor):
    return sensor.valor()
