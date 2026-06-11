import flet as ft

def main(page: ft.Page):
    # Centraliza o container principal na página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def mover_conteudo(e):
        # Alterna o alinhamento entre o topo-esquerda e o centro
        if container_animado.alignment == ft.Alignment.TOP_LEFT:
            container_animado.alignment = ft.Alignment.CENTER
            texto.value = "Cheguei ao Centro!"
        else:
            container_animado.alignment = ft.Alignment.TOP_LEFT
            texto.value = "Estou no Canto!"
        
        # Atualiza a página para executar a animação
        page.update()

    texto = ft.Text("Estou no Canto!", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)

    # Container animado
    container_animado = ft.Container(
        content=texto,
        alignment=ft.Alignment.TOP_LEFT, # Posição inicial
        width=300,
        height=300,
        bgcolor=ft.Colors.BLUE_700,
        border_radius=10,
        padding=20,
        # Define a duração e o estilo da transição
        animate=ft.Animation(1000, curve=ft.AnimationCurve.EASE_IN_OUT_CUBIC)
    )

    botao = ft.ElevatedButton("Alternar Posição", on_click=mover_conteudo)

    page.add(container_animado, ft.Divider(height=20, color=ft.Colors.TRANSPARENT), botao)

ft.app(target=main)
