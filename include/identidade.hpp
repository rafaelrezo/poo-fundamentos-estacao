#pragma once
#include <functional>
#include <string>
#include <stdexcept>
#include <utility>
class IdSensor {
    std::string valor_;
public:
    explicit IdSensor(std::string valor) : valor_(std::move(valor)) {
        if (valor_.empty()) throw std::invalid_argument("identificador vazio");
    }
    const std::string& valor() const { return valor_; }
    bool operator==(const IdSensor& outro) const { (void)outro; return false; } // TODO 12
    bool operator<(const IdSensor& outro) const { (void)outro; return false; } // TODO 12
};
struct HashId {
    std::size_t operator()(const IdSensor& id) const {
        return std::hash<std::string>{}(id.valor());
    }
};
