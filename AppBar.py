import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Body!"))
    page.appbar = ft.AppBar(
    leading=ft.Icon(ft.Icons.PALETTE),
    leading_width=40,
    title=ft.Text("AppBar Example"),
    center_title=False,
    bgcolor=ft.Colors.AMBER,
    actions=[
        ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
        ft.IconButton(ft.Icons.FILTER_3)
    ],
)
    page.update()
    
ft.app(target=main)