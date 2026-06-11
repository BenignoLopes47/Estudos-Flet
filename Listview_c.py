import flet as ft

def main(page: ft.Page):
    page.title = "Lista Vertical com Fotos Locais"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    page.add(ft.Text("Minhas Fotos Locais", size=24, weight=ft.FontWeight.BOLD))

    lista_vertical = ft.ListView(
        horizontal=False,
        spacing=15,
        item_extent=100,
        width=400,
        expand=True
    )

    # 1. Lista com os nomes exatos dos seus arquivos na pasta assets
    minhas_fotos = ["/foto1.jpg", "/foto2.jpg", "/foto3.jpg"]

    # 2. O loop vai ler uma foto de cada vez
    for i, nome_foto in enumerate(minhas_fotos, start=1):
        lista_vertical.controls.append(
            ft.Container(
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                border_radius=15,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                content=ft.Row(
                    controls=[
                        # Cada item recebe uma única foto da lista
                        ft.Image(
                            src=nome_foto,  # <--- Corrigido: ex: "/foto1.jpg"
                            width=100,
                            height=100,
                            fit="contain",
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(f"Foto Número {i}", weight=ft.FontWeight.BOLD, size=16),
                                    ft.Text(f"Arquivo: {nome_foto}", size=12, color=ft.Colors.ON_SURFACE_VARIANT),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5,
                            ),
                            padding=(10),
                            expand=True
                        )
                    ],
                )
            )
        )

    page.add(lista_vertical)

# 3. OBRIGATÓRIO: Definir onde está a pasta assets (ela deve estar ao lado deste script)
ft.app(target=main, assets_dir="assets")
