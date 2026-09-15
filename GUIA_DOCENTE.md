# Guia docente — práticas integradas

## Escopo e tempo

O capítulo 07 permanece com sua atividade de herança. O 08 mantém seu starter próprio. Nos capítulos 09–12, há duas atividades: A encerra 09+10; B encerra 11+12. Os capítulos 09 e 11 usam demonstrações completas sem entrega própria.

Reserve os quatro encontros de 2h: 09 expositivo; 10 com 80 min de exposição e 40 min de início de A; 11 expositivo; 12 com 60 min de modelagem e 60 min de início de B. O orçamento é de até 2h externas por prática, incluindo preparação. É uma estimativa de planejamento, a calibrar observando a turma; não é tempo comprovado por execução automatizada.

## O que avaliar

- A: consulta do painel e calibração; explicar associação, propagação, fronteira de captura e recurso liberado.
- B: inserção, busca e remoção; justificar igualdade das chaves, política de duplicata, multiplicidades e independência do sensor.
- Uma PR por atividade, com commits cumulativos do incremento guiado e da extensão. Não atribuir as antigas etapas 09–13 e UML como exercícios adicionais.
- Interface, fontes, bancada, troca de vínculo, RAII/finally, comparação, hash, genericidade, listagem e soma polimórfica são infraestrutura fornecida. A exposição explica essas decisões; o aluno deve entendê-las sem reimplementar tudo.

## Validação antes da distribuição

A baseline precisa compilar e executar com `make run`. A etapa 07 deve falhar na tag pendente. Numa cópia privada, complete a solução de referência e confira:

1. `make test ETAPA=A` falha primeiro na consulta; após o incremento guiado, na calibração; depois da extensão, passa.
2. `make test ETAPA=B` falha na inserção; após inserção/busca, na remoção; depois da extensão, passa.
3. Remover uma chave não modifica o sensor externo; consultas e aquisições veem o mesmo estado atualizado.
4. `make test-projeto` passa depois da atividade da Parte 2 e seus testes autorais detectam as seis mutações.
5. O material demonstrativo não publica a solução de calibração nem de remoção. A solução de referência não entra neste repositório público.

O runner mantém A -> 11 e B -> 13 como aliases cumulativos. As branches `pratica/integrada-a` e `pratica/integrada-b` executam exatamente o mesmo comando local. As antigas branches continuam mapeadas no workflow para compatibilidade.

## Forks antigos

Siga [ATUALIZACAO.md](ATUALIZACAO.md). A atualização faz mesclagem de três versões: baseline anterior, arquivo atual do estudante e infraestrutura nova. Nenhum arquivo é escrito se houver conflito; o relatório apresenta cópias para resolução acompanhada. Os sensores do capítulo 07 e os arquivos de decisões do aluno não são substituídos.

Uma atualização de infraestrutura pode integrar a mesma branch da prática A. Registre-a num commit separado. Avalie os comportamentos atribuídos, não a quantidade de linhas recebidas na atualização. Alunos com etapas antigas concluídas podem reaproveitá-las; não devem refazer suas soluções para copiar o novo starter.

## CI e revisão humana

A `main` executa somente a baseline, pois precisa receber forks novos com pendências intencionais. A evidência funcional é o resultado da branch/PR associado ao commit. Os workflows usam `contents: read`, sem segredos. Em forks com Actions desativado, habilite a execução e faça o próximo push.

Confira alterações em testes e automação pelo diff. Testes visíveis não provam entendimento nem correção de UML; confronte requisito, diagrama e programa. Em avaliação, peça defesa oral curta. A etapa 14 verifica autoria de testes com mutações em cópias temporárias: mutação que não compila não conta como detectada.

## Passagem para a Parte 2

A prática B verde deixa todos os contratos até 13 satisfeitos, incluindo a infraestrutura que passou a ser fornecida. `projeto/00-testes` amplia essa base; não há tarefa retirada do roteiro que ainda precise ser resolvida escondida entre as partes. Preserve o encaminhamento de `lerServico`/`ler_servico`, utilizado nos testes de propagação e mutação.

Referências operacionais: [eventos do GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) e [sintaxe e permissões](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), conferidas em 15/09/2026.
