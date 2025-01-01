import flet as ft
from utils.constants import APP_COLORS

class Ingresos(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        button_color = APP_COLORS['accent_button']
        title_color = "black"

        # Crear opciones para el dropdown
        dropdown_options = [
            ft.dropdown.Option(text="Option 1", key="1"),
            ft.dropdown.Option(text="Option 2", key="2"),
            ft.dropdown.Option(text="Option 3", key="3"),
        ]

        # Crear el dropdown
        dropdown = ft.Dropdown(
            options=dropdown_options,
            value="1",  # Valor por defecto
            on_change=lambda e: print(f"Selected: {e.control.value}"),
        )

        self.content = ft.Column(
            controls=[
                ft.Text("Ingresos section", color=title_color, size=30),
                ft.ElevatedButton("Dashboard", color="black", on_click=lambda e: page.go("/dashboard"), bgcolor=button_color),
            ]
        )   