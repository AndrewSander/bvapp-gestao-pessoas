"""
CT004 — Inclusão de usina e validação de duplicidade
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Especificar cadastro de usina com campos conhecidos e rejeição
         de registros com mesmo par nome/endereço, conforme as histórias.
Requisito: RF 1.6.1 (#24155).
Referências: CA01–CA05 (#24161, #24163, #24164, #24165, #24167);
             US #24179, #24188, #25837.
Ator: Usuário que acessa cadastro de usinas; permissão específica pendente.
Pré-condições: Cooperativa de referência já cadastrada; dados não duplicados.

DADOS DE TESTE
- Usina A: nome "Usina Solar A", endereço "Rua X", potência <potencia>,
  status "ativo" (escolhido explicitamente; não é afirmado como padrão).
- Opcionais: <data_instalacao> e <descricao>.
- Usina duplicada: mesmo nome "Usina Solar A" e mesmo endereço "Rua X".

[FP] FLUXO PRINCIPAL
1. Acessar cadastro de usinas e conferir a disponibilidade dos campos
   nome, endereço, potência instalada, status e opcionais previstos em CA03.
   Esperado: formulário destinado à inclusão de usinas (US #25837 revisada).
2. Informar valores não duplicados e acionar "Salvar".
   Esperado: validação dos campos obrigatórios e do par nome/endereço.
3. Concluir o cadastro válido.
   Esperado: usina salva, associada automaticamente à cooperativa cadastrada;
   mensagem "Usina <nome_usina> cadastrada com sucesso!" (US #24179).

[FA1] CAMPOS OBRIGATÓRIOS VAZIOS (alternativo ao passo 2)
- Omitir nome, endereço, potência instalada ou status; salvar.
- Esperado: não cadastrar; emitir erro e destacar campos vazios (CA02).

[FA2] NOME E ENDEREÇO IGUAIS A OUTRA USINA (alternativo ao passo 2)
- Usar o mesmo nome E endereço de usina já cadastrada e tentar salvar.
- Esperado: alerta e mensagem literal da US #24188:
  "Erro: Já existe uma usina cadastrada com este nome neste endereço."

[RN] REGRAS DE NEGÓCIO
RN1. Campos obrigatórios: nome, endereço, potência instalada, status (CA01).
RN2. Campos opcionais: data de instalação e descrição (CA03).
RN3. Associação automática à cooperativa (CA04).
RN4. O par repetido é rejeitado conforme US #24179/#24188;
     CA05 é ambíguo sobre repetição isolada do nome ou do endereço.

RESULTADOS ESPERADOS
- Cadastro válido persistido com vínculo institucional e mensagem prevista.
- Cadastro com campo ausente ou mesmo par nome/endereço rejeitado.

DÚVIDAS PARA STAKEHOLDERS
- Um nome igual em endereço diferente é permitido? E endereço igual com
  nome diferente? O backend observado usa regra mais restritiva.
- Unidade e limites da potência, permissão de cadastro e prova da associação?
Estado: PARCIALMENTE ESPECIFICADO (unicidade para repetição isolada pendente).
"""
