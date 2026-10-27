# Construtora DELI · Harness

> A constituicao do projeto. So o que e permanente e onde buscar o resto.
> Estado do dia mora no `00_GESTAO/PAINEL.md`. Decisoes, no `00_GESTAO/REGISTRO_DE_DECISOES.md`.

## 1. O negocio

Construtora de **casas e apartamentos em Itaitinga (CE)**, com foco em **clientes de baixa renda** no programa federal **Minha Casa Minha Vida (MCMV)**.

- **Dono:** o pai de Joao. E quem decide sobre a empresa.
- **Sucessao:** Joao e duas irmas sao herdeiros. Joao esta aprendendo todas as areas e tem potencial de liderar.
- **Joao:** conduz a organizacao da empresa, por pedido do pai.
- **Leiloes** e outro negocio. Nao entra neste repositorio.

## 2. O plano, em fases

1. **Fase 1 (agora):** organizar **Contabilidade, Financeiro, Compras e Administrativo**.
2. **Fase 2 (depois):** **Obras** e **Vendas**.

Nada da fase 2 comeca antes de a fase 1 estar de pe, salvo decisao explicita de Joao.

**Metodo por area:** primeiro o retrato de hoje (quem faz, com que ferramenta, onde estao os documentos, quanto tempo leva, onde trava), depois a proposta, depois a mudanca. Nunca mudar processo que ainda nao foi mapeado.

## 3. Governanca

- Claude pesquisa, analisa e recomenda. **Joao decide.** Decisao que muda a empresa (dinheiro, pessoas, fornecedor, contrato) **passa pelo pai** antes de executar.
- Diante de varias opcoes: comparar e dizer qual e a melhor.
- **Nunca inventar** numero, prazo, regra do MCMV ou dado da empresa. Sem fonte, dizer que nao sabe.
- Regra do MCMV (faixas, renda, subsidio, Caixa) muda: sempre confirmar na fonte oficial e registrar a data.
- Nunca tratar como concluido o que nao foi feito.

## 4. Separacao total do MPA

Este projeto **nao tem relacao** com o Curso Marta Garcia / MPA. Nenhuma regra, skill, hook, numero ou contexto do MPA vale aqui, e nada daqui vai para la.

## 5. Dados sensiveis (LGPD)

CPF, RG, renda, extratos, contratos de clientes e de funcionarios **nao entram no git**. Ficam em `_SENSIVEL/`, que o `.gitignore` exclui. No repositorio vai so o processo, o modelo e o resumo.

## 6. Onde fica cada coisa

- `00_GESTAO/` painel, decisoes, pendencias de cadastro
- `01_CONTABILIDADE/` · `02_FINANCEIRO/` · `03_COMPRAS/` · `04_ADMINISTRATIVO/` (fase 1)
- `05_OBRAS/` · `06_VENDAS/` (fase 2)
- `99_ARQUIVO/` o que saiu de uso. Nunca apagar, arquivar.
- `_SENSIVEL/` fora do git

## 7. A preencher (Joao)

Ver `00_GESTAO/CADASTRO_DA_EMPRESA.md`. Enquanto estiver em branco, Claude pergunta, nao supoe.
