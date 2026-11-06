"""
CT002 — Alteração de status de cooperado
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Verificar a alteração entre ativo e inativo e o impedimento de
         selecionar cooperado inativo em novos vínculos.
Requisito: RF 1.2.4 (#23992).
Referências: CA01–CA04 (#23998, #24000, #24001, #24007);
             US #24006 e #25845.
Ator: Usuário autenticado com autorização (perfil não identificado no PDF).
Pré-condições: Cooperado A cadastrado e inicialmente ativo;
                usuário com acesso à edição de status.

DADOS DE TESTE
- Cooperado A existente; <usuario_responsavel>; status destino "inativo";
  status posterior "ativo".

[FP] FLUXO PRINCIPAL
1. Acessar a edição do status do cooperado A.
   Esperado: registro selecionado para alteração.
2. Selecionar "inativo" e acionar "Salvar".
   Esperado: status passa a inativo; sistema registra data e usuário
   responsável (CA01, CA03, CA04).
3. Iniciar a criação de um novo vínculo/associação e tentar selecionar
   o cooperado A, agora inativo.
   Esperado: cooperado A não pode ser selecionado (CA02).
4. Retornar à edição de status e selecionar "ativo"; salvar.
   Esperado: status volta a ativo e o evento registra data e responsável.

[FA1] COOPERADO INATIVO EM NOVO VÍNCULO (alternativo ao passo 3)
- Se a interface exibir o cooperado inativo como opção, tentar confirmá-lo.
- Esperado: não permitir sua seleção para novo vínculo; a forma de bloqueio
  (ocultar, desabilitar, mensagem) não foi definida.

[RN] REGRAS DE NEGÓCIO
RN1. Status permitido no requisito: ativo ou inativo (CA01).
RN2. Inativos não podem ser selecionados em novos vínculos (CA02).
RN3. Cada alteração registra data e usuário responsável (CA03/CA04).

RESULTADOS ESPERADOS
- Status refletido após salvar; cooperado inativo indisponível para novos
  vínculos; registros de data e responsável existentes.

DÚVIDAS PARA STAKEHOLDERS
- Quais vínculos específicos são abrangidos pelo CA02?
- O que acontece com vínculos previamente existentes? Não presumir exclusão.
- Qual perfil pode alterar o status e onde consultar os metadados de auditoria?
Estado: PARCIALMENTE ESPECIFICADO (permissões e efeitos de vínculos anteriores).
"""
