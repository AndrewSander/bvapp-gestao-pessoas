# BVapp — Cenários de Teste de Gestão de Pessoas

**Aluno:** Andrew Sander Felix de Aragão Pinheiro  
**Disciplina:** Verificação e Validação de Testes de Software (VVTS) — IFPB  
**Entrega:** especificação documental, sem implementação ou execução de testes.

## Objetivo

Organizar ** 10 cenários de teste** para as EPICs do OpenProject
**Cadastro de Cooperados (#23541), Cadastro de Usinas (#23545) e
Cadastro de Cargos Corporativos (#25938)**. Cada arquivo `.py` contém somente
uma docstring com objetivo, requisitos, ator, dados, fluxo principal, fluxos
alternativos, regras de negócio, resultados esperados, pendências e autoria.

O formato foi inspirado no exemplo **UC001 — Manter produtos** da Aula 06:
https://raw.githubusercontent.com/maxwellamaral/maxwellamaral.github.io/refs/heads/main/specs/tests/products/UCS001-manter-produtos.py

## Índice de cenários

| Cenário | Tema | Feature(s) OpenProject |
|---|---|---|
| [CT001](functional_tests/cooperados/ct001_manutencao_cooperados_crud.py) | Manutenção de cooperados (CRUD no mesmo cenário) | 1.2.1, 1.2.2, 1.2.3 |
| [CT002](functional_tests/cooperados/ct002_status_cooperado.py) | Alteração de status de cooperado | 1.2.4 |
| [CT003](functional_tests/cooperados/ct003_atribuicao_cargos_cooperado.py) | Atribuição e alteração de cargos ao cooperado | 1.2.5 |
| [CT004](functional_tests/usinas/ct004_cadastro_usina.py) | Inclusão de usina e duplicidade | 1.6.1 |
| [CT005](functional_tests/usinas/ct005_consulta_usinas.py) | Consulta, busca e filtro de usinas | 1.6.2 |
| [CT006](functional_tests/usinas/ct006_atualizacao_usina.py) | Atualização cadastral de usina | 1.6.3 |
| [CT007](functional_tests/usinas/ct007_status_usina.py) | Ativação e inativação de usina | 1.6.4 |
| [CT008](functional_tests/cargos_corporativos/ct008_inclusao_cargo.py) | Inclusão de cargo corporativo | 1.10.1 |
| [CT009](functional_tests/cargos_corporativos/ct009_consulta_atualizacao_cargo.py) | Consulta e atualização de cargo | 1.10.2, 1.10.3 |
| [CT010](functional_tests/cargos_corporativos/ct010_status_cargo.py) | Alteração de status de cargo | 1.10.4 |

**Cobertura:** as 13 Features distribuídas nas três EPICs aparecem em ao
menos um dos 10 cenários. As quatro Features não CRUD (1.2.4, 1.2.5, 1.6.4
e 1.10.4) possuem cenário próprio. Para cumprir o limite de 10 cenários,
consulta e atualização de cargos foram tratadas juntas no CT009.

**Ressalva quanto ao CRUD:** somente CT001 é um cenário de CRUD completo:
contém criação, consulta, atualização e exclusão no mesmo fluxo. A exclusão,
porém, **não está especificada nos requisitos do OpenProject**


## Organização

```text
bvapp_vvts_cenarios_andrew/
├── manage.py                # entrada padrão Django, não utilizada na entrega
├── pyproject.toml            # metadados mínimos, sem necessidade de instalar
├── config/                   # settings, urls, asgi e wsgi: esqueleto Django
├── cooperados/               # app do domínio (sem implementação)
├── usinas/                   # app do domínio (sem implementação)
├── cargos_corporativos/      # app do domínio (sem implementação)
└── functional_tests/         # 10 especificações em docstrings Python
    ├── cooperados/           # CT001–CT003
    ├── usinas/               # CT004–CT007
    └── cargos_corporativos/  # CT008–CT010
```

Os módulos `tests.py` dos apps são **reservas vazias do padrão Django**.
Não foram feitos modelos, banco de dados funcional, templates, views,
endpoints, scripts de automação, testes executáveis nem execução de testes.
**Para avaliar a atividade, basta abrir o README e ler as docstrings**;
não é necessário instalar Django nem executar `manage.py`.
