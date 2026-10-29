"""
Calculadora Gráfica com CustomTkinter em Python
Requisitos:
- 4 operações básicas: adição (+), subtração (-), multiplicação (*) e divisão (/)
- Interface gráfica com a lib customtkinter
- Código simples e funcional

Como executar:
1. Instale o CustomTkinter: pip install customtkinter
2. Execute o script: python calculadora.py
"""

import customtkinter as ctk

# Configurações globais de aparência do CustomTkinter
ctk.set_appearance_mode("dark")         # "dark", "light" ou "system"
ctk.set_default_color_theme("blue")     # "blue", "green" ou "dark-blue"


class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Calculadora CustomTkinter")
        self.geometry("340x480")
        self.resizable(False, False)

        # Variável para armazenar a expressão matemática atual
        self.expressao = ""

        # Visor da Calculadora (CTkEntry)
        self.visor = ctk.CTkEntry(
            self,
            font=ctk.CTkFont(size=30, weight="bold"),
            justify="right",
            height=70,
            corner_radius=12
        )
        self.visor.grid(row=0, column=0, columnspan=4, padx=16, pady=(20, 16), sticky="nsew")
        self.visor.insert(0, "0")
        self.visor.configure(state="readonly")

        # Definição dos botões: (Texto, Linha, Coluna, Cor_Fundo, Cor_Hover)
        botoes = [
            ("C", 1, 0, "#e74c3c", "#c0392b"),
            ("⌫", 1, 1, "#7f8c8d", "#95a5a6"),
            ("%", 1, 2, "#34495e", "#2c3e50"),
            ("/", 1, 3, "#1f538d", "#14375e"),

            ("7", 2, 0, None, None),
            ("8", 2, 1, None, None),
            ("9", 2, 2, None, None),
            ("*", 2, 3, "#1f538d", "#14375e"),

            ("4", 3, 0, None, None),
            ("5", 3, 1, None, None),
            ("6", 3, 2, None, None),
            ("-", 3, 3, "#1f538d", "#14375e"),

            ("1", 4, 0, None, None),
            ("2", 4, 1, None, None),
            ("3", 4, 2, None, None),
            ("+", 4, 3, "#1f538d", "#14375e"),

            ("±", 5, 0, None, None),
            ("0", 5, 1, None, None),
            (".", 5, 2, None, None),
            ("=", 5, 3, "#2ecc71", "#27ae60"),
        ]

        # Criação dos botões com CTkButton
        for texto, linha, coluna, cor_fg, cor_hover in botoes:
            kwargs = {
                "text": texto,
                "font": ctk.CTkFont(size=20, weight="bold"),
                "width": 64,
                "height": 52,
                "corner_radius": 10,
                "command": lambda t=texto: self.clique_botao(t)
            }
            if cor_fg:
                kwargs["fg_color"] = cor_fg
            if cor_hover:
                kwargs["hover_color"] = cor_hover

            btn = ctk.CTkButton(self, **kwargs)
            btn.grid(row=linha, column=coluna, padx=6, pady=6, sticky="nsew")

        # Configurar proporção de expansão da grade
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)
        for lin in range(1, 6):
            self.grid_rowconfigure(lin, weight=1)

    def atualizar_visor(self, texto):
        """Atualiza o visor mantendo a proteção de apenas leitura."""
        self.visor.configure(state="normal")
        self.visor.delete(0, "end")
        self.visor.insert(0, str(texto))
        self.visor.configure(state="readonly")

    def clique_botao(self, valor):
        """Processa as 4 operações básicas e ações especiais."""
        # Limpar visor
        if valor == "C":
            self.expressao = ""
            self.atualizar_visor("0")

        # Apagar último dígito
        elif valor == "⌫":
            self.expressao = self.expressao[:-1]
            self.atualizar_visor(self.expressao if self.expressao else "0")

        # Inverter sinal positivo/negativo
        elif valor == "±":
            if self.expressao and self.expressao != "0":
                if self.expressao.startswith("-"):
                    self.expressao = self.expressao[1:]
                else:
                    self.expressao = "-" + self.expressao
                self.atualizar_visor(self.expressao)

        # Porcentagem
        elif valor == "%":
            try:
                if self.expressao:
                    res = eval(self.expressao) / 100
                    if res.is_integer():
                        res = int(res)
                    self.expressao = str(res)
                    self.atualizar_visor(self.expressao)
            except Exception:
                self.atualizar_visor("Erro")
                self.expressao = ""

        # Calcular resultado com as 4 operações (+, -, *, /)
        elif valor == "=":
            if not self.expressao:
                return

            try:
                expr_limpa = self.expressao.replace(" ", "")
                # Validação contra divisão por zero
                if "/0" in expr_limpa and not "/0." in expr_limpa:
                    self.atualizar_visor("Erro: Divisão por 0")
                    self.expressao = ""
                    return

                resultado = eval(expr_limpa)

                # Formata inteiros sem casas decimais supérfluas
                if isinstance(resultado, float) and resultado.is_integer():
                    resultado = int(resultado)
                elif isinstance(resultado, float):
                    resultado = round(resultado, 8)

                self.atualizar_visor(resultado)
                self.expressao = str(resultado)
            except ZeroDivisionError:
                self.atualizar_visor("Erro: Divisão por 0")
                self.expressao = ""
            except Exception:
                self.atualizar_visor("Erro")
                self.expressao = ""

        # Inserção de dígitos e operadores (+, -, *, /)
        else:
            operadores = ["+", "-", "*", "/"]

            # Substitui operador se o usuário digitar dois seguidos
            if valor in operadores:
                if not self.expressao:
                    if valor == "-":
                        self.expressao = "-"
                        self.atualizar_visor(self.expressao)
                    return

                if self.expressao[-1] in operadores:
                    self.expressao = self.expressao[:-1] + valor
                    self.atualizar_visor(self.expressao)
                    return

            # Controle de ponto decimal
            if valor == ".":
                partes = self.expressao.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split()
                if partes and "." in partes[-1]:
                    return
                if not self.expressao or self.expressao[-1] in operadores:
                    self.expressao += "0"

            self.expressao += valor
            self.atualizar_visor(self.expressao)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
