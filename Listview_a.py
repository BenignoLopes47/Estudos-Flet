import flet as ft

def main(page: ft.Page):
    page.title = "Carrossel com Imagens"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK  # Fundo escuro para destacar as imagens
    
    page.add(ft.Text("Galeria de Destinos", size=24, weight=ft.FontWeight.BOLD))

    # Configuração da ListView Horizontal
    lista_horizontal = ft.ListView(
        horizontal=True,
        spacing=20,
        item_extent=160,  # Largura de cada cartão
        height=200,       # Altura total do carrossel
    )

    # Lista de IDs de imagens do Unsplash para simular fotos reais
    image_ids = ["1507525428034-b723cf961d3e", "1470071459604-3b5ec3a7fe05", "1501854140801-50d01698950b", "1447752875215-b2761acb3c5d"]

    for i, img_id in enumerate(image_ids, start=1):
        lista_horizontal.controls.append(
            ft.Container(
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                border_radius=15,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  # Força a imagem a respeitar as bordas arredondadas do cartão
                content=ft.Column(
                    controls=[
                        # Componente de Imagem
                        ft.Image(
                            src=f"https://unsplash.com{img_id}?w=300&auto=format&fit=crop",
                            height=150,
                            fit="contain",  
                        ),
                        # Texto/Legenda abaixo da imagem
                        ft.Container(
                            content=ft.Text(f"Lugar {i}", weight=ft.FontWeight.BOLD, size=14),
                            padding=(8)
                        )
                    ],
                    spacing=5,
                )
            )
        )

    page.add(lista_horizontal)

ft.app(target=main)
