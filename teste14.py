import flet as ft
import os

# Deteta a pasta exata onde este ficheiro .py está guardado e muda para .txt
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "lista_compras.txt")

class ShoppingItem(ft.Row):
    def __init__(self, text, completed, edit_item, delete_item):
        super().__init__()
        self.text = text
        self.completed = completed
        self.edit_item = edit_item
        self.delete_item = delete_item
        
        # Componentes visuais
        self.checkbox = ft.Checkbox(value=self.completed, label=self.text, on_change=self.checkbox_changed)
        self.edit_name = ft.TextField(value=self.text, expand=1)
        
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.checkbox,
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE, on_click=self.edit_clicked),
                        ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED, on_click=self.delete_clicked),
                    ]
                )
            ]
        )
        
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(icon=ft.Icons.CHECK, icon_color=ft.Colors.GREEN, on_click=self.save_clicked)
            ]
        )
        
        self.controls = [self.display_view, self.edit_view]

    async def checkbox_changed(self, e):
        self.completed = self.checkbox.value
        await self.edit_item(self)

    def edit_clicked(self, e):
        self.edit_name.value = self.checkbox.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    async def save_clicked(self, e):
        if self.edit_name.value.strip():
            self.text = self.edit_name.value
            self.checkbox.label = self.edit_name.value
            self.display_view.visible = True
            self.edit_view.visible = False
            self.update()
            await self.edit_item(self)

    async def delete_clicked(self, e):
        await self.delete_item(self)


async def main(page: ft.Page):
    page.title = "Lista de Compras Local"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 450
    page.window_height = 600

    items_list = ft.Column()

    # Grava diretamente no ficheiro TXT, uma linha por item
    async def save_data():
        with open(DB_PATH, "w", encoding="utf-8") as f:
            for item in items_list.controls:
                # Guarda no formato: True|Nome do Item ou False|Nome do Item
                f.write(f"{item.completed}|{item.text}\n")

    # Carrega do ficheiro TXT se ele existir
    async def load_data():
        if os.path.exists(DB_PATH):
            with open(DB_PATH, "r", encoding="utf-8") as f:
                for linha in f:
                    linha = linha.strip()
                    if linha and "|" in linha:
                        # Divide o estado (True/False) do texto do produto
                        completado_str, texto = linha.split("|", 1)
                        completado = completado_str == "True"
                        
                        items_list.controls.append(
                            ShoppingItem(texto, completado, item_updated, item_deleted)
                        )
            page.update()

    async def item_updated(item):
        await save_data()

    async def item_deleted(item):
        items_list.controls.remove(item)
        await save_data()
        page.update()

    async def add_clicked(e):
        if new_item_field.value.strip():
            item = ShoppingItem(new_item_field.value, False, item_updated, item_deleted)
            items_list.controls.append(item)
            new_item_field.value = ""
            await save_data()
            page.update()

    new_item_field = ft.TextField(hint_text="O que precisa de comprar?", expand=True, on_submit=add_clicked)
    add_btn = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)

    page.add(
        ft.Text("Minha Lista de Compras", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, weight=ft.FontWeight.BOLD),
        ft.Row(
            controls=[
                new_item_field,
                add_btn
            ]
        ),
        ft.Divider(),
        items_list
    )

    await load_data()

ft.app(target=main)
