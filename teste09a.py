import flet as ft


def main(page: ft.Page):
    page.title = "Flet Dialog Demo"
    page.window.width = 300
    page.window.height = 300

    def on_dlg_button_click(e):
        if e.control.text == "Yes":
            page.window.close()
        page.close(dlg_modal)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmation"),
        content=ft.Text("Do you want to exit?"),
        actions=[
            ft.TextButton("Yes", on_click=on_dlg_button_click),
            ft.TextButton("No", on_click=on_dlg_button_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(dlg_modal)

    def abrir_dialogo(e):
        dlg_modal.open = True
        page.update()
    
    page.add(
        ft.ElevatedButton(
            "Exit",
            on_click=abrir_dialogo,
        ),
    )


ft.app(target=main)