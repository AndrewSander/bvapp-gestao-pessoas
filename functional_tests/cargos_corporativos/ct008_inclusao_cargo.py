"""
CT008 — Inclusão de cargo corporativo
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Delimitar o cadastro de cargo corporativo mencionado no OpenProject,
         sem inventar campos obrigatórios ou validações ausentes no PDF.
Requisito: RF 1.10.1 (#25939).
Referência: US #25944 (Cadastro de novo Cargo).
Ator: Usuário autorizado a cadastrar cargos (perfil a definir).
Pré-condições: Acesso à funcionalidade de cadastro de cargos; condições
                e permissões ainda não documentadas.

DADOS DE TESTE
- <cargo_novo> é um identificador ilustrativo; atributos obrigatórios,
  formato e valores permitidos dependem de validação dos stakeholders.

[FP] FLUXO PRINCIPAL — PROPOSTA PARA REFINAMENTO
1. Acessar a funcionalidade "Cadastro de novo Cargo" (US #25944).
   Esperado: acesso/entrada da funcionalidade; forma de apresentação pendente.
2. Informar os atributos de <cargo_novo> que vierem a ser homologados.
   Esperado: **PENDENTE**; o PDF não fornece lista de campos nem restrições.
3. Solicitar a inclusão do cargo.
   Esperado: **PENDENTE**; persistência, confirmação e validações não estão
   definidas por critérios de aceitação.

[FA1] ENTRADA INVÁLIDA
- Tentar incluir um cargo com um campo a ser definido como inválido.
- Esperado: não definido; não presumir obrigatoriedade, unicidade ou mensagem.

[RN] REGRAS DE NEGÓCIO
RN1. A Feature 1.10.1 e a US #25944 preveem cadastro de novo cargo.
RN2. Não existem CA detalhados no PDF para essa Feature.

RESULTADOS ESPERADOS
- Resultado definitivo NÃO ESPECIFICÁVEL no estado atual; a ficha identifica
  os pontos que precisam ser aprovados para futuramente testar o cadastro.

DÚVIDAS PARA STAKEHOLDERS
- Quais campos, obrigatoriedade, unicidade e formato? Qual perfil cadastra?
- O que representa sucesso, falha e persistência do cargo no sistema?
Estado: PARCIALMENTE ESPECIFICADO (aguarda requisitos verificáveis).
"""
