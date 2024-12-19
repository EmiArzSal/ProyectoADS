import flet as ft
from screens.home_screen import home_screen
from screens.reports_screen import reports_screen
from screens.settings_screen import settings_screen

def dashboard_screen(page: ft.Page):
    # Función para cambiar el contenido principal
    def change_screen(e):
        selected_screen.content = get_screen(e.control.data)
        page.update()

    # Función que devuelve las secciones
    def get_screen(name):
        if name == "home":
            return home_screen()
        elif name == "reports":
            return reports_screen()
        elif name == "settings":
            return settings_screen()
        return ft.Text("Pantalla no encontrada")

    # Contenedor del contenido principal
    selected_screen = ft.Container(content=home_screen())

    # Menú lateral
    menu = ft.NavigationRail(
        selected_index=0,
        on_change=change_screen,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME, label="Inicio", data="home"),
            ft.NavigationRailDestination(icon=ft.icons.ANALYTICS, label="Reportes", data="reports"),
            ft.NavigationRailDestination(icon=ft.icons.SETTINGS, label="Configuración", data="settings"),
        ],
    )

    return ft.Row(
        [
            menu,  # Menú lateral
            ft.VerticalDivider(width=1),  # Separador
            ft.Expanded(child=selected_screen),  # Contenido principal
        ]
    )
