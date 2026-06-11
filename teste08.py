import flet as ft

def main(page: ft.Page):
    page.title = "Flet Information Displays Demo"
    page.window.width = 340
    page.window.height = 400

    header = ft.Text("Latest image", size=18)

    hero = ft.Image(
        src="https://picsum.photos/320/320",
        width=320,
        height=320,
        fit="contain"
    )

    page.add(
        header,
        hero,
    )


ft.app(target=main)
