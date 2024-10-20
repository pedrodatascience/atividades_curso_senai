import flet as ft


class CalculaBoatao(ft.ElevatedButton):
    def __init__(self, text, clicou_botao, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand #expande o botão
        self.on_click = clicou_botao
        self.data = text

class BotaoDigito(CalculaBoatao):
    def __init__(self, text, clicou_botao, expand=1):
        CalculaBoatao.__init__(self, text, clicou_botao, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class AcaoBotao(CalculaBoatao):
    def __init__(self, text, clicou_botao):
        BotaoDigito.__init__(self, text, clicou_botao)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class AcaoExtraBotao(BotaoDigito):
    def __init__(self, text, clicou_botao):
        CalculaBoatao.__init__(self, text, clicou_botao)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK


class CalculatorApp(ft.Container):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        self.width = 350
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),
                ft.Row(
                    controls=[
                        AcaoExtraBotao(
                            text="AC", clicou_botao=self.clicou_botao
                        ),
                        AcaoExtraBotao(
                            text="+/-", clicou_botao=self.clicou_botao
                        ),
                        AcaoExtraBotao(text="%", clicou_botao=self.clicou_botao),
                        AcaoBotao(text="/", clicou_botao=self.clicou_botao),
                    ]
                ),
                ft.Row(
                    controls=[
                        BotaoDigito(text="7", clicou_botao=self.clicou_botao),
                        BotaoDigito(text="8", clicou_botao=self.clicou_botao),
                        BotaoDigito(text="9", clicou_botao=self.clicou_botao),
                        AcaoBotao(text="*", clicou_botao=self.clicou_botao),
                    ]
                ),
                ft.Row(
                    controls=[
                        BotaoDigito(text="4", clicou_botao=self.clicou_botao),
                        BotaoDigito(text="5", clicou_botao=self.clicou_botao),
                        BotaoDigito(text="6", clicou_botao=self.clicou_botao),
                        AcaoBotao(text="-", clicou_botao=self.clicou_botao),
                    ]
                ),
                ft.Row(
                    controls=[
                        BotaoDigito(text="1", clicou_botao=self.clicou_botao),
                        BotaoDigito(text="2", clicou_botao=self.clicou_botao),
                        BotaoDigito(text="3", clicou_botao=self.clicou_botao),
                        AcaoBotao(text="+", clicou_botao=self.clicou_botao),
                    ]
                ),
                ft.Row(
                    controls=[
                        BotaoDigito(
                            text="0", expand=2, clicou_botao=self.clicou_botao
                        ),
                        BotaoDigito(text=".", clicou_botao=self.clicou_botao),
                        AcaoBotao(text="=", clicou_botao=self.clicou_botao),
                    ]
                ),
            ]
        )
    
    def clicou_botao(self, e):
        data = e.control.data
        print(f'Botão clicado com dados = {data}')
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == '0' or self.new_operand == 'True':
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data    
        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )
        self.update()
    
    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num
    
    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    
    calc = CalculatorApp()
 
    page.title = 'Calculadora'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.add(calc)   
    

    page.update()

ft.app(main)