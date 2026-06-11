import flet as ft

def main(page: ft.Page):
    # 1. Alinhamento horizontal (Eixo X)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # 2. Alinhamento vertical (Eixo Y)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos que vão ficar no centro do ecrã
    botao = ft.ElevatedButton("Botão Centralizado")
    texto = ft.Text("Texto no meio da página", size=20)

    page.add(texto, botao)

ft.app(target=main)
