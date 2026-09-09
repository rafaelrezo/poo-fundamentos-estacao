# Fundamentos de POO: estação de sensores

Starter público para as seções 07 e 09–12, além da abertura da Parte 2 do curso. As seções 01–06 e seus repositórios permanecem independentes; não sobrescreva suas entregas. A seção 08 mantém o repositório `rafaelrezo/poo-polimorfismo-contratos`. Depois dela, retorne a este fork para a seção 09.

## Requisitos e preparação

Git, GNU Make, g++ com C++17 e Python 3.10+. Faça fork, clone seu fork, mantenha apenas `origin` apontando para ele. Não configure `upstream`.

```bash
make run
```

Cada linguagem mostra inicialmente `PENDENTE: 50 %` e `PENDENTE: 25 C`. O código inicial compila; os testes funcionais falham intencionalmente. O primeiro diagnóstico de `make test ETAPA=07` pede a tag correta na classe-base. Todos os módulos já possuem esqueletos compiláveis; complete apenas os TODOs da etapa atual.

## Caminho das etapas

| Capítulo atual | Branch | Comando local e CI | Incremento |
|---|---|---|---|
| 07 | `pratica/07-heranca` | `make test ETAPA=07` | herança e invariantes |
| 09 — incremento A | `pratica/09-associacoes` | `make test ETAPA=09` | colaboração e vínculos |
| 09 — incremento B | `pratica/10-interfaces` | `make test ETAPA=10` | interface e fontes |
| 10 | `pratica/11-excecoes` | `make test ETAPA=11` | propagação e limpeza |
| 11 — incremento A | `pratica/12-igualdade` | `make test ETAPA=12` | chaves, igualdade e hash |
| 11 — incremento B | `pratica/13-colecoes` | `make test ETAPA=13` | catálogo e iteração |
| 12 — fim da Parte 1 | `pratica/12-uml` | `make test ETAPA=13` | modelo do sistema, antes dos testes autorais |
| Parte 2 — capítulo 01 | `projeto/00-testes` | `make test-projeto` | etapa técnica 14: projeto e testes autorais |

Os números de ETAPA são IDs dos contratos publicados, não números dos capítulos atuais. Eles permanecem estáveis para preservar forks. Não existe ETAPA=08 neste repositório. `pratica/14-testes` e `pratica/15-uml` continuam aceitas apenas por compatibilidade com o roteiro anterior; novos trabalhos seguem a tabela acima.

Cada comando repete as etapas técnicas anteriores. UML exige apenas até13; a etapa14 começa depois, na Parte2. Na main, CI verifica somente o baseline executável; a evidência funcional é a execução da branch/PR.

A aula no site do curso conduz o primeiro incremento de cada seção e reserva uma extensão para adaptação. Registre a decisão em `docs/decisoes.md` e o modelo em `docs/diagrama.md`.

## Contratos que não mudam

- Tag não vazia; nível finito em 0..100 e temperatura finita em -40..125.
- Construção inválida lança erro; atualização inválida retorna falso e preserva a leitura.
- A base da seção 07 é concreta quanto a operações (construtor protegido C++); a interface abstrata é elaborada no capítulo09.
- `PainelFixo` e `Bancada` referenciam sensores externos; o chamador garante sua vida em C++.
- `IFonteLeitura`: `valor()` e `unidade()` são consultas; cliente não seleciona classes.
- Falha de aquisição é uma operação distinta da rejeição de atualização. Exceções previstas são capturadas na fronteira; defeitos inesperados propagam.
- `IdSensor` compara a tag exata, sem normalização; nenhuma API modifica seu conteúdo. Hash é coerente com igualdade.
- Catálogo rejeita duplicata sem substituir o item. `buscar` retorna ponteiro nulo/None quando ausente; valores None não fazem parte do contrato de itens desta atividade.
- Soma de fontes é um experimento com percentuais de simulação, todos na mesma unidade; não some grandezas físicas incompatíveis.

## Fluxo de entrega

Crie a branch da seção a partir da main com a etapa anterior integrada; faça commits pequenos, teste localmente, push e PR para a main **do próprio fork**, nunca para o docente. Confira Actions e associe o resultado ao commit. Atualize `AI_LOG.md`, inclusive se não usou IA.

Não altere `tests/contrato.*`, ferramentas, Makefile ou CI para obter aprovação. Na abertura da Parte2, **escreva seus próprios testes em `tests/aluno.cpp` e `tests/aluno.py`**. `make test-aluno` executa só esses testes. A etapa 14 também insere defeitos temporários para verificar se eles detectam problemas reais. O teste de mutação não altera seus fontes originais.

## Limites

A automação verifica contratos e algumas regressões. Não comprova entendimento, semântica UML, qualidade de todos os testes ou ausência universal de defeitos. O professor revisa diff, justificativas e, em avaliações, defesa oral curta. Consulte `GUIA_DOCENTE.md` para operação de CI.

## Continuidade no projeto integrador

Depois do capítulo12 (UML), conclua `projeto/00-testes` e integre a etapa técnica14. Depois use as branches `projeto/01-arquitetura`, `projeto/02-integracao`, `projeto/03-regras`, `projeto/04-persistencia`, `projeto/05-comunicacao` e `projeto/06-entrega`. A CI executa `make test-projeto` nessas branches. Inicialmente esse alvo repete a etapa 14; a equipe deve acrescentar os testes de cada incremento ao mesmo alvo. O baseline verde sozinho não valida JSON, persistência ou rede. Abra PR para a main do próprio fork e registre resultados e decisões.
