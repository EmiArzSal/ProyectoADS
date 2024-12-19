import flet as ft
from screens.auth.login import Login
from screens.auth.signup import signUp
from screens.auth.loginGoogle import loginGoogle
from utils.constants import APP_COLORS

def views_handler(page):
    bckcolor = APP_COLORS['background']
    return {
        "/login": ft.View(
            route="/login",
            bgcolor=bckcolor,
            controls=[
                ft.Container(
                    content=Login(page),
                    expand=True,
                    image=ft.Image(
                        src="/assets/imagebg.png",
                        fit=ft.ImageFit.COVER
                    )
                )
            ]
        ),
        "/signup": ft.View(route="/signup", bgcolor=bckcolor,controls=[
            signUp(page)
        ]),
        "/loginGoogle": ft.View(route="/loginGoogle", bgcolor=bckcolor,controls=[
            loginGoogle(page)
        ])
    }