import flet as ft

def main(page: ft.Page):
    st = ft.Stack(
        [
            ft.Image(
                src="https://picsum.photos/300/300",
                width=600,
                height=500,
                fit="contain",
            
            ),
            ft.Row(
                [
                    ft.Text(
                        "Título da imagem",
                        color="white",
                        size=30,
                        weight="bold",
                        opacity=0.5,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        width=300,
        height=300,
    )
    page.add(st)
    
ft.app(target=main)