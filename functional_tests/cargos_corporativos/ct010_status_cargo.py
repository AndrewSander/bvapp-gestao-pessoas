"""
CT010 — Alteração de status de cargo corporativo
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Especificar a funcionalidade anunciada para alteração de status
         de cargo e registrar o que falta para determinar seu resultado.
Requisito: RF 1.10.4 (#25942).
Referência: US #25949 (Alteração de status ao Cargo).
Ator: Usuário com permissão de gerenciamento de cargos (perfil indefinido).
Pré-condições: Cargo C cadastrado; estados válidos e permissões pendentes.

DADOS DE TESTE
- <cargo_existente>, <status_atual>, <novo_status_autorizado>.
- Os valores "ativo/inativo" NÃO são exigidos aqui porque não foram
  definidos para cargos no PDF (embora existam para outras entidades).

[FP] FLUXO PRINCIPAL — PROPOSTA PARA REFINAMENTO
1. Localizar o cargo e acessar a função de alteração de status (US #25949).
   Esperado: acesso e interface ainda não especificados.
2. Selecionar um estado de destino que venha a ser definido em requisito.
   Esperado: **PENDENTE**; domínio de estados e transições indefinido.
3. Confirmar a alteração de status.
   Esperado: **PENDENTE**; persistência, mensagem e efeitos não documentados.
4. Reabrir o registro e examinar o status.
   Esperado: **PENDENTE**; critério verificável não foi homologado.

[FA1] ALTERAÇÃO NÃO PERMITIDA
- Solicitar uma transição que a regra futura venha a vedar.
- Esperado: não especificado; não inventar bloqueio nem texto de erro.

[RN] REGRAS DE NEGÓCIO
RN1. A Feature 1.10.4 e a US #25949 registram a existência da operação.
RN2. Estados aceitos, autorização e efeito sobre vínculos não constam no PDF.

RESULTADOS ESPERADOS
- Resultado funcional definitivo pendente de decisão dos stakeholders.

DÚVIDAS PARA STAKEHOLDERS
- Quais estados e transições são permitidos? Quem altera?
- Cargos já atribuídos a cooperados são afetados? Como exibir êxito e erros?
Estado: PARCIALMENTE ESPECIFICADO (falta detalhamento de CA e US).
"""
