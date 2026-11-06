"""
CT001 — Manutenção de cooperados (CRUD)
Autor: Andrew Sander Felix de Aragão Pinheiro
Objetivo: Especificar, em um único fluxo, cadastro, consulta, atualização e
         a etapa de exclusão de um cooperado, sem presumir regra não documentada.
Requisitos: RF 1.2.1 (#23871), RF 1.2.2 (#23900), RF 1.2.3 (#23960).
Referências: CA01–CA05 de 1.2.1 (#23874, #23880, #23883, #23885, #25275);
             CA01–CA03 de 1.2.2 (#23902, #23939, #23942);
             CA01–CA06 de 1.2.3 (#23973, #23975, #23977, #23978, #23979, #23980);
             US #23898, #23899, #23945, #23950, #23983, #23988.
Ator: Usuário autenticado e autorizado (qual permissão concede acesso: pendente).
Pré-condições: Cooperativa cadastrada; cooperado de teste ainda inexistente;
                acesso às funcionalidades conforme permissões a definir.

DADOS DE TESTE
- Cooperado A: nome "Cooperado Exemplo A"; <cpf_novo_valido>;
  <data_nascimento>, <profissao>, <endereco>, <cota>, <telefone>,
  <email>, <data_ingresso>.
- Status inicial: ativo, conforme CA01 de cadastro; RG e órgão expedidor opcionais.
- Atualização: nome "Cooperado Exemplo Atualizado" e <email_atualizado>.
- Valores são fictícios/parametrizados; formato de 'cota' e demais validações
  aguardam definição dos stakeholders.

[FP] FLUXO PRINCIPAL — CRIAR, CONSULTAR, ATUALIZAR E EXCLUIR
1. CRIAR: acessar o cadastro de cooperados; informar os campos obrigatórios
   previstos no CA01, sem duplicar CPF; acionar "Salvar".
   Esperado: registro salvo; mensagem "Cooperado <nome> cadastrado com sucesso";
   vínculo automático com a cooperativa cadastrada (CA04).
2. CONSULTAR: abrir a listagem de cooperados e localizar o registro recém-criado
   pelo nome/CPF; acessar seus dados.
   Esperado: o registro aparece na lista e pode ser identificado por nome,
   CPF/CNPJ e status, conforme US #23945 e #25841.
3. ATUALIZAR: abrir o registro, modificar nome e e-mail preservando os demais
   campos obrigatórios e salvar.
   Esperado: alterações persistem; data da última atualização e usuário
   responsável são registrados (CA05 e CA06 de 1.2.3).
4. EXCLUIR: solicitar a exclusão do registro cadastrado.
   Esperado: **PENDENTE DE VALIDAÇÃO**. As RFs 1.2.1–1.2.3 não estabelecem se
   exclusão é permitida, a quem, de que modo, nem a pós-condição observável.
   Não simular sucesso, remoção, confirmação nem substituir exclusão por inativação.

[FA1] CADASTRO COM DADOS OBRIGATÓRIOS AUSENTES (alternativo ao passo 1)
- Deixar um campo obrigatório sem preenchimento e tentar salvar.
- Esperado: cadastro impedido, erro exibido e campos ausentes destacados (CA02).

[FA2] CADASTRO COM CPF JÁ CADASTRADO (alternativo ao passo 1)
- Utilizar <cpf_ja_cadastrado> e tentar salvar.
- Esperado: registro não criado; mensagem "CPF já usado." (US #23899).

[FA3] ATUALIZAÇÃO INVÁLIDA (alternativo ao passo 3)
- Deixar campo obrigatório vazio ou informar CPF/CNPJ já utilizado por outro
  cooperado e salvar.
- Esperado: atualização não persistida e mensagem de erro conforme US #23988:
  "Campos obrigatórios não preenchidos" ou
  "CPF ou CNPJ já utilizado por outro cooperado".

[RN] REGRAS DE NEGÓCIO
RN1. Os campos obrigatórios e opcionais são os do CA01/CA05 de 1.2.1.
RN2. Não é permitido cadastrar CPF duplicado (CA03 de 1.2.1).
RN3. A inclusão associa o cooperado à cooperativa cadastrada (CA04 de 1.2.1).
RN4. Atualização não pode invalidar os campos obrigatórios nem duplicar
     CPF/CNPJ e deve registrar data e responsável (CA02–CA06 de 1.2.3).

RESULTADOS ESPERADOS
- Cadastro, consulta e atualização verificáveis pelos dados listados e salvos.
- Exclusão: resultado indefinido; cenário CRUD apenas parcialmente especificado.

DÚVIDAS PARA STAKEHOLDERS
- A exclusão existe? É física ou lógica? Quais condições, efeitos e permissão?
- Qual perfil pode criar, consultar, editar e excluir cooperados?
- Significado e formato de "cota"; conflito entre campos do PDF e do código;
  uso de CPF versus CPF/CNPJ e forma de verificar auditoria e vínculo.
Estado: PARCIALMENTE ESPECIFICADO (exclusão e itens acima pendentes).
"""
