import flet as ft
from utils.constants import APP_COLORS

def Sidebar(page: ft.Page):
    sidebarcolor = APP_COLORS['sidebar']  # Color rosado para el sidebar

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
                        tooltip=label,
                        on_click=navigate
                    ),
                    ft.Text(label, color="white", size=12, text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            width=100  # Ancho fijo para los elementos de navegación
        )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("CashWise", color="white", size=20, weight="bold"),
                ft.Container(height=30),  # Espacio después del título
                create_nav_item(ft.Icons.DASHBOARD, "Dashboard", "/dashboard"),
                create_nav_item(ft.Icons.ACCOUNT_BALANCE_WALLET, "Ingresos", "/ingresos"),
                create_nav_item(ft.Icons.SHOPPING_CART, "Gastos", "/gastos"),
                create_nav_item(ft.Icons.BAR_CHART, "Gráficos", "/graficos"),
                create_nav_item(ft.Icons.SETTINGS, "Ajustes", "/ajustes"),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        ),
        width=120,
        bgcolor=sidebarcolor,
        padding=ft.padding.only(top=20, left=10, right=10),
    )