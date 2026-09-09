#pragma once
#include "fontes.hpp"
class PoliticaAlarme {
    double limite_;
public:
    explicit PoliticaAlarme(double limite) : limite_(limite) {}
    bool aciona(double valor) const { return valor > limite_; }
};
class ControladorConsulta {
    const IFonteLeitura& fonte_;
    PoliticaAlarme politica_;
public:
    ControladorConsulta(const IFonteLeitura& fonte, PoliticaAlarme politica)
        : fonte_(fonte), politica_(politica) {}
    bool avaliar() const { (void)fonte_; (void)politica_; return false; } // TODO 14: delegar.
};
