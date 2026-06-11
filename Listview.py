import asyncio
import flet as ft


async def main(page: ft.Page):
    page.title = "ListView de rolagem automática"

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    count = 1

    # 1. Adiciona as primeiras 30 linhas na tela de forma instantânea
    for i in range(0, 30):
        lv.controls.append(ft.Text(f"Linha {count}"))
        count += 1

    page.add(lv)

    # 2. Adiciona mais 30 linhas (uma por segundo) até chegar na Linha 60
    for i in range(0, 30):
        await asyncio.sleep(1)
        lv.controls.append(ft.Text(f"Linha {count}"))
        count += 1
        page.update()

ft.app(target=main)
