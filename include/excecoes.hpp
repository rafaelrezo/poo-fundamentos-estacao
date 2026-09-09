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
    ~Sessao() { } // TODO 11: liberar o recurso simulado, inclusive na excecao.
    Sessao(const Sessao&) = delete;
    Sessao& operator=(const Sessao&) = delete;
};
inline double adquirir(const IFonteLeitura& fonte, bool disponivel, bool calibrado, int& abertas) {
    Sessao sessao(abertas);
    (void)disponivel; (void)calibrado; // TODO 11: lancar os tipos de falha apropriados.
    return fonte.valor();
}
inline double lerServico(const IFonteLeitura& fonte, bool disponivel, bool calibrado, int& abertas) {
    return adquirir(fonte, disponivel, calibrado, abertas); // propagacao intencional
}
struct ResultadoLeitura { bool sucesso; double valor; };
inline ResultadoLeitura executarCiclo(const IFonteLeitura& fonte, bool disponivel, bool calibrado, int& abertas) {
    // TODO 11: capturar FalhaLeitura na fronteira; retornar {false, 0} nesse caso.
    return {true, lerServico(fonte, disponivel, calibrado, abertas)};
}
