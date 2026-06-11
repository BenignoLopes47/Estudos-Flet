import flet as ft

def main(page: ft.Page):
    

    page.add(
        ft.Row(
            [
                
            ft.Text("Centralizado no meio da página!")
            
            ],
        
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )
    
        
ft.app(target=main)
