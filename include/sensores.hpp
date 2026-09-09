#pragma once
#include <cmath>
#include <stdexcept>
#include <string>
#include <utility>
class Sensor {
    std::string tag_;
protected:
    explicit Sensor(std::string tag) : tag_(std::move(tag)) {
        if (tag_.empty()) throw std::invalid_argument("tag vazia");
    }
public:
    const std::string& tag() const { return tag_; }
};
class SensorNivel : public Sensor {
    double valor_;
public:
    explicit SensorNivel(std::string tag, double valor = 50)
        : Sensor("PENDENTE"), valor_(valor) { // TODO 07: inicializar a base com a tag.
        (void)tag;
        if (!std::isfinite(valor) || valor < 0 || valor > 100)
            throw std::invalid_argument("nivel fora da faixa");
    }
    double valor() const { return valor_; }
    std::string unidade() const { return "%"; }
    bool atualizar(double valor) {
        // TODO 07: rejeitar nao finitos e valores fora de 0..100 sem alterar estado.
        (void)valor; return false;
    }
};
class SensorTemperatura : public Sensor {
    double valor_;
public:
    explicit SensorTemperatura(std::string tag, double valor = 25)
        : Sensor("PENDENTE"), valor_(valor) { // TODO 07: inicializar a base.
        (void)tag;
        if (!std::isfinite(valor) || valor < -40 || valor > 125)
            throw std::invalid_argument("temperatura fora da faixa");
    }
    double valor() const { return valor_; }
    std::string unidade() const { return "C"; }
    bool atualizar(double valor) {
        // TODO 07: aplicar a faixa -40..125.
        (void)valor; return false;
    }
};
