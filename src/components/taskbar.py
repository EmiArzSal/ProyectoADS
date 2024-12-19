import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Barra de navegación lateral"
    page.window_width = 800
    page.window_height = 600

    # Controlador del estado de navegación
    def on_nav_change(e):
        page.views.clear()
        if e.control.selected_index == 0:
            page.views.append(view_home)
        elif e.control.selected_index == 1:
            page.views.append(view_profile)
        elif e.control.selected_index == 2:
            page.views.append(view_settings)
        page.update()

    # Vistas para cada sección
    view_home = ft.View(
        "/home",
        [
            ft.Text("Inicio", size=30),
            ft.Text("Bienvenido a la página principal."),
        ],
    )
    view_profile = ft.View(
        "/profile",
        [
            ft.Text("Perfil", size=30),
            ft.Text("Esta es tu página de perfil."),
        ],
    )
    view_settings = ft.View(
        "/settings",
        [
            ft.Text("Configuración", size=30),
            ft.Text("Configura las preferencias de la aplicación."),
        ],
    )

    # Barra de navegación lateral
    nav_rail = ft.NavigationRail(
        selected_index=0,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                selected_icon=ft.icons.HOME_OUTLINED,
                label="Inicio",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON,
                selected_icon=ft.icons.PERSON_OUTLINE,
                label="Perfil",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS,
                selected_icon=ft.icons.SETTINGS_OUTLINED,
                label="Configuración",
            ),
        ],
    )

    # Layout principal
    page.add(
        ft.Row(
            [
                nav_rail,  # Barra de navegación lateral
                ft.VerticalDivider(width=1),  # Línea divisoria
                ft.Column(
                    expand=True, 
                    controls=[view_home],  # Vista inicial
                ),
            ],
            expand=True,
        )
    )

ft.app(target=main)
