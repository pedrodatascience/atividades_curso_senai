#Crie um programa que calcule o IMC do usuário, em Flet. Ao terminar, envie o link do repositório.
import flet as ft
#  pyinstaller  #gera o executavel pra web
#  pillow #conver a imagem pra usar como incone

def main(page: ft.Page):
    def calcular_imc(e):
        imc = float(peso.value.replace(',','.')) / (float(altura.value.replace(',','.')) ** 2)
        result.value = f'{nome.value} seu IMC é: {imc:.2f}'
        if imc < 18.5:
                result.value += ' (Abaixo do peso)'
        elif 18.5 <= imc < 24.9:
            result.value += ' (Peso normal)'
        elif 25 <= imc < 29.9:
            result.value += ' (Sobrepeso)'
        else:
            result.value += ' (Obesidade)'
        

        page.update()


    nome = ft.TextField(label='Nome')
    peso = ft.TextField(label='Peso', suffix_text='kg', suffix_style=ft.TextStyle(color='grey'))
    altura = ft.TextField(label='Altura', suffix_text='metros', suffix_style=ft.TextStyle(color='grey'), on_submit=calcular_imc)
    result = ft.Text(size=30, color= '#D02323')

    botao = ft.ElevatedButton(
         'CALCULAR',
         bgcolor='#53B63B',
         color='white',
         
         elevation=10,
         on_click= calcular_imc,
         width=300, #largura
         height=50 #altura
              
    )

    page.title = 'Calculadora de IMC'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
         ft.Row(
              [ft.Text('Calculadora de IMC', size=40, weight='bold')],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [nome],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [peso],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [altura],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [botao],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.update()

ft.app(main)