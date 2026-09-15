#pragma once
#include "sensores.hpp"
// Infraestrutura demonstrada no capitulo 09: contrato e fontes.
class IFonteLeitura {
public:
    virtual ~IFonteLeitura() = default;
    virtual double valor() const = 0;
    virtual std::string unidade() const = 0;
};
class FonteNivel : public IFonteLeitura {
    const SensorNivel& sensor_;
public:
    explicit FonteNivel(const SensorNivel& sensor) : sensor_(sensor) {}
    double valor() const override { return sensor_.valor(); }
    std::string unidade() const override { return sensor_.unidade(); }
};
class FonteConstante : public IFonteLeitura {
    double valor_;
    std::string unidade_;
public:
    FonteConstante(double valor, std::string unidade) : valor_(valor), unidade_(std::move(unidade)) {}
    double valor() const override { return valor_; }
    std::string unidade() const override { return unidade_; }
};
inline double lerFonte(const IFonteLeitura& fonte) { return fonte.valor(); }
