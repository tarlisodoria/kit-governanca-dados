# Modelo de classificação da informação

Quatro níveis, do mais aberto ao mais restrito. Na dúvida entre dois níveis, use o mais restrito e revise depois com o responsável pelo dado.

| Nível | Quem pode acessar | Exemplos em pesquisa | Tratamento mínimo |
|---|---|---|---|
| **Público** | Qualquer pessoa | Dados já publicados em artigo, bases abertas de governo, metadados de catálogo | Licença de uso definida (ex.: CC BY 4.0) e citação recomendada |
| **Interno** | Colaboradores da instituição | Dados brutos de campo ainda não publicados, planilhas de controle de projeto | Armazenamento institucional, sem compartilhamento por link aberto |
| **Restrito** | Equipe do projeto, nominalmente | Dados sob acordo de cooperação, sequências genéticas com patente em análise, localização de espécies ameaçadas | Lista de acesso nominal, revisão periódica dos acessos, registro de quem baixou |
| **Confidencial** | Pessoas autorizadas pelo responsável e pelo encarregado de dados | Dados pessoais sensíveis (LGPD art. 5º, II), dados de saúde de participantes, informação contratual sigilosa | Anonimização ou pseudonimização quando possível, criptografia em repouso, base legal documentada |

## Perguntas para decidir o nível

Responda na ordem. A primeira resposta "sim" define o nível.

1. O conjunto tem dado pessoal sensível ou dado protegido por contrato de sigilo? **Confidencial.**
2. A divulgação pode causar dano ambiental, financeiro ou violar um acordo com parceiro? **Restrito.**
3. O dado ainda não foi publicado ou validado pela equipe? **Interno.**
4. Nenhuma das anteriores. **Público.**

## Quando reclassificar

- Na publicação do artigo ou relatório que usa o dado (normalmente Interno vira Público).
- No fim de um acordo de cooperação ou de um período de embargo.
- Quando o dado é anonimizado de forma irreversível.
- Em revisão anual, junto com a revisão dos acessos.

## Campo na ficha de metadados

Registre o nível no campo `classificacao` da [ficha Dublin Core](../metadados/dublin-core-modelo.yaml), usando exatamente um destes valores: `publico`, `interno`, `restrito`, `confidencial`.
