CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Werror -pedantic -Iinclude
.PHONY: build run test test-aluno
build:
	mkdir -p build
	$(CXX) $(CXXFLAGS) src/main.cpp -o build/estacao
run: build
	./build/estacao
	PYTHONPATH=src python3 src/main.py
test: build
	python3 tools/testar.py $(ETAPA)
test-aluno: build
	$(CXX) $(CXXFLAGS) tests/aluno.cpp -o build/aluno
	./build/aluno
	PYTHONPATH=src python3 tests/aluno.py

# Baseline do projeto. Acrescente aqui os testes de cada incremento.
.PHONY: test-projeto
test-projeto:
	$(MAKE) test ETAPA=14
