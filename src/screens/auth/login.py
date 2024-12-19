import flet as ft
from utils.constants import APP_COLORS

class Login(ft.Container):
    
    
    def __init__(self, page: ft.Page):
        super().__init__(page)
    
        button_colortext = APP_COLORS['other']
        bg_inputs = APP_COLORS['secondary']
        label_color = APP_COLORS['text_secondary']
        google_button = ft.ElevatedButton(
            "Iniciar sesión con Google",
            bgcolor="white",
            color="black",
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=20),
            ),
            on_click=lambda e: page.go("/loginGoogle"),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="https://img.icons8.com/color/48/google-logo.png",
                        width=24,  # Ajusta el tamaño del icono
                        height=24
                    ),
                    ft.Text("Iniciar sesión con Google", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            width=250,
        )

        facebook_button = ft.ElevatedButton(
            "Iniciar sesión con Facebook",
            bgcolor="white",
            color="black",
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=20),
            ),
            on_click=lambda e: page.go("/loginGoogle"),
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.FACEBOOK, size=24, color="blue"),
                    ft.Text("Iniciar sesión con Facebook", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            width=270,
        )

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Hola, bienvenidx!", color="white", size=30, weight=ft.FontWeight.BOLD),
                            ft.TextField(label="Correo electrónico",border=None,border_color=None,  border_width = None, label_style=ft.TextStyle(color=label_color), bgcolor=bg_inputs, color="white", width=400),
                            ft.TextField(label="Contraseña",border=None,border_color=None,  border_width = None, label_style=ft.TextStyle(color=label_color), password=True, can_reveal_password=True,bgcolor=bg_inputs, color="white", width=400),
                            ft.ElevatedButton("Iniciar sesión", bgcolor=APP_COLORS['accent'], color="black", style=ft.ButtonStyle(text_style=ft.TextStyle(size=16), padding=ft.padding.symmetric(horizontal=18, vertical=12))),
                            ft.Text("o", color=APP_COLORS['text_secondary']),
                            ft.Row(
                                controls=[google_button, facebook_button],  # Ambos botones se colocan en fila
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=20
                            ),
                            ft.Text("¿Aún no tienes una cuenta?", color=APP_COLORS['text_secondary']),
                            ft.ElevatedButton("Registrarse", bgcolor="white", color=button_colortext, style=ft.ButtonStyle(text_style=ft.TextStyle(size=16), padding=ft.padding.symmetric(horizontal=18, vertical=12)), on_click=lambda e: page.go("/signup")),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=ft.padding.all(80),
                    width=680,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
