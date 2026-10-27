---
name: deli-diagnostico-contabil
description: Monta e atualiza o diagnóstico da contabilidade da Construtora DELI: regime de imposto, impostos e INSS em atraso, certidões negativas, documentos que não chegaram ao contador, prazo mensal e a urgência do pai, com status por item e um plano de ação curto. Use quando João disser "como está a contabilidade", "o que falta resolver", "faz o diagnóstico", "atualiza o diagnóstico", ou trouxer resposta do pai ou do contador sobre a contabilidade.
---

# Diagnóstico da contabilidade

Arquivo vivo: `01_CONTABILIDADE/DIAGNOSTICO.md`. Crie se não existir, com a estrutura abaixo; depois, só atualize.

## Os 8 itens (sempre esta ordem)

| # | Item | Pergunta que responde |
|---|---|---|
| 1 | Urgência do pai | O que, nas palavras dele, precisa ser resolvido? |
| 2 | Escritório de contabilidade | Quem é, quem é o contato, se responde e entrega. |
| 3 | Regime tributário | Simples, Presumido ou Real; usa RET ou patrimônio de afetação. |
| 4 | Impostos e guias | Algo atrasado ou parcelado? Quanto, desde quando. |
| 5 | INSS e folha de obra | CNO das obras, eSocial e DCTFWeb em dia? |
| 6 | Certidões negativas | Federal, INSS, FGTS, estadual, municipal: em dia ou travada, e por quê. |
| 7 | Documentos pendentes | Que meses de notas e extratos não chegaram ao contador. |
| 8 | Rotina mensal | Data em que o contador precisa receber os papéis, e quem envia. |

Cada item tem: **status** (🔴 problema · 🟡 sem informação · 🟢 resolvido), **o que se sabe** (com fonte: quem disse, quando, qual papel), **próximo passo** (um só, com quem faz).

## Como rodar
1. Leia o diagnóstico atual, `00_GESTAO/CADASTRO_DA_EMPRESA.md` e o que João trouxe.
2. Atualize só o que a informação nova muda. Nunca troque 🟡 por 🟢 sem fonte.
3. Regra legal envolvida: chame o agente `pesquisador-regras` antes de afirmar.
4. No topo do arquivo, mantenha **"Para resolver a urgência do pai, falta:"** com no máximo 3 linhas. É isso que João leva ao pai.
5. Atualize a prioridade em `00_GESTAO/PAINEL.md` se mudou.
6. Salve com a skill `deli-registrar` (commit e push).
7. Responda a João: o que mudou, o que falta, o próximo passo. Sem repetir o arquivo inteiro.
