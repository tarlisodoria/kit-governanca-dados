# Checklist FAIR

Para cada item, marque se o seu conjunto de dados atende. Não é preciso atender tudo de uma vez: comece pelos itens de **Localizável**, que dão o maior ganho com o menor esforço.

## F: Localizável (Findable)

- [ ] O conjunto tem um identificador persistente (DOI, handle ou caminho estável no repositório institucional).
- [ ] Existe uma ficha de metadados preenchida ([modelo](../metadados/dublin-core-modelo.yaml)).
- [ ] A ficha cita o identificador do próprio conjunto.
- [ ] O conjunto está registrado em um catálogo ou repositório pesquisável.

## A: Acessível (Accessible)

- [ ] Está claro como pedir acesso, mesmo quando o dado é restrito.
- [ ] O acesso usa protocolo aberto e padrão (HTTPS, SFTP, API documentada).
- [ ] Os metadados continuam disponíveis mesmo se o dado for removido ou embargado.
- [ ] O nível de [classificação](../classificacao/modelo-classificacao.md) está definido.

## I: Interoperável (Interoperable)

- [ ] O arquivo está em formato aberto (CSV, NetCDF, GeoTIFF, Parquet) e não só em formato proprietário.
- [ ] As colunas usam unidades e nomes descritos em um [dicionário de dados](../dicionario/dicionario-de-dados-modelo.csv).
- [ ] As palavras-chave vêm de vocabulário controlado quando existe um para a área.
- [ ] Os metadados apontam para dados, artigos ou projetos relacionados.

## R: Reutilizável (Reusable)

- [ ] Há uma licença de uso explícita (ex.: CC BY 4.0).
- [ ] A descrição explica como o dado foi coletado e processado (proveniência).
- [ ] O dado segue padrões da comunidade da área, quando existem.
- [ ] Existe uma citação recomendada.

## Como pontuar

Conte os itens marcados em cada letra (0 a 4). Um conjunto com pelo menos 3 em cada letra já está em boa situação para ser compartilhado. Abaixo de 2 em qualquer letra, priorize essa letra antes de divulgar.
