import flet as ft

# Função para processar as entradas e calcular o resultado
def main(page: ft.Page):
    page.title = "Calc App"
    
    # Campo de exibição da calculadora
    display = ft.Text(value="0", size=32, weight="bold")
    current_expression = ""

    # Função para lidar com os cliques dos botões
    def button_click(e):
        nonlocal current_expression

        if e.control.data == "AC":
            current_expression = ""
            display.value = "0"
        elif e.control.data == "=":
            try:
                current_expression = str(eval(current_expression))
            except:
                current_expression = "Erro"
            display.value = current_expression
        else:
            if current_expression == "Erro":
                current_expression = ""
            current_expression += e.control.data
            display.value = current_expression

        page.update()

    # Função para criar botões
    def create_button(text, data, width=80, height=60):
        return ft.ElevatedButton(
            text,
            data=data,
            width=width,
            height=height,
            on_click=button_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=20),
                color=ft.colors.BLUE
            )
        )

    # Layout dos botões
    buttons = [
        ["AC", "+/-", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "="]
    ]

    # Cria o layout da calculadora
    calc_layout = ft.Column(
        [
            display,
            ft.Column(
                [
                    ft.Row([create_button(text, text) for text in row], alignment="center")
                    for row in buttons
                ],
                tight=True
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Adiciona à página
    page.add(calc_layout)

# Executa o app
ft.app(target=main)
