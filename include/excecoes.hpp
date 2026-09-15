#pragma once
#include "fontes.hpp"
class FalhaLeitura : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
};
class FalhaCalibracao : public FalhaLeitura {
public:
    using FalhaLeitura::FalhaLeitura;
};
class Sessao {
    int& abertas_;
public:
    explicit Sessao(int& abertas) : abertas_(abertas) { ++abertas_; }
    ~Sessao() { --abertas_; }
    Sessao(const Sessao&) = delete;
    Sessao& operator=(const Sessao&) = delete;
};
inline double adquirir(const IFonteLeitura& fonte, bool disponivel, bool calibrado, int& abertas) {
    Sessao sessao(abertas);
    if (!disponivel) throw FalhaLeitura("fonte indisponivel");
    (void)calibrado; // TODO A: rejeitar a falta de calibracao com o tipo especifico.
    return fonte.valor();
}
inline double lerServico(const IFonteLeitura& fonte, bool disponivel, bool calibrado, int& abertas) {
    return adquirir(fonte, disponivel, calibrado, abertas); // propagacao intencional
}
struct ResultadoLeitura { bool sucesso; double valor; };
inline ResultadoLeitura executarCiclo(const IFonteLeitura& fonte, bool disponivel, bool calibrado, int& abertas) {
    try {
        return {true, lerServico(fonte, disponivel, calibrado, abertas)};
    } catch (const FalhaLeitura&) {
        return {false, 0};
    }
}
