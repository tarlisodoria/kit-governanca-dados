"""Valida fichas de metadados do kit de governança de dados.

Uso:
    python scripts/validar_metadados.py ficha1.yaml [ficha2.yaml ...]

Retorna código 1 se alguma ficha tiver erro, para uso em CI.
"""
import re
import sys
from pathlib import Path

import yaml

OBRIGATORIOS = [
    "titulo", "criador", "assunto", "descricao", "data", "tipo",
    "formato", "direitos", "classificacao", "responsavel",
]
NIVEIS = {"publico", "interno", "restrito", "confidencial"}
DATA_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def vazio(valor):
    return valor is None or (isinstance(valor, (str, list)) and len(valor) == 0)


def validar(caminho):
    erros, avisos = [], []
    ficha = yaml.safe_load(Path(caminho).read_text(encoding="utf-8")) or {}

    for campo in OBRIGATORIOS:
        if vazio(ficha.get(campo)):
            erros.append(f"campo obrigatório vazio: {campo}")

    nivel = ficha.get("classificacao")
    if nivel and nivel not in NIVEIS:
        erros.append(f"classificacao inválida: {nivel!r} (use {', '.join(sorted(NIVEIS))})")

    for campo in ("data", "revisao_em"):
        valor = ficha.get(campo)
        if valor and not DATA_ISO.match(str(valor)):
            erros.append(f"{campo} fora do formato AAAA-MM-DD: {valor}")

    if ficha.get("contem_dado_pessoal") and vazio(ficha.get("base_legal_lgpd")):
        erros.append("contem_dado_pessoal é true, mas base_legal_lgpd está vazio")

    if ficha.get("contem_dado_pessoal") and nivel == "publico":
        erros.append("ficha com dado pessoal não pode ser classificada como publico")

    if vazio(ficha.get("identificador")):
        avisos.append("sem identificador persistente (item F1 do checklist FAIR)")
    if vazio(ficha.get("dicionario_de_dados")):
        avisos.append("sem dicionário de dados associado")

    return erros, avisos


def main(arquivos):
    if not arquivos:
        print(__doc__)
        return 2
    falhou = False
    for arquivo in arquivos:
        erros, avisos = validar(arquivo)
        status = "ERRO" if erros else "OK"
        print(f"[{status}] {arquivo}")
        for e in erros:
            print(f"  erro: {e}")
        for a in avisos:
            print(f"  aviso: {a}")
        falhou = falhou or bool(erros)
    return 1 if falhou else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
