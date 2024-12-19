import flet as ft
from utils.constants import APP_COLORS

class signUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        button_color = APP_COLORS['accent']
        title_color = APP_COLORS['white']
        self.content = ft.Column(
            controls=[
                ft.Text("Sign Up section", color=title_color, size=30),
                ft.ElevatedButton("Log In", color="black", on_click=lambda e: page.go("/login"), bgcolor=button_color),
            ]
        )   