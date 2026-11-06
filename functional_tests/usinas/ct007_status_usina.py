"""
CT007 — Ativação e inativação de usina
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Verificar troca entre os estados ativo e inativo com confirmação
         e registro temporal do evento.
Requisito: RF 1.6.4 (#24159).
Referências: CA01–CA02 (#24300, #24301); US #24305 e #25855.
Ator: Usuário que acessa a função de gerenciamento/edição de usinas
      (permissão a esclarecer).
Pré-condições: Usina A existente; status atual conhecido.

DADOS DE TESTE
- Usina A: status inicial "ativo"; destino "inativo"; retorno "ativo".

[FP] FLUXO PRINCIPAL
1. Acessar edição/gerenciamento da usina A e selecionar alteração de status.
   Esperado: opção de escolher entre "Ativo" e "Inativo" (US #24305).
2. Selecionar "Inativo" e confirmar.
   Esperado: status da usina atualizado; data e hora da alteração
   registradas; mensagem "Status da usina atualizado com sucesso!".
3. Reabrir a informação de status da usina.
   Esperado: usina consta como inativa (CA01).
4. Selecionar "Ativo" e confirmar.
   Esperado: status atualizado, data/hora da nova alteração registradas
   e mesma mensagem de sucesso para a transição (CA01 e US #24305).

[FA1] FALHA AO ALTERAR STATUS
- Considerar uma solicitação que não possa ser concluída.
- Esperado: comportamento de erro não previsto; pendente de validação.

[RN] REGRAS DE NEGÓCIO
RN1. Status alterna entre ativo e inativo e gera confirmação em ambos
     os casos (CA01).
RN2. Cada mudança registra sua data (CA02); a US #24305 especifica
     explicitamente data e hora.

RESULTADOS ESPERADOS
- Estado persistido e mensagem literal de confirmação em ambas as direções;
  informação temporal registrada para cada alteração.

DÚVIDAS PARA STAKEHOLDERS
- Que permissões habilitam a mudança? Onde verificar o histórico temporal?
- Inativação afeta rateios, vínculos ou operação da usina? O PDF não determina.
Estado: PARCIALMENTE ESPECIFICADO (efeitos colaterais e acesso).
"""
