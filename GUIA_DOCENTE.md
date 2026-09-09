# Guia docente

O starter constitui uma trilha nova e preserva os arquivos já utilizados nas seções 01–06. Não se deve exigir que o estudante encontre ControladorNivel ou ETAPA=06 no repositório de composição; a seção 07 inicia este recorte explícito. A seção 08 continua usando seu starter próprio, e a 09 retoma a main deste fork.

## Roteiro e validação

Use a tabela de branches do README. Cada etapa tem explicação guiada no site, uma extensão autônoma e testes cumulativos locais/remotos. A solução de referência deve ser mantida separadamente; este repositório contém apenas esqueletos, infraestrutura, testes e instruções.

Antes da distribuição, `make run` precisa compilar nas duas linguagens; `make test ETAPA=07` deve falhar na tag pendente. Na solução, a etapa 14 deve passar todas as etapas e detectar seis mutações nos testes autorais. Nenhum segredo é necessário; a única permissão do workflow é contents: read. Falhas funcionais no starter são intencionais; erros de ferramenta ou etapas ausentes não são.

A main executa apenas baseline, pois precisa servir a forks novos. Ao avaliar entregas, confira a execução da branch/PR correspondente ao commit. Se os arquivos de automação tiverem sido modificados, investigue o diff e valide com os contratos originais em ambiente isolado.

## Competências avaliadas

07: herança e invariantes; 09: referência, associação e ciclo de vida; 10: abstração, interface e cliente substituível; 11: lançamento, propagação, captura e limpeza; 12: igualdade/identidade/hash; 13: 1:N e generics; 14: coesão, acoplamento e autoria de testes; 15: UML consistente com o código.

Os testes de mutação da etapa 14 alteram temporariamente pontos documentados do esqueleto (política e encaminhamento de aquisição). Uma mutação que não compila não conta como detectada. A inspeção deve confirmar que os testes do aluno falham pelo comportamento, não por procurar texto no fonte. A ferramenta não substitui revisão humana nem comprova cobertura total.

## Tempo e continuidade

As seções são unidades de material e não equivalem automaticamente a encontros adicionais. Combine exposição curta em sala com prática entre encontros, conforme o cronograma do curso e o tempo restante após as aulas já dadas. Não reduza retroativamente o tempo das seções 01–06. Ao migrar ao projeto, conserve os testes e documente os adaptadores entre os contratos; não troque silenciosamente retorno falso por exceção.
