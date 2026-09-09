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
    bool inserir(const IdSensor& id, const T& item) { (void)id; (void)item; return false; } // TODO 13
    const T* buscar(const IdSensor& id) const { (void)id; return nullptr; } // TODO 13
    bool remover(const IdSensor& id) { (void)id; return false; } // TODO 13
    std::size_t quantidade() const { return itens_.size(); }
    std::set<IdSensor> ids() const { return {}; } // TODO 13
};
// Exemplo especifico da simulacao: todas as fontes desta soma devem usar "%".
inline double somarPercentuais(const std::vector<std::unique_ptr<IFonteLeitura>>& fontes) {
    (void)fontes; return 0; // TODO 13: percorrer objetos pelo contrato, sem copiar unique_ptr.
}
