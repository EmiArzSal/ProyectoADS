import flet as ft
from screens.auth.login import login
from screens.auth.signup import signUp
from utils.constants import APP_COLORS

def views_handler(page):
    bckcolor = APP_COLORS['background']
    return {
        "/login": ft.View(route="/login",bgcolor=bckcolor, decoration=ft.BoxDecoration(image=ft.DecorationImage(src="assets/imagebg.png", fit=ft.ImageFit.COVER)), controls=[
            login(page)
        ]),
        "/signup": ft.View(route="/signup", controls=[
            signUp(page)
        ])
    }