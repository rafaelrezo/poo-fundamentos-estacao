import inspect
import sys
from sensores import Sensor, SensorNivel, SensorTemperatura
from relacoes import PainelFixo, Bancada, consultar_agora
from fontes import IFonteLeitura, FonteNivel, FonteConstante, ler_fonte
from excecoes import *
from identidade import IdSensor
from colecoes import Catalogo, Medicao, somar_percentuais
from projeto import PoliticaAlarme, ControladorConsulta

def exigir(ok, msg):
    if not ok:
        raise AssertionError(msg)

def rejeita(tipo, acao):
    try:
        acao()
    except tipo:
        return
    raise AssertionError(f"esperava {tipo.__name__}")

class FonteTeste(IFonteLeitura):
    leitura = 7
    def valor(self): return self.leitura
    def unidade(self): return "%"

def etapa07():
    exigir(issubclass(SensorNivel, Sensor) and issubclass(SensorTemperatura, Sensor), "especializar Sensor")
    for cls, tag, minimo, maximo, unidade in [(SensorNivel,"LT",0,100,"%"),(SensorTemperatura,"TT",-40,125,"C")]:
        s=cls(tag)
        exigir(s.tag==tag and s.unidade()==unidade,"inicializar tag pela base e preservar unidade")
        for v in (minimo,20,maximo):
            exigir(s.atualizar(v) and s.valor()==v,"aceitar leitura na faixa")
        for v in (minimo-1,maximo+1,float("nan"),float("inf")):
            exigir(not s.atualizar(v) and s.valor()==maximo,"rejeicao preserva estado")
            rejeita(ValueError,lambda: cls(tag,v))
        rejeita(ValueError,lambda: cls(""))

def etapa09():
    a,b=SensorNivel("A",10),SensorNivel("B",70)
    p,q=PainelFixo(a),PainelFixo(a)
    exigir(p.leitura()==q.leitura()==10,"consultar sensor associado")
    a.atualizar(20)
    exigir(p.leitura()==q.leitura()==20,"associacao nao copia leitura")
    p.conectar(b)
    exigir(p.leitura()==70 and q.leitura()==20,"trocar apenas o vinculo solicitado")
    del p,q
    exigir(a.atualizar(30) and b.valor()==70,"sensores externos continuam existindo")
    grupo=Bancada()
    exigir(grupo.sensor is None,"vaga vazia permitida")
    grupo.receber(a)
    exigir(grupo.sensor is a,"grupo referencia o mesmo sensor")
    grupo.liberar()
    exigir(grupo.sensor is None and consultar_agora(a)==30,"liberar agrupamento preserva sensor")

def etapa10():
    exigir(inspect.isabstract(IFonteLeitura),"IFonteLeitura deve ser abstrata")
    rejeita(TypeError,IFonteLeitura)
    n=SensorNivel("LT",30)
    real,fixa,extra=FonteNivel(n),FonteConstante(12,"%"),FonteTeste()
    exigir(ler_fonte(real)==30 and real.unidade()=="%","adaptar o sensor existente")
    exigir(ler_fonte(fixa)==12 and fixa.unidade()=="%","implementar fonte alternativa")
    n.atualizar(40);extra.leitura=91
    exigir(ler_fonte(real)==40 and ler_fonte(extra)==91,"cliente aceita implementacao desconhecida")

