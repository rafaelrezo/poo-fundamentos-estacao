class PoliticaAlarme:
    def __init__(self, limite):
        self._limite = limite
    def aciona(self, valor):
        return valor > self._limite

class ControladorConsulta:
    def __init__(self, fonte, politica):
        self._fonte, self._politica = fonte, politica
    def avaliar(self):
        return False  # TODO 14: delegar para politica e fonte.
