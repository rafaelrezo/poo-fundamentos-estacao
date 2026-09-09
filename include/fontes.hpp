#pragma once
#include "sensores.hpp"
// TODO 10: tornar este contrato abstrato; nenhuma leitura generica faz sentido.
class IFonteLeitura {
public:
    virtual ~IFonteLeitura() = default;
    virtual double valor() const { return 0; }
    virtual std::string unidade() const { return "PENDENTE"; }
};
class FonteNivel : public IFonteLeitura {
    const SensorNivel& sensor_;
public:
    explicit FonteNivel(const SensorNivel& sensor) : sensor_(sensor) {}
    double valor() const override { (void)sensor_; return 0; } // TODO 10
    std::string unidade() const override { return "PENDENTE"; } // TODO 10
};
class FonteConstante : public IFonteLeitura {
    double valor_;
    std::string unidade_;
public:
    FonteConstante(double valor, std::string unidade) : valor_(valor), unidade_(std::move(unidade)) {}
    double valor() const override { (void)valor_; return 0; } // TODO 10
    std::string unidade() const override { return "PENDENTE"; } // TODO 10
};
inline double lerFonte(const IFonteLeitura& fonte) { (void)fonte; return 0; } // TODO 10
