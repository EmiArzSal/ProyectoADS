import flet as ft 
from utils.constants import APP_COLORS
from utils.validation import Validation

class Login(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.validation = Validation()
        
        self.email_field = ft.TextField(
            label="Correo electrónico",
            border=ft.InputBorder.NONE,
            label_style=ft.TextStyle(color=APP_COLORS['text_secondary']),
            color="black",
            bgcolor=APP_COLORS['bginput'],
            width=400,
            on_change=self.validate_email
        )
        
        self.password_field = ft.TextField(
            label="Contraseña",
            border=ft.InputBorder.NONE,
            label_style=ft.TextStyle(color=APP_COLORS['text_secondary']),
            password=True,
            can_reveal_password=True,
            color="black",
            bgcolor=APP_COLORS['bginput'],
            width=400,
            on_change=self.validate_password
        )

        self.login_button = ft.ElevatedButton(
            "Iniciar sesión",
            bgcolor=APP_COLORS['accent_button'],
            color="black",
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=16),
                padding=ft.padding.symmetric(horizontal=18, vertical=12)
            ),
            on_click=self.handle_login
        )

        self.google_button = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="https://img.icons8.com/color/48/google-logo.png",
                        width=24,
                        height=24
                    ),
                    ft.Text("Iniciar sesión con Google", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="white",
            color="black",
            style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)),
            on_click=lambda _: self.page.go("/loginGoogle"),
            width=250,
        )

        self.facebook_button = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.icons.FACEBOOK, size=24, color="blue"),
                    ft.Text("Iniciar sesión con Facebook", size=16)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="white",
            color="black",
            style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)),
            on_click=lambda _: self.page.go("/loginFacebook"),
            width=270,
        )

    def build(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(
                                            text="Hola, bienvenidx a ",
                                            style=ft.TextStyle(color="black", size=30, weight=ft.FontWeight.BOLD),
                                        ),
                                        ft.TextSpan(
                                            text="Axo",
                                            style=ft.TextStyle(color=APP_COLORS['other'], size=30, weight=ft.FontWeight.BOLD),
                                        ),
                                        ft.TextSpan(
                                            text="Bank",
                                            style=ft.TextStyle(color=APP_COLORS['text_secondary'], size=30, weight=ft.FontWeight.BOLD),
                                        ),
                                    ]
                                ),
                                ft.Container(expand=True, height=20),
                                self.email_field,
                                self.password_field,
                                self.login_button,
                                ft.Text("o", color=APP_COLORS['text_secondary']),
                                ft.Row(
                                    controls=[self.google_button, self.facebook_button],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20
                                ),
                                ft.Text("¿Aún no tienes una cuenta?", color=APP_COLORS['text_secondary']),
                                ft.ElevatedButton(
                                    "Registrarse",
                                    color="black",
                                    bgcolor=APP_COLORS['accent_btn_sec'],
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(size=16),
                                        padding=ft.padding.symmetric(horizontal=18, vertical=12)
                                    ),
                                    on_click=lambda _: self.page.go("/signup")
                                ),
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
        )

    def validate_email(self, e):
        if not self.validation.is_valid_email(self.email_field.value):
            self.email_field.error_text = "Correo electrónico inválido"
        else:
            self.email_field.error_text = None
        self.email_field.update()

    def validate_password(self, e):
        if not self.validation.is_valid_password(self.password_field.value):
            self.password_field.error_text = "La contraseña debe tener al menos 8 caracteres, un número y un carácter especial"
        else:
            self.password_field.error_text = None
        self.password_field.update()

    def handle_login(self, e):
        is_email_valid = self.validation.is_valid_email(self.email_field.value)
        is_password_valid = self.validation.is_valid_password(self.password_field.value)

        if is_email_valid and is_password_valid:
            print("Has entrado exitosamente!")  # Para depuración
            self.page.go("/dashboard")
        else:
            if not is_email_valid:
                self.email_field.error_text = "Correo electrónico inválido"
            if not is_password_valid:
                self.password_field.error_text = "Contraseña inválida"
            self.email_field.update()
            self.password_field.update()
        self.update()  # Asegurarse de que la UI se actualice