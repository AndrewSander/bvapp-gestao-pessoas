"""
CT003 — Atribuição e alteração de cargos de um cooperado
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Descrever as operações anunciadas nas histórias de usuário de
         associação de cargos e indicar o que falta para torná-las testáveis.
Requisito: RF 1.2.5 (#25943).
Referências: US #25950 (atribuir), #25951 (alterar), #28373 (visualização).
Ator: Usuário responsável pela gestão de cargos (perfil a definir).
Pré-condições: Cooperado A existente; cargo corporativo C existente;
                permissões de acesso ainda não especificadas.

DADOS DE TESTE
- <cooperado_existente>, <cargo_existente>, <outro_cargo_existente>.
- Valores usados apenas para descrever entradas possíveis, sem fixar
  cardinalidade, cargo elegível nem vigência não documentadas.

[FP] FLUXO PRINCIPAL — ETAPAS A ESPECIFICAR
1. Selecionar um cooperado existente na funcionalidade de atribuição.
   Esperado: possibilidade de identificar o cooperado; interface exata pendente.
2. Indicar um cargo e solicitar sua atribuição (US #25950).
   Esperado: **PENDENTE**. Não há critérios que determinem validações,
   sucesso, persistência ou se múltiplos cargos são permitidos.
3. Solicitar alteração do cargo atribuído (US #25951).
   Esperado: **PENDENTE**. Não está definido se substitui, adiciona,
   encerra ou preserva vínculo anterior.
4. Consultar o resultado pela visualização de cargos (US #28373).
   Esperado: **PENDENTE**. Os campos de saída não constam no PDF.

[FA1] TENTATIVA DE ATRIBUIÇÃO REPETIDA (alternativo ao passo 2)
- Solicitar novamente o mesmo vínculo cooperado/cargo.
- Esperado: comportamento não especificado; registrar para validação.

[FA2] ALTERAÇÃO PARA CARGO INATIVO (alternativo ao passo 3)
- Solicitar associação a um cargo considerado inativo, se esse estado existir.
- Esperado: comportamento não especificado; não pressupor bloqueio.

[RN] REGRAS DE NEGÓCIO
RN1. As histórias #25950/#25951 preveem atribuir e alterar cargos.
RN2. A história #28373 prevê apresentação visual do vínculo.
RN3. Não há CA no PDF que determine cardinalidade ou efeito da alteração.

RESULTADOS ESPERADOS
- Não é possível determinar um oráculo de teste definitivo para a criação,
  alteração ou exibição do vínculo antes da validação dos stakeholders.

DÚVIDAS PARA STAKEHOLDERS
- Quem pode atribuir? Quantos cargos por cooperado? Quais estados e vigência?
- Como tratar cargo repetido, inativo e cargo anterior? Quais dados aparecem?

[SUGESTÃO DE FLUXO E CRITÉRIOS DE ACEITAÇÃO — PENDENTE DE VALIDAÇÃO]

Fluxo sugerido:
- Selecionar um cooperado e um cargo disponível, realizar a atribuição e
  conferir o vínculo na consulta. Na alteração, selecionar outro cargo e
  verificar o vínculo atualizado.

Critérios sugeridos:
- CA-S1: Impedir novas atribuições a cooperados ou cargos inativos.
- CA-S2: Evitar atribuições duplicadas do mesmo cargo ao mesmo cooperado.
- CA-S3: Definir a cardinalidade dos vínculos; como proposta inicial, avaliar
  um cargo ativo por cooperado, com substituição explícita na alteração.

Pendente: validar se múltiplos cargos simultâneos são permitidos e como os
          vínculos anteriores devem ser tratados.

Estado: PARCIALMENTE ESPECIFICADO (US apenas com títulos no PDF).
"""
