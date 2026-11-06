"""
CT006 — Atualização cadastral de usina e registro da modificação
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Verificar alterações válidas de dados de usina, preservação dos
         campos obrigatórios e registro da última atualização.
Requisito: RF 1.6.3 (#24158).
Referências: CA01–CA03 (#24287, #24288, #24290);
             US #24293 e #24295.
Ator: Usuário com acesso à edição de usinas (permissão concreta pendente).
Pré-condições: Usina A existente e identificável na funcionalidade de edição.

DADOS DE TESTE
- Usina A com nome "Usina Solar A" e endereço "Rua X".
- Alteração de exemplo: nome "Usina Solar A - Revisada".
- O exemplo só se aplica se nome estiver entre os campos editáveis
  autorizados; a lista completa de campos editáveis não está definida.

[FP] FLUXO PRINCIPAL
1. Acessar a tela de edição de uma usina previamente cadastrada.
   Esperado: registro identificado para alteração (US #24293).
2. Alterar um campo permitido, mantendo nome, endereço, potência
   instalada e status preenchidos; acionar "Salvar Alterações".
   Esperado: verificação da presença dos quatro campos obrigatórios.
3. Concluir a atualização válida.
   Esperado: dados persistidos, nova data de modificação registrada e
   mensagem "Dados da usina atualizados com sucesso!" (US #24293;
   CA01 com redação editorial revisada).

[FA1] REMOÇÃO DE CAMPO OBRIGATÓRIO (alternativo ao passo 2)
- Apagar valor de um campo obrigatório e tentar salvar.
- Esperado: não se pode concluir atualização que deixe obrigatório vazio
  (CA02); apresentação de erro/mensagem ainda não detalhada nesta RF.

[FA2] EDIÇÃO DE CAMPO NÃO CONFIRMADO (alternativo ao passo 2)
- Caso o campo escolhido não conste da lista autorizada homologada,
  não afirmar que a operação deve ser aceita; suspender esse passo até
  definição dos campos editáveis.

[RN] REGRAS DE NEGÓCIO
RN1. Atualizar dados de usina é permitido (CA01), respeitando campos editáveis.
RN2. Os quatro campos obrigatórios permanecem preenchidos (CA02/US #24293).
RN3. Última atualização cadastral é registrada (CA03).
RN4. A mensagem de sucesso é a especificada na US #24293.

RESULTADOS ESPERADOS
- Atualização válida observável, campos obrigatórios mantidos e
  registro temporal da alteração.

DÚVIDAS PARA STAKEHOLDERS
- Quais campos podem mudar e quais perfis estão autorizados?
- Onde comprovar a data da última atualização? Como tratar usina inexistente?
Estado: PARCIALMENTE ESPECIFICADO (campos editáveis e exceções).
"""
