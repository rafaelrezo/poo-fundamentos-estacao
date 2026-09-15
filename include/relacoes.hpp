#pragma once
#include "sensores.hpp"
class PainelFixo {
    const SensorNivel* sensor_;
public:
    explicit PainelFixo(const SensorNivel& sensor) : sensor_(&sensor) {}
    double leitura() const { (void)sensor_; return 0; } // TODO A: consultar o associado (incremento guiado).
    void conectar(const SensorNivel& sensor) { sensor_ = &sensor; }
};
// Agrupamento de uma vaga. Nao e dono do sensor; ambos podem existir separados.
class Bancada {
    const SensorNivel* sensor_ = nullptr;
public:
    void receber(const SensorNivel& sensor) { sensor_ = &sensor; }
    void liberar() { sensor_ = nullptr; }
    const SensorNivel* sensor() const { return sensor_; }
};
inline double consultarAgora(const SensorNivel& sensor) { return sensor.valor(); }
