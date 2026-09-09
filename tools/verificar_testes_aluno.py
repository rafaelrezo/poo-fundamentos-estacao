"""Verifica comportamento dos testes autorais com alteracoes deliberadas em copia temporaria."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile

# Os pontos de mutacao pertencem ao esqueleto fornecido. Nao editar para contornar a verificacao.
mutacoes=[
 ("include/projeto.hpp","return valor > limite_;","return valor >= limite_;","fronteira C++"),
 ("include/projeto.hpp","return valor > limite_;","(void)valor; return false;","alarme C++"),
 ("include/excecoes.hpp","return adquirir(fonte, disponivel, calibrado, abertas);","(void)disponivel; (void)calibrado; (void)abertas; return fonte.valor();","propagacao C++"),
 ("src/projeto.py","return valor > self._limite","return valor >= self._limite","fronteira Python"),
 ("src/projeto.py","return valor > self._limite","return False","alarme Python"),
 ("src/excecoes.py","return adquirir(fonte, disponivel, calibrado, sessao)","return fonte.valor()","propagacao Python"),
]
for arquivo,antes,depois,nome in mutacoes:
    with tempfile.TemporaryDirectory(prefix="poo-mutacao-") as pasta:
        copia=Path(pasta)/"exercicio"
        shutil.copytree(".",copia,ignore=shutil.ignore_patterns(".git","build","__pycache__"))
        p=copia/arquivo;s=p.read_text()
        if antes not in s:
            raise SystemExit("Ponto de mutacao alterado; restaure o trecho fornecido: "+nome)
        p.write_text(s.replace(antes,depois,1))
        if arquivo.endswith(".hpp"):
            compilacao=subprocess.run(["g++","-std=c++17","-Wall","-Wextra","-Werror","-pedantic","-Iinclude","tests/aluno.cpp","-o","aluno"],cwd=copia,capture_output=True,text=True)
            if compilacao.returncode:
                raise SystemExit("Mutacao nao compilou; isso nao prova que o teste detectou o defeito: "+nome+"\n"+compilacao.stderr)
            cmd=["./aluno"]
        else:
            cmd=["python3","tests/aluno.py"]
        resultado=subprocess.run(cmd,cwd=copia,env={**os.environ,"PYTHONPATH":"src"},capture_output=True,text=True)
        if resultado.returncode==0:
            raise SystemExit("FALHA: seus testes nao detectaram "+nome)
        print("OK testes autorais detectaram",nome)
