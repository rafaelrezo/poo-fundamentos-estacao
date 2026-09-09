#pragma once
#include "sensores.hpp"
class PainelFixo {
    const SensorNivel* sensor_;
public:
    explicit PainelFixo(const SensorNivel& sensor) : sensor_(&sensor) {}
    double leitura() const { (void)sensor_; return 0; } // TODO 09: consultar o associado.
    void conectar(const SensorNivel& sensor) { (void)sensor; } // TODO 09: trocar vinculo.
};
// Agrupamento de uma vaga. Nao e dono do sensor; ambos podem existir separados.
class Bancada {
    const SensorNivel* sensor_ = nullptr;
public:
    void receber(const SensorNivel& sensor) { (void)sensor; } // TODO 09
    void liberar() { sensor_ = nullptr; }
    const SensorNivel* sensor() const { return sensor_; }
};
inline double consultarAgora(const SensorNivel& sensor) { return sensor.valor(); }
