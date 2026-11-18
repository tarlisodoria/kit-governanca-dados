# Kit de Governança de Dados para Pesquisa

Modelos prontos para organizar, classificar e documentar dados de pesquisa científica. Tudo aqui parte de padrões públicos (princípios FAIR e Dublin Core) e pode ser adaptado a qualquer instituição.

O objetivo é simples: um pesquisador que nunca ouviu falar em governança de dados consegue, em uma tarde, deixar um conjunto de dados descrito, classificado e pronto para ser encontrado e reutilizado.

## O que tem aqui

| Pasta | Conteúdo | Para que serve |
|---|---|---|
| [`classificacao/`](classificacao/modelo-classificacao.md) | Modelo de classificação da informação em 4 níveis | Decidir quem pode acessar cada conjunto de dados |
| [`metadados/`](metadados/dublin-core-modelo.yaml) | Ficha de metadados baseada em Dublin Core, com exemplo preenchido | Descrever um conjunto de dados de forma padronizada |
| [`dicionario/`](dicionario/dicionario-de-dados-modelo.csv) | Modelo de dicionário de dados | Explicar cada coluna: tipo, unidade, valores aceitos |
| [`fair/`](fair/checklist-fair.md) | Checklist FAIR comentado | Avaliar se o dado é localizável, acessível, interoperável e reutilizável |
| [`scripts/`](scripts/validar_metadados.py) | Validador de fichas de metadados em Python | Conferir campos obrigatórios e nível de classificação antes de publicar |

## Como usar

1. Copie `metadados/dublin-core-modelo.yaml` para a pasta do seu conjunto de dados e preencha.
2. Classifique o conjunto com o [modelo de classificação](classificacao/modelo-classificacao.md) e registre o nível no campo `classificacao`.
3. Monte o dicionário de dados a partir de `dicionario/dicionario-de-dados-modelo.csv`.
4. Rode o validador:

```bash
pip install -r requirements.txt
python scripts/validar_metadados.py caminho/para/metadados.yaml
```

5. Passe pelo [checklist FAIR](fair/checklist-fair.md) antes de compartilhar.

O repositório tem um workflow do GitHub Actions que valida as fichas de `metadados/exemplos/` a cada push, para servir de modelo a quem quiser automatizar a checagem no próprio projeto.

## Referências

- Wilkinson, M. D. et al. (2016). *The FAIR Guiding Principles for scientific data management and stewardship*. Scientific Data, 3, 160018.
- DCMI Metadata Terms: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- GO FAIR: https://www.go-fair.org/fair-principles/
- Lei Geral de Proteção de Dados (Lei 13.709/2018).

## Autor

Tarliso Dória, analista de governança e engenharia de dados em Belém, Pará.
[LinkedIn](https://www.linkedin.com/in/tarlisodoria/) · [GitHub](https://github.com/tarlisodoria)

Material independente, sem vínculo com documentos internos de nenhuma instituição. Licença MIT.
