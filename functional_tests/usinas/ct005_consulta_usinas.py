"""
CT005 — Consulta, busca por nome e filtragem de usinas
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Verificar apresentação de lista de usinas, pesquisa por nome e
         filtro por status conforme os critérios documentados.
Requisito: RF 1.6.2 (#24156).
Referências: CA01–CA04 (#24201, #24209, #24212, #24231);
             US #24239, #24241, #25836, #28830.
Ator: Usuário da funcionalidade de consulta (permissão a confirmar).
Pré-condições: Existem ao menos duas usinas cadastradas com nomes e status
                conhecidos para o cenário.

DADOS DE TESTE
- Usina A: nome "Usina Solar A", localização "Local A", status "ativo".
- Usina B: nome "Usina Solar B", localização "Local B", status "inativo".
- Termo de busca: "Solar A"; filtro de status: "ativo".

[FP] FLUXO PRINCIPAL
1. Acessar a listagem de usinas.
   Esperado: registros cadastrados exibidos (CA01).
2. Examinar o registro de cada usina.
   Esperado: exibição de pelo menos nome, localização e status
   (CA04, redação editorial revisada).
3. Pesquisar pelo nome "Solar A".
   Esperado: somente usinas cujo nome contenha o termo informado (US #24241).
4. Aplicar filtro de status "ativo" na funcionalidade de filtro.
   Esperado: consulta filtrada por status, como prevê CA03.

[FA1] PESQUISA POR OUTRO NOME (alternativo ao passo 3)
- Informar "Solar B" como termo da pesquisa.
- Esperado: retornar somente nomes que contenham o termo, conforme US #24241.

[FA2] PESQUISA SEM RESULTADOS (alternativo ao passo 3)
- Informar termo inexistente.
- Esperado: formato da tela/mensagem sem resultados não foi especificado;
  não exigir mensagem literal inventada.

[RN] REGRAS DE NEGÓCIO
RN1. Listagem de usinas cadastradas (CA01).
RN2. Busca por nome (CA02; US #24241 fala em "conter" o termo).
RN3. Filtro por status (CA03).
RN4. Exibição mínima de nome, localização e status (CA04 revisado).

RESULTADOS ESPERADOS
- Dados de saída e correspondências de pesquisa coerentes com os critérios.
- A combinação simultânea de busca e filtro não possui regra de precedência
  ou composição suficientemente detalhada: não exigir comportamento extra.

DÚVIDAS PARA STAKEHOLDERS
- Como combinar busca e status? Quais usuários podem consultar?
- Como representar lista vazia? A visualização de cooperados e rateios
  associados (US #28830) requer especificação própria de dados e acesso.
Estado: PARCIALMENTE ESPECIFICADO (combinação de filtros/estados vazios).
"""
