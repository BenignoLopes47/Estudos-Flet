import flet as ft

def main(page):
    page.title = "Exemplo usando \"card\""

    listitulo = ft.ListTile(leading=ft.Icon(ft.Icons.ACCESS_ALARM,  size=50, color="#D3143E"),
                            title=ft.Text("Compromisso: 28 de junho de 2024"),
                            subtitle=ft.Text("Aniversário de seu filho. Não esqueça o presente!"),)
    
    def apagar(e):
        listitulo.title= ft.Text("")
        listitulo.subtitle=ft.Text("* apagado", color="#aaaaaa")
        cartao.color="WHITE"
        page.update()

    def proximo(e):
        listitulo.title=ft.Text("Compromisso: 01 de agosto de 2024")
        listitulo.subtitle=ft.Text("Viagem para São Paulo", color="#000000")
        cartao.color="#CBEBA8"
        page.update()

    bt1 = ft.TextButton("Apagar", on_click=apagar)
    bt2 = ft.TextButton("Próximo compromisso", on_click=proximo)

    linha = ft.Row([bt1, bt2], alignment=ft.MainAxisAlignment.END)
    coluna = ft.Column([listitulo, linha,])
    contem = ft.Container(coluna, width=500, padding=20,)
    cartao = ft.Card(contem, bgcolor="YELLOW", shadow_color="white", elevation=8.0)

    page.add(cartao)

ft.app(target=main)