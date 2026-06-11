import flet as ft

def main(page: ft.Page): # 'Page' com P maiúsculo
    items = []
    for i in range(1, 8):
        # Componentes e propriedades com iniciais maiúsculas
        items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.Alignment.CENTER, # Correção do alinhamento do container
                width=50,
                height=50,
                bgcolor=ft.Colors.AMBER, # Cores geralmente em maiúsculas (ou string "amber")
                border_radius=10,
            )
        )
        
    # 'Row' e 'Column' com iniciais maiúsculas
    row = ft.Row(spacing=10, controls=items)
    
    # Passando os elementos corretamente dentro do page.add()
    page.add(
        ft.Column([ft.Text("exemplo de rows em flet")]), 
        row
    )

ft.app(target=main)
