# Fundamentos de POO: estação de sensores

Starter público do capítulo 07, das práticas integradas **A (09+10)** e **B (11+12)** e da abertura da Parte 2. O capítulo 08 usa `rafaelrezo/poo-polimorfismo-contratos`; depois dele, retorne a este fork.

## Requisitos e primeira execução

Git, GNU Make, g++ com C++17 e Python 3.10+. Faça fork e clone seu próprio fork. Mantenha somente `origin` apontando para ele, sem `upstream`.

```bash
make run
```

O programa compila; em cada linguagem, mostra `PENDENTE: 50 %` e `PENDENTE: 25 C`. O capítulo 07 completa a identificação dos sensores. `make test ETAPA=07` inicialmente falha pedindo a tag correta.

Já possui um fork anterior a esta revisão? Siga [ATUALIZACAO.md](ATUALIZACAO.md) antes das práticas integradas. Não substitua as implementações do estudante pelo starter pendente.

## Duas práticas integradas

| Momento | Branch | Comando local e CI | Trabalho do estudante |
|---|---|---|---|
| Capítulo 07 | `pratica/07-heranca` | `make test ETAPA=07` | encaminhar tag à base e preservar invariantes |
| Final do 10, integrando 09+10 | `pratica/integrada-a` | `make test ETAPA=A` | consulta do painel; extensão de calibração |
| Final do 12, integrando 11+12 | `pratica/integrada-b` | `make test ETAPA=B` | inserção e busca; remoção e modelagem |
| Parte 2 — capítulo 01 | `projeto/00-testes` | `make test-projeto` | delegação e testes autorais |

Os capítulos 09 e 11 são expositivos com demonstrações; não há entrega própria neles. Cada prática integrada tem um incremento guiado, uma extensão e **uma PR**. Faça commits pequenos na branch da atividade. A CI repete o contrato completo a cada push; uma falha durante o incremento guiado indica a extensão pendente. Integre somente depois de concluir e validar a atividade.

### Prática A

Pré-requisito: capítulo 07 integrado. Complete `PainelFixo.leitura` em `include/relacoes.hpp` e `src/relacoes.py`. Depois adapte `adquirir` em `include/excecoes.hpp` e `src/excecoes.py` para a falta de calibração. O site demonstra a consulta e a falha de indisponibilidade; a extensão exige decisão do aluno.

São fornecidos: troca de vínculo, bancada, contrato abstrato, fontes, sessão e limpeza, falha de indisponibilidade, serviço e captura. Esses comportamentos continuam testados, mas não são seis exercícios adicionais.

`make test ETAPA=A` repete os contratos técnicos 07, 09, 10 e 11. Primeiro aponta a consulta pendente; depois, a calibração. Ao concluir, termina com `OK pratica integrada A (C++ e Python)`.

### Prática B

Pré-requisito: A integrada. Complete `inserir`, `buscar` e `remover` em `include/colecoes.hpp` e `src/colecoes.py`. O tipo genérico, a identidade, a comparação, o hash, a listagem e a soma polimórfica são infraestrutura fornecida e explicada nas demonstrações.

`make test ETAPA=B` repete A e os contratos 12 e 13. Depois da inserção e busca, a primeira pendência será a remoção. Ao concluir, termina com `OK pratica integrada B (C++ e Python)`.

No mesmo trabalho, atualize `docs/diagrama.md`: vista do catálogo, pequena vista de colaboração e três correspondências com o código. Justifique multiplicidades e a independência do sensor externo. Código e modelo formam uma única entrega.

## Contratos preservados

- Tag não vazia; nível finito em 0..100 e temperatura finita em -40..125.
- Construção inválida lança erro; atualização inválida retorna falso e preserva a leitura.
- A base do capítulo 07 não declara operações abstratas; seu construtor C++ é protegido. `IFonteLeitura` é a interface abstrata do capítulo 09.
- `PainelFixo` e `Bancada` referenciam sensores externos; o chamador garante sua vida em C++.
- As fontes oferecem `valor()` e `unidade()` como consultas. O cliente aceita novas implementações sem selecionar classes.
- Indisponibilidade tem prioridade sobre calibração. Falhas previstas são recuperadas na fronteira; defeitos inesperados propagam após a limpeza.
- `IdSensor` usa a tag exata, sem normalização. Chaves são estáveis; hash é coerente com igualdade.
- Catálogo rejeita duplicata sem substituir o item. Busca ausente retorna ponteiro nulo/None; `None` não é um item válido do domínio desta atividade.
- Remoção não altera o sensor externo. Em Python, referências externas a registros imutáveis podem continuar existindo.
- A soma de fontes fornecida é um experimento com percentuais da mesma unidade, não uma soma de grandezas físicas incompatíveis.

## Entrega e evidências

Crie a branch documentada a partir da `main` com a atividade anterior integrada. Execute o comando local, faça push e abra PR para a `main` **do próprio fork**, nunca contra o repositório-base. Inclua saída local, link de Actions associado ao commit e explicação técnica. Registre em `AI_LOG.md` os pedidos, aceites/rejeições e justificativas, ou declare ausência de IA.

Se Actions estiver desativado no fork, habilite os workflows na aba Actions. Na `main`, CI verifica apenas a baseline executável; a evidência funcional é a execução da branch/PR. A automação não comprova compreensão ou correção semântica de UML. O docente revisa diff, decisões e, em avaliações, faz defesa oral curta.

Não altere testes fornecidos, ferramentas, Makefile ou CI para obter aprovação. Na abertura da Parte 2, escreva seus testes em `tests/aluno.cpp` e `tests/aluno.py`. `make test-aluno` executa esses arquivos; `make test-projeto` também verifica se eles detectam seis defeitos deliberados em cópias temporárias.

## Compatibilidade e continuidade

Os IDs antigos continuam válidos: `07`, `09`, `10`, `11`, `12`, `13`, `14`. A equivale à validação até 11; B, até 13. As branches antigas seguem aceitas por compatibilidade, sem constituir entregas extras para o novo roteiro. As práticas ainda não concluídas permanecem com marcadores de comportamento pendente.

Após integrar B, use `projeto/00-testes`. O comando `make test-projeto` executa a etapa técnica 14, incluindo todos os contratos anteriores e os testes autorais. Não é necessário completar uma atividade adicional de UML. Depois, use as branches `projeto/01-arquitetura`, `projeto/02-integracao`, `projeto/03-regras`, `projeto/04-persistencia`, `projeto/05-comunicacao` e `projeto/06-entrega`. Acrescente os testes de cada incremento ao mesmo alvo: a baseline não valida JSON, persistência ou rede.

Consulte [GUIA_DOCENTE.md](GUIA_DOCENTE.md) para escopo e validação.
