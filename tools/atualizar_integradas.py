"""Mescla infraestrutura nova com o fork, sem escrever quando houver conflitos."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python3 atualizar_integradas.py pacote.json (na raiz do fork)")
    raiz = Path.cwd().resolve()
    top = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
    if Path(top).resolve() != raiz:
        raise SystemExit("Execute na raiz do fork.")
    for args in (["git", "diff", "--quiet"], ["git", "diff", "--cached", "--quiet"]):
        if subprocess.run(args).returncode:
            raise SystemExit("Registre ou guarde as alteracoes atuais antes da atualizacao.")
    pacote = json.loads(Path(sys.argv[1]).read_text())
    if pacote.get("versao") != "integradas-2026-09-15":
        raise SystemExit("Pacote de atualizacao desconhecido.")
    alteracoes = {}
    conflitos = []
    # O pacote e publico e inspecionavel. Caminhos fora dos modulos previstos sao rejeitados.
    permitidos = {"README.md", "GUIA_DOCENTE.md", "ATUALIZACAO.md", ".github/workflows/testes.yml",
                  "tools/testar.py", "tests/contrato.cpp", "tests/contrato.py"}
    permitidos.update(f"include/{nome}.hpp" for nome in
                      ("relacoes", "fontes", "excecoes", "identidade", "colecoes"))
    permitidos.update(f"src/{nome}.py" for nome in
                      ("relacoes", "fontes", "excecoes", "identidade", "colecoes"))
    relatorio = Path(tempfile.mkdtemp(prefix="poo-atualizacao-"))
    for nome, versoes in pacote["arquivos"].items():
        if nome not in permitidos:
            raise SystemExit("Caminho nao permitido no pacote: " + nome)
        destino = raiz / nome
        if destino.resolve() != destino or (not destino.is_file() and versoes["antes"]):
            raise SystemExit("Arquivo ausente ou caminho simbolico: " + nome)
        pasta = relatorio / nome.replace("/", "_")
        pasta.mkdir()
        atual = destino.read_text() if destino.is_file() else ""
        for arquivo, texto in (("atual", atual), ("base", versoes["antes"]),
                               ("novo", versoes["depois"])):
            (pasta / arquivo).write_text(texto)
        resultado = subprocess.run(
            ["git", "merge-file", "-p", "-L", "seu-fork", "-L", "base-anterior",
             "-L", "infraestrutura-integrada", str(pasta / "atual"),
             str(pasta / "base"), str(pasta / "novo")],
            capture_output=True, text=True)
        if resultado.returncode < 0 or resultado.returncode > 127:
            raise SystemExit("Falha na mesclagem: " + resultado.stderr)
        (pasta / "mesclado").write_text(resultado.stdout)
        if resultado.returncode:
            conflitos.append(nome)
        elif resultado.stdout != atual:
            alteracoes[nome] = resultado.stdout
    if conflitos:
        print("Nenhum arquivo do fork foi alterado. Conflitos:")
        print("\n".join(conflitos))
        print("Versoes para resolucao acompanhada:", relatorio)
        raise SystemExit(1)
    for nome, texto in alteracoes.items():
        (raiz / nome).write_text(texto)
        print("Atualizado:", nome)
    print("Revise git diff; sensores e documentos do estudante foram preservados.")
    print("Copias anteriores e mescladas:", relatorio)


if __name__ == "__main__":
    main()
