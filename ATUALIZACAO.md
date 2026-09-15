# Atualizar um fork anterior às práticas integradas

Forks novos já possuem a infraestrutura. Este procedimento é para quem iniciou a atividade do capítulo 07 antes de 15/09/2026. O código de sensores e os documentos do estudante serão preservados. Não é necessário adicionar outro remoto.

## 1. Isolar a atualização na branch da prática A

Conclua e integre o capítulo 07. Se houver alterações locais, registre-as antes de continuar.

```bash
git switch main
git pull --ff-only origin main
git remote -v
git switch -c pratica/integrada-a
```

Use somente `origin` apontando para seu fork. Se a branch da prática A já existir, entre nela com `git switch pratica/integrada-a`.

## 2. Obter e conferir o pacote público

Os dois arquivos abaixo contêm o procedimento de mesclagem e as versões anterior/nova da infraestrutura. Não incluem a solução das extensões atribuídas aos estudantes.

```bash
curl -L --fail --silent --show-error https://raw.githubusercontent.com/rafaelrezo/poo-fundamentos-estacao/main/tools/atualizar_integradas.py -o /tmp/poo-atualizar-integradas.py
curl -L --fail --silent --show-error https://raw.githubusercontent.com/rafaelrezo/poo-fundamentos-estacao/main/tools/migracao_integradas.json -o /tmp/poo-migracao-integradas.json
```

Abra os arquivos no editor e confira o conteúdo. A ferramenta combina a baseline anterior, seu arquivo atual e a infraestrutura nova. Execute na raiz do fork:

```bash
python3 /tmp/poo-atualizar-integradas.py /tmp/poo-migracao-integradas.json
git diff --check
git diff --stat
git diff
```

Se houver conflitos, **nenhum arquivo do fork será escrito**. A ferramenta informa a pasta temporária com `atual`, `base`, `novo` e `mesclado` para cada arquivo. Com apoio do docente, resolva as regiões marcadas de `mesclado`, preservando a implementação do estudante, e copie as versões resolvidas para os respectivos arquivos do fork. Não copie marcadores de conflito. Não aceite o arquivo novo inteiro apenas para eliminar o conflito.

As cópias `atual` permitem recuperar o estado anterior de cada arquivo. O pacote altera módulos de infraestrutura, contratos, runner, workflow e instruções; não altera sensores, testes autorais ou os documentos produzidos pelo aluno.

## 3. Registrar a infraestrutura e continuar a prática

```bash
make run
git diff --check
git add include/relacoes.hpp include/fontes.hpp include/excecoes.hpp include/identidade.hpp include/colecoes.hpp src/relacoes.py src/fontes.py src/excecoes.py src/identidade.py src/colecoes.py tests/contrato.cpp tests/contrato.py tools/testar.py .github/workflows/testes.yml README.md GUIA_DOCENTE.md ATUALIZACAO.md
git commit -m "atualiza infraestrutura para duas praticas integradas"
make test ETAPA=A
```

O último comando ainda pode falhar no comportamento que você precisa implementar. Ele não deve falhar por comando desconhecido, arquivo ausente ou infraestrutura pendente que o novo roteiro fornece.

Continue na mesma branch; não repita sua criação ao voltar ao capítulo 10. A atualização fica num commit separado dentro da PR da prática A, sem uma entrega adicional. Se já tiver implementado etapas antigas, conserve as soluções válidas. As branches e contratos antigos seguem aceitos.
