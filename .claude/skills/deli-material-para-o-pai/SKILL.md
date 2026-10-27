---
name: deli-material-para-o-pai
description: Produz material que João leva ao pai (Eduardo) ou imprime: resumo de uma página, lista de pendências, roteiro curto, tabela para preencher à mão, em PDF A4 limpo e sem nenhuma menção a IA. Use quando João disser "faz para imprimir", "versão em PDF", "algo para levar para meu pai", "uma folha para ele ver", "resume para ele".
---

# Material para o pai

## Regras do conteúdo
- **Uma página sempre que possível.** Mais que duas, cortar.
- Linguagem de dono de construtora: direta, sem jargão de marketing, sem termos em inglês, sem "processo", "sistema", "framework".
- **Nenhuma menção a IA, Claude, harness, GitHub.** O material é de João.
- Começa pelo que interessa a ele (a urgência dele), não pelo que João quer propor.
- Sem dado sensível de terceiros (CPF, salário). Valores da empresa só se João pedir.
- Espaço para ele escrever à mão quando for pergunta ou lista para preencher.

## Como gerar o PDF
1. Escreva o conteúdo em Markdown em `00_GESTAO/` ou na pasta da área (`#` título, `##` blocos, `1.` perguntas, `-` listas, `**negrito**`).
2. Gere o HTML de impressão: `python3 .claude/scripts/gerar_impressao.py ARQUIVO.md ARQUIVO.html` (no Windows: `python`). Linhas para anotar saem embaixo de cada item numerado; use `--sem-linhas` para resumo e `--linhas=2` para caber em uma página.
3. PDF:
   - Onde houver Playwright (sessão na nuvem): `node .claude/scripts/html_para_pdf.js ARQUIVO.html ARQUIVO.pdf` (com `NODE_PATH=$(npm root -g)` se precisar).
   - No Dell: abrir o HTML no Edge ou Chrome → Ctrl+P → "Salvar como PDF".
4. **Confira o visual** antes de entregar: renderize a primeira página em imagem e olhe (quebra de página, número cortado, texto apertado).
5. O PDF não leva o HTML para o git; só o `.md` e o `.pdf`. Salve com `deli-registrar`.
