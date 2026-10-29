# 🧮 Calculadora Gráfica com CustomTkinter

> **Desafio 1 - Imersão Engenharia de Software: Dev na Era da IA**  
> Parceria: **Google** & **Alura**

Projeto desenvolvido como solução do primeiro desafio da imersão, utilizando assistência de Inteligência Artificial (**Google AI Studio**) para projetar e construir uma calculadora completa em Python com interface gráfica moderna.

---

## 📌 Sobre o Desafio

O objetivo principal deste desafio foi explorar o uso de ferramentas de IA no fluxo de desenvolvimento de software, compreendendo como instruções, variáveis, estruturas condicionais e tratamento de eventos se articulam na construção de uma aplicação funcional.

### Questões propostas pelo desafio:
1. **Quais são os principais componentes do código gerado?**
2. **Como a aplicação recebe os números e identifica a operação escolhida?**
3. **Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal do projeto.
- **CustomTkinter** - Biblioteca gráfica baseada em Tkinter para criação de interfaces modernas no modo Dark.
- **Google AI Studio** - Plataforma de IA utilizada na assistência e geração do código.

---

## 🎨 Funcionalidades

- ➕ **Operações Básicas:** Adição (+), Subtração (-), Multiplicação (*) e Divisão (/).
- 🎛️ **Recursos Adicionais:** 
  - Limpar visor (`C`).
  - Apagar último caractere (`⌫`).
  - Cálculo de porcentagem (`%`).
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
   git clone https://github.com/seu-usuario/calculadora-customtkinter.git
   cd calculadora-customtkinter
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

## 🧐 Explicação Técnica e Análise do Código

Para responder às perguntas reflexivas propostas pela **Imersão Alura + Google**:

### 1. Quais são os principais componentes do código gerado?
* **Classe `Calculadora` (`ctk.CTk`):** Estrutura principal baseada em Programação Orientada a Objetos (POO) que representa a janela da aplicação.
* **Visor (`CTkEntry`):** Campo de texto onde os números e resultados são exibidos (configurado como `readonly` para evitar digitação manual).
* **Grade de Botões (`CTkButton`):** Conjunto de botões mapeados em uma lista de tuplas com suas posições (linha, coluna) e cores estilizadas.
* **Método `clique_botao(valor)`:** Função central encarregada de capturar as ações do usuário.
* **Método `atualizar_visor(texto)`:** Função auxiliar que gerencia o estado do visor de forma segura.

### 2. Como a aplicação recebe os números e identifica a operação escolhida?
A interface mapeia cada clique de botão via comando `lambda t=texto: self.clique_botao(t)`. 

* Quando um número ou operador é clicado, o caractere correspondente é enviado para o método `clique_botao`.
* O programa concatena o caractere recebido em uma string chamada `self.expressao`.
* **Tratamento de duplicidade de operadores:** Caso o usuário digite dois operadores em sequência (ex: `5 + *`), o código identifica a duplicidade e substitui o operador anterior pelo novo.

### 3. Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?
* **Processamento:** Ao pressionar `=`, a aplicação limpa e valida a string de expressão contida em `self.expressao`.
* **Cálculo:** Utiliza a função `eval()` dentro de um bloco de proteção `try-except` para interpretar matematicamente a expressão formatada.
* **Tratamento de Exceções:** 
  - Se houver tentativa de divisão por zero (`/0`), é exibida a mensagem `"Erro: Divisão por 0"`.
  - Se a sintaxe for inválida, é exibida a mensagem `"Erro"`.
* **Formatação do Resultado:** Caso o resultado seja um número de ponto flutuante inteiro (ex: `10.0`), ele é convertido para inteiro (`10`). Se tiver casas decimais, é arredondado em até 8 casas para manter o visor limpo.

---

## 📝 Aprendizados da Imersão

- **Engenharia de Prompts:** Formulação de instruções claras para obter um código modular e funcional via Google AI Studio.
- **Leitura e Compreensão de Código:** Entendimento de como eventos da interface acionam a lógica interna em Python.
- **Resiliência de Software:** Implementação de regras para prevenção de erros de execução (Divisão por zero, ponto decimal duplo, etc.).

---

Desenvolvido por **Davi Konuma** durante a Imersão Engenharia de Software da **Alura** & **Google**.
