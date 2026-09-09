from pathlib import Path
import os
import subprocess
import sys

ETAPAS=["07","09","10","11","12","13","14"]
etapa=sys.argv[1] if len(sys.argv)>1 else ""
if etapa not in ETAPAS:
    raise SystemExit("Use make test ETAPA="+"|".join(ETAPAS))
subprocess.run(["g++","-std=c++17","-Wall","-Wextra","-Werror","-pedantic","-Iinclude","tests/contrato.cpp","-o","build/contrato"],check=True)
for e in ETAPAS[:ETAPAS.index(etapa)+1]:
    result = subprocess.run(["./build/contrato",e])
    if result.returncode: raise SystemExit(result.returncode)
    result = subprocess.run(["python3","tests/contrato.py",e],env={**os.environ,"PYTHONPATH":"src"})
    if result.returncode: raise SystemExit(result.returncode)
if etapa=="14":
    subprocess.run(["make","test-aluno"],check=True)
    subprocess.run(["python3","tools/verificar_testes_aluno.py"],check=True)
