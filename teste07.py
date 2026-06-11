import flet as ft


def main(page: ft.Page):
    page.title = "Flet Navigation Bar Demo"
    page.window.width = 500
    page.window.height = 500

    info = ft.Text("You are on the Home tab", text_align=ft.TextAlign.CENTER)

    def on_nav_change(e):
        idx = page.navigation_bar.selected_index
        if idx == 0:
            info.value = "You are on the Home tab"
        elif idx == 1:
            info.value = "You are on the Search tab"
        else:
            info.value = "You are on the Profile tab"
            
                    
        page.update()
        

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
        ],
        on_change=on_nav_change,
    )

    page.add(
        ft.Row([
            ft.Column(
                controls=[info],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                
            )
        ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )

        )
    

        


ft.app(target=main)
