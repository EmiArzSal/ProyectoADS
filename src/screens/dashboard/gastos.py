#Here it will be the code for the gastos screen (expenses) of the dashboard, this screen will show the expenses of the user and the user will be able to add new expenses, filter them by date, month and last year, also the user will be able to delete them.

import flet as ft
from components.sidebar import Sidebar
from components.user_menu_button import user_menu_button


def Gastos(page: ft.Page):
    def create_nav_item(icon, label, route):
        def navigate(e):
            page.go(route)
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.IconButton(
                        icon=icon,
                        icon_color="white",
                        icon_size=30,
                        on_click=navigate
                    ),
                    ft.Text(label, color="white",
                      size=15,
                      text_align=ft.TextAlign.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            width=100  # Ancho fijo para los elementos de navegación
        )
    # Crear opciones para el dropdown
    dropdown_options = [
            ft.dropdown.Option(text="Ultima quincena", key="1"),
            ft.dropdown.Option(text="Ultimo mes", key="2"),
            ft.dropdown.Option(text="Ultimo año", key="3"),
    ]

    # Crear el dropdown
    dropdown = ft.Dropdown(
            options=dropdown_options,
            value="1",  # Valor por defecto
            on_change=lambda e: print(f"Selected: {e.control.value}"),
    )

    # Main content
    main_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Gastos", color="black", size=24, weight="bold"),
                        ft.Container(expand=True),  # Espaciador flexible
                        user_menu_button(page, "Usuario"), # Debe de tomar el nombre del usuario logueado de la base de datos en firebase
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=20),  # Espacio después del encabezado
                ft.Text("Contenido principal de los gastos", color="black", size=16),
                # Agrega más contenido según sea necesario
                ft.Container(
                    content=ft.Row(
                        controls=[
                            
                            ft.Text("Filtrar por:", color="black", size=16),
                            dropdown,
                            ft.Container(expand=True),  # Espaciador flexible
                            ft.Button(
                                text="Añadir gasto",
                                color=ft.Colors.PRIMARY,
                                on_click=lambda _: print("Añadiendo gasto..."),
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=ft.padding.all(10),
                ),
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
                Sidebar(page),  # Pasamos la referencia de page al Sidebar
                ft.VerticalDivider(width=1, color=ft.Colors.BLACK26),
                main_content,
            ],
            spacing=0,
            expand=True,
        ),
        expand=True,
    )
