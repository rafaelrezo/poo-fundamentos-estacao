class PainelFixo:
    def __init__(self, sensor):
        self._sensor = sensor
    def leitura(self):
        return 0  # TODO A: consultar o associado (incremento guiado).
    def conectar(self, sensor):
        self._sensor = sensor

class Bancada:
    def __init__(self):
        self.sensor = None
    def receber(self, sensor):
        self.sensor = sensor
    def liberar(self):
        self.sensor = None

def consultar_agora(sensor):
    return sensor.valor()
