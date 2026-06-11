import flet as ft

def main(page: ft.Page):
    page.title = "Flet Event & Callback Demo"
    page.window.width = 340
    page.window.height = 360

    # Criação do texto do diálogo primeiro
    dialog_text = ft.Text("")

    # Função para fechar o diálogo de forma compatível
    def fechar_dialogo(e):
        dlg_modal.open = False
        page.update()

    # Definição do diálogo modal
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Dialog"),
        content=dialog_text,
        actions=[ft.TextButton("OK", on_click=fechar_dialogo)],
    )

    # GARANTE QUE O DIÁLOGO FICA INVISÍVEL NO INÍCIO E ADICIONA AO OVERLAY
    dlg_modal.open = False
    page.overlay.append(dlg_modal)  # Solução universal para injetar o diálogo na página

    # Callback do botão "Click Me!"
    def on_click(e):  
        dialog_text.value = f'You typed: "{txt_input.value}"'
        dlg_modal.open = True  # Ativa a visibilidade
        page.update()          # Atualiza a página e renderiza o diálogo

    # Callback do botão "Abrir Diálogo"
    def abrir_dialogo(e):
        dialog_text.value = "Diálogo aberto sem texto digitado."
        dlg_modal.open = True  
        page.update()          

    # Elementos da interface
    txt_input = ft.TextField(label="Type something and press Click Me!")
    btn = ft.ElevatedButton("Click Me!", on_click=on_click)
    btn_abrir = ft.ElevatedButton("Abrir Diálogo", on_click=abrir_dialogo)

    # Adiciona os botões e inputs ao ecrã principal
    page.add(
        btn_abrir,
        txt_input,
        btn,
    )

ft.app(target=main)
