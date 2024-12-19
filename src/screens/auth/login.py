import flet as ft
from utils.constants import APP_COLORS

class login(ft.Container):
    
    
    def __init__(self, page: ft.Page):
        super().__init__(page)
    
        button_colortext = APP_COLORS['other']
        bg_inputs = APP_COLORS['secondary']
        label_color = APP_COLORS['text_secondary']

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Inicio de sesión", color="white", size=30, weight=ft.FontWeight.BOLD),
                            ft.TextField(label="Correo electrónico",label_style=ft.TextStyle(color=label_color), bgcolor=bg_inputs, color="white"),
                            ft.TextField(label="Contraseña",label_style=ft.TextStyle(color=label_color), password=True, can_reveal_password=True,bgcolor=bg_inputs, color="white"),
                            ft.ElevatedButton("Iniciar sesión", bgcolor=APP_COLORS['accent'], color="black", style=ft.ButtonStyle(text_style=ft.TextStyle(size=16), padding=ft.padding.symmetric(horizontal=18, vertical=12))),
                            ft.ElevatedButton("Iniciar sesión con Google", bgcolor="white", color=button_colortext, style=ft.ButtonStyle(text_style=ft.TextStyle(size=16), padding=ft.padding.symmetric(horizontal=18, vertical=12)), on_click=lambda e: self.login_with_google()),
                            ft.Text("¿Aún no tienes una cuenta?", color=APP_COLORS['text_secondary']),
                            ft.ElevatedButton("Registrarse", bgcolor="white", color=button_colortext, style=ft.ButtonStyle(text_style=ft.TextStyle(size=16), padding=ft.padding.symmetric(horizontal=18, vertical=12)), on_click=lambda e: page.go("/signup")),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=ft.padding.all(80),
                    width=400,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
