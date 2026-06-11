import flet as ft

def main(page: ft.Page):
    items = []
    for i in range(1, 8):
        items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.Alignment.CENTER,
                width=50,
                height=50,
                bgcolor=ft.Colors.GREEN_700,
                border_radius=10,
            )
        )
    col = ft.Column(spacing=10, controls=items)
    page.add(ft.Column([ft.Text("Exemplo de column em Flet")]), col)
    
ft.app(target=main)