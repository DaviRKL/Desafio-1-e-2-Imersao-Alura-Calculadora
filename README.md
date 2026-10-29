# 🧮 Calculadora Gráfica com CustomTkinter

> **Desafios 1 e 2 — Imersão Engenharia de Software**  
> Parceria: **Google** & **Alura**

Aplicação desenvolvida e evoluída durante a imersão com o suporte de Inteligência Artificial (**Google AI Studio** e **Google Antigravity**), englobando desde a concepção inicial até a refatoração, adição de regras de negócio complexas e testes de regressão.

---

## 📌 Sobre os Desafios

### 🔹 Desafio 1: Criando a Aplicação com IA
- **Ferramenta:** Google AI Studio  
- **Objetivo:** Compreender a estrutura básica de um software em Python (variáveis, condicionais e tratamento de eventos) e gerar uma calculadora com as 4 operações básicas (`+`, `-`, `*`, `/`).

### 🔹 Desafio 2: Evoluindo o Projeto com Agentes de IA
- **Ferramenta:** Google Antigravity  
- **Objetivo:** Simular o fluxo real de Engenharia de Software através de 3 etapas:
  1. **Explorar:** Mapear a arquitetura e responsabilidades dos módulos existentes.
  2. **Evoluir:** Implementar o suporte completo a cálculos percentuais (`%`).
  3. **Testar:** Validar cenários de borda e garantir ausência de regressões nas funções anteriores.

---

## 🛠️ Tecnologias

- **Python 3.x**
- **CustomTkinter** (UI em Dark Mode)
- **Módulo `re`** (Expressões Regulares para parsing de expressões com porcentagem)
- **Google AI Studio & Google Antigravity** (Assistência agêntica e geração de código)

---

## 🎨 Funcionalidades

- **Operações Fundamentais:** Adição (`+`), Subtração (`-`), Multiplicação (`*`) e Divisão (`/`).
- **Cálculo Percentual Avançado (`%`) — *[Desafio 2]*:**
  - `50%` $\rightarrow$ `0.5` *(Conversão direta)*
  - `200 + 10%` $\rightarrow$ `220` *(Acréscimo)*
  - `200 - 15%` $\rightarrow$ `170` *(Desconto)*
  - `200 * 10%` $\rightarrow$ `20` *(Fração)*
  - `50 / 10%` $\rightarrow$ `500` *(Divisão percentual)*
- **Utilitários:** Limpar visor (`C`), Apagar último caractere (`⌫`) e Inversão de sinal (`±`).
- **Tratamento de Erros:** Prevenção contra divisão por zero (`/0`) e mensagens de sintaxe inválida.

---

## 🚀 Como Executar

```bash
# 1. Clonar o repositório
git clone [https://github.com/DaviRKL/Desafio-1-Imersao-Alura-Calculadora.git](https://github.com/DaviRKL/Desafio-1-Imersao-Alura-Calculadora.git)
cd Desafio-1-Imersao-Alura-Calculadora

# 2. Instalar dependências
pip install customtkinter

# 3. Executar
python calculadora.py
