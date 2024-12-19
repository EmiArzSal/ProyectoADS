import flet as ft
from utils.constants import APP_COLORS


class loginGoogle(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        button_colortext = APP_COLORS['other']

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Inicio de sesión con Google", color="white", size=30, weight=ft.FontWeight.BOLD),
                            ft.ElevatedButton("Iniciar sesión con Google", bgcolor="white", color="black", icon=ft.Image(src=f"/assets/icon-google.png"), style=ft.ButtonStyle(text_style=ft.TextStyle(size=16), padding=ft.padding.symmetric(horizontal=18, vertical=12))),
                            ft.Text("¿Aún no tienes una cuenta?", color=APP_COLORS['text_secondary']),
                            ft.ElevatedButton("Registrarse", bgcolor="white", color=button_colortext, style=ft.ButtonStyle(text_style=ft.TextStyle(size=16), padding=ft.padding.symmetric(horizontal=18, vertical=12)), on_click=lambda e: page.go("/signup")),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=ft.padding.all(80),
                    width=600,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.on_click = lambda e: page.go("/loginGoogle")