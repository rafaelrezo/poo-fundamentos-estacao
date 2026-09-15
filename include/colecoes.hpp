#pragma once
#include "identidade.hpp"
#include "fontes.hpp"
#include <map>
#include <set>
#include <vector>
#include <memory>
struct Medicao { double valor; std::string unidade; };
template<typename T>
class Catalogo {
    std::map<IdSensor, T> itens_;
public:
    bool inserir(const IdSensor& id, const T& item) { (void)id; (void)item; return false; } // TODO B
    const T* buscar(const IdSensor& id) const { (void)id; return nullptr; } // TODO B
    bool remover(const IdSensor& id) { (void)id; return false; } // TODO B
    std::size_t quantidade() const { return itens_.size(); }
    std::set<IdSensor> ids() const {
        std::set<IdSensor> resultado;
        for (const auto& par : itens_) resultado.insert(par.first);
        return resultado;
    }
};
// Exemplo especifico da simulacao: todas as fontes desta soma devem usar "%".
inline double somarPercentuais(const std::vector<std::unique_ptr<IFonteLeitura>>& fontes) {
    double total = 0;
    for (const auto& fonte : fontes) total += fonte->valor();
    return total;
}
