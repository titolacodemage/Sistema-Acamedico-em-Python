# Sistema Acadêmico - Gestão de Disciplinas e Notas



Este projeto foi desenvolvido como parte das atividades acadêmicas do curso de **Análise e Desenvolvimento de Sistemas**. Trata-se de uma aplicação de console em Python projetada para gerenciar o desempenho estudantil, permitindo o cadastro de múltiplas disciplinas, validação de dados de entrada, cálculo de médias e análise de frequência.

---

##  Funcionalidades do Sistema

* **Cadastro Dinâmico:** O usuário define quantas disciplinas deseja cadastrar no início da execução.
* **Validação de Dados Estrita:** Garante que notas inválidas (fora do intervalo de 0 a 10) ou frequências incorretas (fora de 0% a 100%) não quebrem o sistema.
* **Tratamento de Erros (Try/Except):** Impede que o programa feche inesperadamente caso o usuário digite letras em campos numéricos.
* **Lógica de Decisão Avançada:** Avalia o aluno com base em dois critérios simultâneos (Média $\ge$ 6.0 e Presença $\ge$ 75%).
* **Relatório Final Formatado:** Exibe uma tabela organizada no terminal com o resumo do semestre e a **Média Geral** do estudante.

---

##  Conceitos de Programação Aplicados

Durante o desenvolvimento deste projeto, foram colocados em prática conceitos fundamentais de desenvolvimento de software:

1. **Modularização:** Divisão do código em funções de responsabilidade única (`calcular_nota_disciplina`, `verificar_situacao`, `cadastrar_disciplinas`, `gerar_relatorio_final`).
2. **Estruturas de Dados:** Uso de **Listas** e **Dicionários** para armazenar e manipular os dados de forma estruturada.
3. **Estruturas de Repetição e Condicionais:** Uso de laços `for` e `while` combinados com blocos `if/elif/else`.
4. **Clean Code:** Código limpo, identado e documentado com *docstrings*.

---

##  Regras de Negócio do Sistema

| Critério | Condição | Resultado |
| :--- | :--- | :--- |
| **Aprovação** | Média $\ge$ 6.0 **E** Presença $\ge$ 75% | `APROVADO` |
| **Reprovação por Falta** | Presença $<$ 75% | `REPROVADO POR FALTA` |
| **Reprovação por Nota** | Média $<$ 6.0 **E** Presença $\ge$ 75% | `REPROVADO POR NOTA` |

---

##  Como Executar o Projeto

### Pré-requisitos
Você precisa ter o **Python 3.x** instalado na sua máquina.

### Passo a Passo
1. Clone este repositório para a sua máquina local:
```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
