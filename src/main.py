import flet as ft
from router import views_handler
from utils.constants import APP_COLORS

def main(page: ft.Page):
    page.window_icon = "assets/icon.ico"
    def route_change(route):
        page.views.clear()
        page.views.append(views_handler(page)[page.route])
        page.update()

    page.on_route_change = route_change
    page.go("/login")

ft.app(target=main, assets_dir="assets")
