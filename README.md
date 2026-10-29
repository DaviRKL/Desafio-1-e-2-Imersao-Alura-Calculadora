# 🧮 Calculadora Gráfica com CustomTkinter

> **Desafios 1 e 2 - Imersão Engenharia de Software: Dev na Era da IA**  
> Parceria: **Google** & **Alura**

Projeto desenvolvido e evoluído durante a imersão, utilizando assistência de Inteligência Artificial (**Google AI Studio** no Desafio 1 e **Google Antigravity** no Desafio 2) para projetar, compreender, aprimorar e testar uma calculadora completa em Python com interface gráfica moderna.

---

## 📌 Sobre os Desafios

### 🔹 Desafio 1: Criação da Calculadora com IA
O objetivo do primeiro desafio foi explorar o uso de ferramentas de IA no fluxo de criação de software, compreendendo como instruções, variáveis, estruturas condicionais e tratamento de eventos se articulam na construção de uma aplicação funcional em Python.

**Questões propostas pelo Desafio 1:**
1. **Quais são os principais componentes do código gerado?**
2. **Como a aplicação recebe os números e identifica a operação escolhida?**
3. **Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?**

---

### 🔹 Desafio 2: Evolução e Manutenção com Google Antigravity
No segundo desafio, demos um passo adiante para praticar uma rotina essencial da **Engenharia de Software**: compreender um código existente, implementar melhorias e verificar se tudo continua funcionando sem comprometer o que já existia. Utilizando o **Google Antigravity**, o desafio foi dividido em três atividades:

1. **Explorar o projeto:** Identificar os arquivos e explicar como o código e as funções estão organizados.
2. **Adicionar uma funcionalidade:** Implementar e aprimorar a operação de **cálculo de porcentagem (`%`)** mantendo todas as funcionalidades existentes.
3. **Testar a aplicação:** Verificar se a nova funcionalidade opera corretamente em diferentes cenários sem introduzir regressões nas operações básicas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal do projeto.
- **CustomTkinter** - Biblioteca gráfica baseada em Tkinter para criação de interfaces modernas no modo Dark.
- **Módulo `re` (Regex)** - Biblioteca nativa do Python utilizada para interpretar expressões compostas no cálculo de porcentagem.
- **Google AI Studio** - Plataforma de IA utilizada na concepção inicial do projeto (Desafio 1).
- **Google Antigravity** - Ambiente agêntico de desenvolvimento utilizado para exploração da arquitetura, refatoração da funcionalidade de porcentagem e testes automatizados (Desafio 2).

---

## 🎨 Funcionalidades

- ➕ **Operações Básicas:** Adição (`+`), Subtração (`-`), Multiplicação (`*`) e Divisão (`/`).
- 📊 **Cálculo Completo de Porcentagem (`%`) — *[Desafio 2]*:**
  - **Valor percentual direto:** `50%` → `0.5`
  - **Acréscimo percentual:** `200 + 10%` → `220`
  - **Desconto percentual:** `200 - 15%` → `170`
  - **Multiplicação percentual:** `200 * 10%` → `20`
  - **Divisão percentual:** `50 / 10%` → `500`
- 🎛️ **Recursos Adicionais:** 
  - Limpar visor (`C`).
  - Apagar último caractere (`⌫`).
  - Inversão de sinal positivo/negativo (`±`).
- 🛑 **Validação de Erros:** Tratamento para divisão por zero e sintaxes inválidas.
- 🎨 **Interface Dark Mode:** Design moderno estilizado com `CustomTkinter`.

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado em seu computador.

### Passos:
1. Clone este repositório ou baixe o arquivo do código:
   ```bash
   git clone https://github.com/DaviRKL/Desafio-1-Imersao-Alura-Calculadora.git
   cd Desafio-1-Imersao-Alura-Calculadora
   ```

2. Instale a biblioteca `customtkinter`:
   ```bash
   pip install customtkinter
   ```

3. Execute a aplicação:
   ```bash
   python calculadora.py
   ```

---

## 🧐 Atividade 1: Explicação Técnica e Análise do Código

Para responder às perguntas reflexivas propostas no **Desafio 1**:

### 1. Quais são os principais componentes do código gerado?
* **Classe `Calculadora` (`ctk.CTk`):** Estrutura principal baseada em Programação Orientada a Objetos (POO) que representa a janela da aplicação.
* **Visor (`CTkEntry`):** Campo de texto onde os números e resultados são exibidos (configurado como `readonly` para evitar digitação manual inválida).
* **Grade de Botões (`CTkButton`):** Conjunto de botões mapeados em uma lista de tuplas com suas posições (`linha`, `coluna`) e cores estilizadas.
* **Método `clique_botao(valor)`:** Função central encarregada de capturar as ações do usuário e direcionar para a operação correspondente.
* **Método `calcular_porcentagem()`:** Método dedicado ao processamento de porcentagens isoladas e combinadas com as quatro operações básicas.
* **Método `atualizar_visor(texto)`:** Função auxiliar que gerencia o estado do visor de forma segura (habilita edição, atualiza o texto e retorna para `readonly`).

### 2. Como a aplicação recebe os números e identifica a operação escolhida?
A interface mapeia cada clique de botão via comando `lambda t=texto: self.clique_botao(t)`. 

* Quando um número ou operador é clicado, o caractere correspondente é enviado para o método `clique_botao`.
* O programa concatena o caractere recebido em uma string chamada `self.expressao`.
* **Tratamento de duplicidade de operadores:** Caso o usuário digite dois operadores em sequência (ex.: `5 + *`), o código identifica a duplicidade e substitui o operador anterior pelo novo.

