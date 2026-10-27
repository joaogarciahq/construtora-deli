---
name: deli-registrar
description: Grava no hub da Construtora DELI o que foi decidido, aprendido ou descoberto, sempre por acréscimo, e salva no GitHub (commit e push) para chegar ao Dell e ao Projeto do claude.ai. Use ao fim de toda tarefa que mudou arquivo, quando João disser "ficou decidido", "decidi que", "anota isso", "o certo é", "salva", e quando ele corrigir um dado do cadastro.
---

# Registrar e salvar

## Onde vai cada coisa
| O quê | Arquivo |
|---|---|
| Decisão (o quê, quem, por quê) | `00_GESTAO/REGISTRO_DE_DECISOES.md`, uma linha, acréscimo |
| Dado da empresa | `00_GESTAO/CADASTRO_DA_EMPRESA.md`, reescrevendo a linha no presente, com a data |
| Prioridade, o que está parado | `00_GESTAO/PAINEL.md` |
| Situação de uma área | o diagnóstico ou retrato da área (`01_` a `04_`) |
| Regra oficial pesquisada | `00_GESTAO/REGRAS_OFICIAIS.md`, com link e data |
| Regra permanente de como trabalhar | `CLAUDE.md`, só com o ok explícito de João |

## Regras
- Nunca apagar: o que sai de uso vai para `99_ARQUIVO/`.
- Decisão do pai é registrada como dele; de João, como de João.
- **Antes do commit**, confira que nada sensível entrou: `git diff --cached` sem CPF, RG, número de conta, salário. O hook `bloquear_dado_sensivel.py` também barra CPF.
- Dado sensível vai para `_SENSIVEL/` (fora do git).

## Salvar
```bash
git add -A
git commit -m "<área>: <o que mudou em poucas palavras>"
git push origin main
```
Depois confira com `git ls-remote origin main` que o commit chegou, e diga a João em uma linha o que foi salvo. No Dell, ele traz as mudanças com `git pull`; no Projeto do claude.ai, com o botão de sincronizar.
