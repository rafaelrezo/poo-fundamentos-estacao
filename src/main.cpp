#include "sensores.hpp"
#include <iostream>
int main() {
    SensorNivel nivel{"LT-101"};
    SensorTemperatura temperatura{"TT-201"};
    std::cout << nivel.tag() << ": " << nivel.valor() << " " << nivel.unidade() << '\n';
    std::cout << temperatura.tag() << ": " << temperatura.valor() << " " << temperatura.unidade() << '\n';
    std::cout << "Consulte os TODOs e execute make test ETAPA=07 para o primeiro incremento.\n";
}
