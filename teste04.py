import flet as ft

def main(page: ft.Page):
    # Centraliza o conteúdo vertical e horizontalmente na página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ft.Text("Centralizado no meio da página!"))

ft.app(target=main)
