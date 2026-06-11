import flet as ft


def main(page: ft.Page):
    # 1. Definimos uma largura inicial padrão para a janela funcionar corretamente
    page.window.width = 800
    page.window.height = 600

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    ft.Text(value=str(i), color="white", size=20),
                    alignment=ft.Alignment.CENTER,
                    width=40,
                    height=40,
                    bgcolor="#40A4D2",
                    border_radius=10
                )
            )
        return items

    def muda_largura(e):
        linha.width = float(e.control.value)
        linha.update()

    def muda_separa(e):
        linha.spacing = int(e.control.value)
        linha.update()

    slid_separa = ft.Slider(min=0, max=50, divisions=50,
                            value=0, label="{value}", on_change=muda_separa)

    # 2. Atualizado para usar page.window.width
    slid_largura = ft.Slider(
        min=0,
        max=page.window.width,
        divisions=20,
        value=page.window.width,
        label="{value}",
        on_change=muda_largura
    )

    # 3. Atualizado para usar page.window.width
    linha = ft.Row(wrap=True, spacing=10, run_spacing=10,
                   controls=items(30), width=page.window.width)

    txt1 = ft.Text("O primeiro controle seleciona a largura da linha:")
    txt2 = ft.Text("O segundo controle seleciona espaçamento entre colunas:")

    page.add(
        ft.Column([txt1, slid_largura]),
        ft.Column([txt2, slid_separa]),
        linha
    )


ft.app(target=main)
