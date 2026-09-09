#include "sensores.hpp"
#include "relacoes.hpp"
#include "fontes.hpp"
#include "excecoes.hpp"
#include "identidade.hpp"
#include "colecoes.hpp"
#include "projeto.hpp"
#include <cstdlib>
#include <iostream>
#include <limits>
#include <type_traits>
#include <unordered_set>
void exigir(bool ok, const char* msg) {
    if (!ok) { std::cerr << "FALHA: " << msg << '\n'; std::exit(1); }
}
template<class E, class F> void rejeita(F f, const char* msg) {
    bool capturada = false;
    try { f(); } catch (const E&) { capturada = true; }
    exigir(capturada, msg);
}
void etapa07() {
    exigir(std::is_base_of_v<Sensor, SensorNivel> && std::is_base_of_v<Sensor, SensorTemperatura>, "especializacoes devem derivar de Sensor");
    exigir(!std::is_abstract_v<Sensor>, "base desta etapa ainda nao e abstrata");
    SensorNivel n{"LT-101"}; SensorTemperatura t{"TT-201"};
    exigir(n.tag() == "LT-101" && t.tag() == "TT-201", "inicialize a tag pela classe-base");
    exigir(n.unidade() == "%" && t.unidade() == "C", "preserve as unidades");
    for (double v : {0.0, 42.5, 100.0}) exigir(n.atualizar(v) && n.valor() == v, "nivel deve aceitar 0..100");
    for (double v : {-40.0, 15.0, 125.0}) exigir(t.atualizar(v) && t.valor() == v, "temperatura deve aceitar -40..125");
    for (double v : {-1.0, 101.0, std::numeric_limits<double>::infinity(), std::numeric_limits<double>::quiet_NaN()}) {
        exigir(!n.atualizar(v) && n.valor() == 100, "rejeicao deve preservar nivel, inclusive NaN");
        rejeita<std::invalid_argument>([v]{ SensorNivel x{"LT",v}; }, "construcao invalida de nivel deve falhar");
    }
    for (double v : {-41.0, 126.0, std::numeric_limits<double>::infinity(), std::numeric_limits<double>::quiet_NaN()}) {
        exigir(!t.atualizar(v) && t.valor() == 125, "rejeicao deve preservar temperatura");
        rejeita<std::invalid_argument>([v]{ SensorTemperatura x{"TT",v}; }, "construcao invalida de temperatura deve falhar");
    }
    rejeita<std::invalid_argument>([]{SensorNivel n{""};}, "tag vazia deve ser rejeitada na base");
    rejeita<std::invalid_argument>([]{SensorTemperatura t{""};}, "tag vazia deve ser rejeitada em toda especializacao");
}
void etapa09() {
    SensorNivel a{"A",10}, b{"B",70};
    { PainelFixo p(a), q(a);
      exigir(p.leitura()==10 && q.leitura()==10,"dois paineis devem consultar o mesmo sensor");
      a.atualizar(20);
      exigir(p.leitura()==20 && q.leitura()==20,"associacao nao deve copiar uma leitura antiga");
      p.conectar(b);
      exigir(p.leitura()==70 && q.leitura()==20,"troca de vinculo deve afetar apenas um painel");
    }
    exigir(a.atualizar(30) && b.valor()==70,"destruir painel nao remove sensores externos");
    Bancada bancada;
    exigir(bancada.sensor()==nullptr,"bancada admite vaga vazia");
    bancada.receber(a);
    exigir(bancada.sensor()==&a,"bancada deve agrupar o mesmo objeto");
    bancada.liberar();
    exigir(bancada.sensor()==nullptr && a.valor()==30,"liberar grupo nao destrói parte");
    exigir(consultarAgora(a)==30,"dependencia por parametro deve consultar valor atual");
}
class FonteTeste : public IFonteLeitura {
public:
    double leitura = 7;
    double valor() const override { return leitura; }
    std::string unidade() const override { return "%"; }
};
void etapa10() {
    exigir(std::is_abstract_v<IFonteLeitura>,"IFonteLeitura deve ser abstrata");
    SensorNivel n{"LT",30}; FonteNivel real(n); FonteConstante fixa(12,"%"); FonteTeste extra;
    exigir(lerFonte(real)==30 && real.unidade()=="%", "FonteNivel deve consultar sensor por associacao");
    exigir(lerFonte(fixa)==12 && fixa.unidade()=="%", "FonteConstante deve cumprir o mesmo contrato");
    n.atualizar(40); extra.leitura=91;
    exigir(lerFonte(real)==40 && lerFonte(extra)==91,"cliente deve aceitar nova implementacao sem selecionar tipo");
}
void etapa11() {
    FonteTeste fonte; int abertas=0;
    exigir(lerServico(fonte,true,true,abertas)==7 && abertas==0,"sucesso deve liberar sessao");
    rejeita<FalhaLeitura>([&]{lerServico(fonte,false,true,abertas);},"falha deve propagar ao chamador");
    exigir(abertas==0,"RAII deve liberar sessao ao propagar falha");
    rejeita<FalhaCalibracao>([&]{lerServico(fonte,true,false,abertas);},"calibracao deve lancar excecao especifica");
    exigir(abertas==0,"calibracao deve liberar sessao");
    auto r=executarCiclo(fonte,false,true,abertas);
    exigir(!r.sucesso && abertas==0,"fronteira deve capturar FalhaLeitura");
    r=executarCiclo(fonte,true,false,abertas);
    exigir(!r.sucesso && abertas==0,"captura da base deve aceitar falha especializada");
    r=executarCiclo(fonte,true,true,abertas);
    exigir(r.sucesso && r.valor==7 && abertas==0,"falha anterior nao impede ciclo seguinte");
    class FonteDefeito : public IFonteLeitura {
        double valor() const override { throw std::logic_error("defeito inesperado"); }
        std::string unidade() const override { return "%"; }
    } defeito;
    rejeita<std::logic_error>([&]{executarCiclo(defeito,true,true,abertas);},"nao ocultar falhas fora do contrato de recuperacao");
    exigir(abertas==0,"limpeza deve ocorrer tambem em defeito inesperado");
}
void etapa12() {
    IdSensor a{"LT-101"}, b{"LT-101"}, c{"LT-102"}; const IdSensor& alias=a;
    exigir(&alias==&a && &a!=&b,"identidade de objetos e distinta de igualdade");
    exigir(a==a && a==b && b==a && !(a==c),"igualdade deve comparar o identificador");
    exigir(a<c && !(a<b) && !(b<a),"ordenacao deve ser lexicografica e coerente com igualdade");
    exigir(HashId{}(a)==HashId{}(b),"objetos iguais precisam ter hash igual");
    std::unordered_set<IdSensor,HashId> ids{a,b,c};
    exigir(ids.size()==2 && ids.count(IdSensor{"LT-101"})==1,"conjunto deve reconhecer chave logicamente igual");
    rejeita<std::invalid_argument>([]{IdSensor id{""};},"identificador vazio deve falhar");
}
void etapa13() {
    Catalogo<Medicao> c; IdSensor a{"LT-101"}, b{"LT-102"};
    exigir(c.quantidade()==0 && c.buscar(a)==nullptr && !c.remover(a),"catalogo vazio deve ser seguro");
    exigir(c.inserir(a,Medicao{12,"%"}) && c.inserir(b,Medicao{20,"%"}),"inserir duas medicoes distintas");
    exigir(!c.inserir(IdSensor{"LT-101"},Medicao{99,"%"}),"chave duplicada deve ser rejeitada");
    exigir(c.quantidade()==2 && c.buscar(a) && c.buscar(a)->valor==12,"duplicata nao pode substituir valor");
    exigir(c.ids().size()==2 && c.ids().count(a)==1,"listar identificadores sem duplicatas");
    exigir(c.remover(a) && !c.remover(a) && c.quantidade()==1,"remocao deve informar ausencia");
    Catalogo<std::string> nomes;
    exigir(nomes.inserir(a,"bancada") && *nomes.buscar(a)=="bancada","mesmo generico deve aceitar outro tipo");
    std::vector<std::unique_ptr<IFonteLeitura>> fontes;
    exigir(somarPercentuais(fontes)==0,"colecao polimorfica vazia deve produzir zero");
    fontes.push_back(std::make_unique<FonteConstante>(12,"%"));
    exigir(somarPercentuais(fontes)==12,"uma fonte deve ser consultada");
    fontes.push_back(std::make_unique<FonteTeste>());
    exigir(somarPercentuais(fontes)==19,"duas implementacoes devem participar da iteracao");
}
void etapa14() {
    FonteTeste fonte; PoliticaAlarme politica(10); ControladorConsulta c(fonte,politica);
    fonte.leitura=10; exigir(!c.avaliar(),"fronteira exata nao deve alarmar");
    fonte.leitura=11; exigir(c.avaliar(),"controlador deve delegar para a politica");
    fonte.leitura=9; exigir(!c.avaliar(),"controlador deve consultar leitura atual a cada chamada");
}
int main(int argc,char** argv) {
    exigir(argc==2,"informe uma etapa");
    const std::string e=argv[1];
    if(e=="07") etapa07(); else if(e=="09") etapa09(); else if(e=="10") etapa10();
    else if(e=="11") etapa11(); else if(e=="12") etapa12(); else if(e=="13") etapa13();
    else if(e=="14") etapa14(); else exigir(false,"etapa desconhecida");
    std::cout << "OK C++ etapa " << e << '\n';
}
