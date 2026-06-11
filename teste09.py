import flet as ft


def main(page: ft.Page):
    page.title = "Flet Dialog Demo"
    page.window.width = 300
    page.window.height = 300

    def on_dlg_button_click(e):
        if e.control.text == "Yes":
            page.window.destroy()  # Fecha o aplicativo de vez
        else:
            dlg_modal.open = False  # Fecha o diálogo mudando a propriedade
            page.update()           # Atualiza a página para aplicar a mudança

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

    # 1. Adiciona o diálogo diretamente no overlay da página (Essencial para versões antigas)
    page.overlay.append(dlg_modal)

    def abrir_dialogo(e):
        dlg_modal.open = True  # Altera a propriedade para visível
        page.update()          # Força a atualização visual da página

    page.add(
        ft.ElevatedButton(
            "Abrir Diálogo",
            on_click=abrir_dialogo,
        ),
    )


ft.app(target=main)
