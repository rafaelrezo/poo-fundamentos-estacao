class FalhaLeitura(Exception):
    pass

class FalhaCalibracao(FalhaLeitura):
    pass

class Sessao:
    def __init__(self):
        self.abertas = 0
    def abrir(self):
        self.abertas += 1
    def fechar(self):
        self.abertas -= 1

def adquirir(fonte, disponivel, calibrado, sessao):
    sessao.abrir()
    try:
        if not disponivel:
            raise FalhaLeitura("fonte indisponivel")
        # TODO A: rejeitar a falta de calibracao com o tipo especifico.
        return fonte.valor()
    finally:
        sessao.fechar()

def ler_servico(fonte, disponivel, calibrado, sessao):
    return adquirir(fonte, disponivel, calibrado, sessao)

def executar_ciclo(fonte, disponivel, calibrado, sessao):
    try:
        return True, ler_servico(fonte, disponivel, calibrado, sessao)
    except FalhaLeitura:
        return False, 0
