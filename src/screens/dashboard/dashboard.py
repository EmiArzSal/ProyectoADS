import flet as ft
from components.sidebar import Sidebar
from components.user_menu_button import user_menu_button

def Dashboard(page: ft.Page):
    def logout(e):
        print("Cerrando sesión...")
        # Implementa la lógica de cierre de sesión aquí
        page.go("/login")

    # Main content
    main_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Dashboard", color="black", size=24, weight="bold"),
                        ft.Container(expand=True),  # Espaciador flexible
                        user_menu_button(page, "Usuario"), # Debe de tomar el nombre del usuario logueado de la base de datos en firebase
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=20),  # Espacio después del encabezado
                ft.Text("Contenido principal del dashboard", color="black", size=16),
                # Agrega más contenido según sea necesario
            ],
            spacing=0,
            expand=True,
        ),
        padding=20, 
        expand=True,
        bgcolor=ft.Colors.WHITE,
    )

    # Main layout
    return ft.Container(
        content=ft.Row(
            controls=[
                Sidebar(page),
                ft.VerticalDivider(width=1, color=ft.Colors.BLACK26),
                main_content,
            ],
            spacing=0,
            expand=True,
        ),
        expand=True,
    )

