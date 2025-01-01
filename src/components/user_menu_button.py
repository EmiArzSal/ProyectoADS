import flet as ft

def user_menu_button(page: ft.Page, username: str):
    def logout(e):
        print("Cerrando sesión...")
        # Implementa la lógica de cierre de sesión aquí
        page.go("/login")

    def go_to_profile(e):
        print("Navegando al perfil...")
        # Implementa la navegación al perfil aquí
        page.go("/profile")

    return ft.PopupMenuButton(
        icon=ft.Icons.ACCOUNT_CIRCLE,
        icon_size=35,
        tooltip=f"Menú de {username}",
        items=[
            ft.PopupMenuItem(text=f"Conectado como {username}", disabled=True),
            ft.PopupMenuItem(),  # Divisor
            ft.PopupMenuItem(text="Perfil", icon=ft.Icons.PERSON, on_click=go_to_profile),
            ft.PopupMenuItem(),  # Divisor
            ft.PopupMenuItem(text="Cerrar sesión", icon=ft.Icons.LOGOUT, on_click=logout),
        ],
    )