def etapa11():
    fonte=FonteTeste();sessao=Sessao()
    exigir(ler_servico(fonte,True,True,sessao)==7 and sessao.abertas==0,"liberar apos sucesso")
    rejeita(FalhaLeitura,lambda:ler_servico(fonte,False,True,sessao))
    exigir(sessao.abertas==0,"finally libera ao propagar erro")
    rejeita(FalhaCalibracao,lambda:ler_servico(fonte,True,False,sessao))
    exigir(sessao.abertas==0,"liberar apos falha especifica")
    try:
        ler_servico(fonte,False,False,sessao)
    except FalhaCalibracao:
        raise AssertionError("indisponibilidade deve ter prioridade sobre calibracao")
    except FalhaLeitura:
        pass
    else:
        raise AssertionError("duas falhas nao podem produzir leitura")
    exigir(sessao.abertas==0,"duas falhas devem liberar sessao")
    sensor=SensorNivel("LT",10)
    real,painel=FonteNivel(sensor),PainelFixo(sensor)
    sensor.atualizar(20)
    exigir(executar_ciclo(real,True,True,sessao)==(True,painel.leitura())
           and painel.leitura()==20,"painel e aquisicao observam o mesmo sensor")
    exigir(executar_ciclo(fonte,False,True,sessao)==(False,0),"capturar falha na fronteira")
    exigir(executar_ciclo(fonte,True,False,sessao)==(False,0),"captura da base inclui derivada")
    exigir(executar_ciclo(fonte,True,True,sessao)==(True,7) and sessao.abertas==0,"recuperar ciclo seguinte")
    class Defeito(FonteTeste):
        def valor(self): raise RuntimeError("defeito inesperado")
    rejeita(RuntimeError,lambda:executar_ciclo(Defeito(),True,True,sessao))
    exigir(sessao.abertas==0,"limpeza tambem no erro inesperado")

def etapa12():
    a,b,c=IdSensor("LT-101"),IdSensor("LT-101"),IdSensor("LT-102")
    alias=a
    exigir(alias is a and a is not b,"identidade nao e igualdade")
    exigir(a==a and a==b and b==a and a!=c,"comparar identificador")
    exigir(a<c and not a<b and not b<a,"ordenacao coerente")
    exigir(a.__eq__("LT-101") is NotImplemented,"comparacao de tipo nao suportado")
    exigir(hash(a)==hash(b) and len({a,b,c})==2,"igualdade e hash devem cooperar")
    rejeita(AttributeError,lambda:setattr(a,"valor","OUTRO"))
    rejeita(ValueError,lambda:IdSensor(""))

def etapa13():
    c=Catalogo[Medicao]();a,b=IdSensor("LT-101"),IdSensor("LT-102")
    exigir(c.quantidade()==0 and c.buscar(a) is None and not c.remover(a),"vazio seguro")
    exigir(c.inserir(a,Medicao(12,"%")) and c.inserir(b,Medicao(20,"%")),"inserir objetos")
    exigir(not c.inserir(IdSensor("LT-101"),Medicao(99,"%")),"rejeitar chave duplicada")
    exigir(c.quantidade()==2 and c.buscar(a).valor==12,"preservar medicao ao rejeitar duplicata")
    exigir(c.ids()=={a,b},"conjunto de chaves")
    exigir(c.remover(a) and not c.remover(a) and c.quantidade()==1,"remover e detectar ausencia")
    sensor=SensorNivel("LT-externo",12)
    registros=Catalogo[Medicao]()
    registros.inserir(a,Medicao(sensor.valor(),"%"))
    sensor.atualizar(20)
    exigir(registros.buscar(a).valor==12,"registro e fotografia da leitura")
    exigir(registros.remover(a) and sensor.valor()==20,"remover registro preserva sensor externo")
    nomes=Catalogo[str]()
    exigir(nomes.inserir(a,"bancada") and nomes.buscar(a)=="bancada","mesmo generico com outro tipo")
    fontes=[]
    exigir(somar_percentuais(fontes)==0,"iterar vazio")
    fontes.append(FonteConstante(12,"%"))
    exigir(somar_percentuais(fontes)==12,"iterar uma fonte")
    fontes.append(FonteTeste())
    exigir(somar_percentuais(fontes)==19,"iterar fontes diferentes")

def etapa14():
    fonte=FonteTeste();c=ControladorConsulta(fonte,PoliticaAlarme(10))
    for v,esperado in [(10,False),(11,True),(9,False)]:
        fonte.leitura=v
        exigir(c.avaliar()==esperado,"consulta e politica devem colaborar a cada chamada")

if __name__=="__main__":
    etapa=sys.argv[1]
    globals()["etapa"+etapa]()
    print("OK Python etapa",etapa)
