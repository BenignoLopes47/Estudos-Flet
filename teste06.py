import flet as ft

def main(page:ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "App com linha e colunas"
    texto1 = ft.Text(value= "Texto 1",size=24,color=ft.Colors.WHITE)
    texto2 = ft.Text(value= "Texto 2",size=24,color=ft.Colors.WHITE)
    texto3 = ft.Text(value= "Texto 3",size=24,color=ft.Colors.WHITE)
    page.add(ft.Row(
        controls=[texto1,texto2,texto3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
        )
    )

    botao1 = ft.FilledButton("Botão 1")
    botao2 = ft.FilledButton("Botão 2")
    botao3 = ft.FilledButton("Botão 3")
    
    fila_botoes = ft.Row(
        controls=[botao1,botao2,botao3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(fila_botoes)
    
    textos_colunas = [
        ft.Text(value="Coluna 1 - Fila 1", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Coluna 1 - Fila 2", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Coluna 1 - Fila 3", size=18, color=ft.Colors.WHITE),]
      
    coluna_texto1 = ft.Column(
        controls=textos_colunas,
    )
    
    
    
    textos_colunas2 = [
        ft.Text(value="Coluna 2 - Fila 1", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Coluna 2 - Fila 2", size=18, color=ft.Colors.WHITE),
        ft.Text(value="Coluna 2 - Fila 3", size=18, color=ft.Colors.WHITE),]
    coluna_texto2 = ft.Column(
        controls=textos_colunas2,
    )
    fila_colunas = ft.Row(
        controls=[coluna_texto1,coluna_texto2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    page.add(fila_colunas)
    
        




ft.app(target=main)


