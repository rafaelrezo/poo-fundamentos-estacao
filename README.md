# Fundamentos de POO: estação de sensores

Starter público para as seções 07 e 09–15 do curso. As seções 01–06 e seus repositórios permanecem independentes; não sobrescreva suas entregas. A seção 08 mantém o repositório `rafaelrezo/poo-polimorfismo-contratos`. Depois dela, retorne a este fork para a seção 09.

## Requisitos e preparação

Git, GNU Make, g++ com C++17 e Python 3.10+. Faça fork, clone seu fork, mantenha apenas `origin` apontando para ele. Não configure `upstream`.

```bash
make run
```

Cada linguagem mostra inicialmente `PENDENTE: 50 %` e `PENDENTE: 25 C`. O código inicial compila; os testes funcionais falham intencionalmente. O primeiro diagnóstico de `make test ETAPA=07` pede a tag correta na classe-base. Todos os módulos já possuem esqueletos compiláveis; complete apenas os TODOs da etapa atual.

## Caminho das etapas

| Seção | Branch | Comando local e CI | Incremento |
|---|---|---|---|
| 07 | `pratica/07-heranca` | `make test ETAPA=07` | base com tag, especializações e invariantes |
| 09 | `pratica/09-associacoes` | `make test ETAPA=09` | dois painéis compartilham e trocam sensor |
| 10 | `pratica/10-interfaces` | `make test ETAPA=10` | contrato abstrato e duas implementações |
| 11 | `pratica/11-excecoes` | `make test ETAPA=11` | falhas próprias, propagação e limpeza |
| 12 | `pratica/12-igualdade` | `make test ETAPA=12` | identidade, igualdade, ordem e hash |
| 13 | `pratica/13-colecoes` | `make test ETAPA=13` | catálogo genérico e coleção polimórfica |
| 14 | `pratica/14-testes` | `make test ETAPA=14` | colaboração, testes autorais e mutações |
| 15 | `pratica/15-uml` | `make test ETAPA=14` | revisão UML do sistema implementado |

Cada comando repete as etapas anteriores deste starter. Não existe ETAPA=08 aqui; não confunda número da seção com etapa do outro repositório. Na main, CI verifica somente baseline executável; a evidência funcional da entrega é a execução da branch/PR com a etapa correspondente.

A aula no site do curso conduz o primeiro incremento de cada seção e reserva uma extensão para adaptação. Registre a decisão em `docs/decisoes.md` e o modelo em `docs/diagrama.md`.

## Contratos que não mudam

- Tag não vazia; nível finito em 0..100 e temperatura finita em -40..125.
- Construção inválida lança erro; atualização inválida retorna falso e preserva a leitura.
- A base da seção 07 é concreta quanto a operações (construtor protegido C++); a interface abstrata é elaborada na seção 10.
- `PainelFixo` e `Bancada` referenciam sensores externos; o chamador garante sua vida em C++.
- `IFonteLeitura`: `valor()` e `unidade()` são consultas; cliente não seleciona classes.
- Falha de aquisição é uma operação distinta da rejeição de atualização. Exceções previstas são capturadas na fronteira; defeitos inesperados propagam.
- `IdSensor` compara a tag exata, sem normalização; nenhuma API modifica seu conteúdo. Hash é coerente com igualdade.
- Catálogo rejeita duplicata sem substituir o item. `buscar` retorna ponteiro nulo/None quando ausente; valores None não fazem parte do contrato de itens desta atividade.
- Soma de fontes é um experimento com percentuais de simulação, todos na mesma unidade; não some grandezas físicas incompatíveis.

## Fluxo de entrega

Crie a branch da seção a partir da main com a etapa anterior integrada; faça commits pequenos, teste localmente, push e PR para a main **do próprio fork**, nunca para o docente. Confira Actions e associe o resultado ao commit. Atualize `AI_LOG.md`, inclusive se não usou IA.

Não altere `tests/contrato.*`, ferramentas, Makefile ou CI para obter aprovação. Na seção 14, **escreva seus próprios testes em `tests/aluno.cpp` e `tests/aluno.py`**. `make test-aluno` executa só esses testes. A etapa 14 também insere defeitos temporários para verificar se eles detectam problemas reais. O teste de mutação não altera seus fontes originais.

## Limites

A automação verifica contratos e algumas regressões. Não comprova entendimento, semântica UML, qualidade de todos os testes ou ausência universal de defeitos. O professor revisa diff, justificativas e, em avaliações, defesa oral curta. Consulte `GUIA_DOCENTE.md` para operação de CI.

## Continuidade no projeto integrador

Depois de concluir e integrar a etapa 15, use branches `projeto/01-arquitetura`, `projeto/02-integracao`, `projeto/03-regras`, `projeto/04-persistencia`, `projeto/05-comunicacao` e `projeto/06-entrega`. A CI executa `make test-projeto` nessas branches. Inicialmente esse alvo repete a etapa 14; a equipe deve acrescentar os testes de cada incremento ao mesmo alvo. O baseline verde sozinho não valida JSON, persistência ou rede. Abra PR para a main do próprio fork e registre resultados e decisões.