### 3. Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?
* **Processamento:** Ao pressionar `=`, a aplicação limpa e valida a string de expressão contida em `self.expressao`.
* **Cálculo:** Utiliza a função `eval()` dentro de um bloco de proteção `try-except` para interpretar matematicamente a expressão formatada.
* **Tratamento de Exceções:** 
  - Se houver tentativa de divisão por zero (`/0`), é exibida a mensagem `"Erro: Divisão por 0"`.
  - Se a sintaxe for inválida, é exibida a mensagem `"Erro"`.
* **Formatação do Resultado:** O resultado passa por arredondamento de até 8 casas decimais (`round(resultado, 8)`) para evitar ruídos de ponto flutuante e, caso seja inteiro (ex.: `10.0`), é convertido para `int` (`10`) para manter o visor limpo.

---

## 🚀 Atividade 2: Evolução do Projeto com Google Antigravity

Durante o **Desafio 2**, utilizamos o **Google Antigravity** para cumprir as três etapas de engenharia de software propostas:

### 1. Exploração da Estrutura do Projeto
O projeto é organizado de forma enxuta e modular no arquivo `calculadora.py`, centralizado na classe `Calculadora`:
- `__init__()`: Constrói a janela (`340x480`), inicializa o estado (`self.expressao`), renderiza o visor e posiciona os 20 botões em uma grade 5x4.
- `atualizar_visor(texto)`: Encapsula a atualização visual do componente `CTkEntry`.
- `calcular_porcentagem()`: Encapsula a regra de negócio matemática para cálculos percentuais.
- `clique_botao(valor)`: Gerencia o fluxo de eventos dos botões (`C`, `⌫`, `±`, `%`, `=`, dígitos e operadores).

### 2. Implementação da Funcionalidade de Porcentagem (`%`)
Na versão inicial, o botão `%` apenas dividia o resultado total da expressão por `100` (`eval(self.expressao) / 100`), o que impedia cálculos reais de calculadora como acréscimos (`200 + 10%`) ou descontos (`200 - 15%`).

**Alterações realizadas no código:**
- **Importação do módulo `re`:** Utilizado para separar a expressão base, o operador e a taxa percentual através da expressão regular `r"^(.+)([+\-*/])(\d+(?:\.\d+)?)$"`.
- **Criação do método `calcular_porcentagem()`:**
  - **Adição (`+`):** Calcula o acréscimo percentual sobre a base (`base + (base * taxa)`).
  - **Subtração (`-`):** Calcula o desconto percentual sobre a base (`base - (base * taxa)`).
  - **Multiplicação (`*`):** Calcula a fração percentual da base (`base * taxa`).
  - **Divisão (`/`):** Divide a base pela taxa percentual (`base / taxa`), incluindo validação contra divisão por `0%`.
  - **Número isolado:** Converte diretamente o valor para sua forma decimal (`valor / 100`).
- **Refatoração em `clique_botao`:** A condição `elif valor == "%":` passou a delegar a execução diretamente para `self.calcular_porcentagem()`, mantendo o código limpo e de fácil manutenção.

### 3. Testes da Aplicação e Verificação de Regressão
Para garantir que a nova funcionalidade operasse corretamente sem impactar as operações existentes, foram executados testes cobrindo os cenários de porcentagem e as 4 operações básicas:

| Cenário de Teste | Entrada Simulada | Resultado Esperado | Resultado Obtido | Status |
| :--- | :---: | :---: | :---: | :---: |
| Porcentagem simples | `50` `%` | `0.5` | `0.5` | ✅ Passou |
| Acréscimo percentual | `200` `+` `10` `%` | `220` | `220` | ✅ Passou |
| Desconto percentual | `200` `-` `15` `%` | `170` | `170` | ✅ Passou |
| Multiplicação com `%` | `200` `*` `10` `%` | `20` | `20` | ✅ Passou |
| Divisão com `%` | `50` `/` `10` `%` | `500` | `500` | ✅ Passou |
| Divisão por `0%` | `100` `/` `0` `%` | `Erro: Divisão por 0` | `Erro: Divisão por 0` | ✅ Passou |
| Regressão: 4 operações | `10+5=`, `20-8=`, `6*7=`, `15/3=` | `15`, `12`, `42`, `5` | `15`, `12`, `42`, `5` | ✅ Passou |
| Precisão decimal | `0.1` `+` `0.2` `=` | `0.3` | `0.3` | ✅ Passou |

---

## 📝 Aprendizados da Imersão

- **Engenharia de Prompts (Desafio 1):** Formulação de instruções claras para obter um código modular e funcional via Google AI Studio.
- **Compreensão de Código Legado/Existente (Desafio 2):** Uso do Google Antigravity para mapear componentes, entender responsabilidades de métodos e identificar pontos de melhoria.
- **Manutenção Evolutiva e Refatoração (Desafio 2):** Extração de lógica complexa para métodos dedicados (`calcular_porcentagem`), utilizando expressões regulares sem quebrar a arquitetura existente.
- **Qualidade e Testes de Regressão (Desafio 2):** Validação sistemática de casos de uso e casos de borda (divisão por zero, precisão de ponto flutuante e preservação das operações anteriores).

---

Desenvolvido por **Davi Konuma** durante a Imersão Engenharia de Software da **Alura** & **Google**.
