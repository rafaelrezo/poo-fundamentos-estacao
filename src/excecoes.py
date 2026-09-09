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
    # TODO 11: lancamento e finally para liberar a sessao.
    return fonte.valor()

def ler_servico(fonte, disponivel, calibrado, sessao):
    return adquirir(fonte, disponivel, calibrado, sessao)

def executar_ciclo(fonte, disponivel, calibrado, sessao):
    # TODO 11: capturar FalhaLeitura; retornar (False, 0) nesse caso.
    return True, ler_servico(fonte, disponivel, calibrado, sessao)
