import flet as ft
from screens.auth.login import Login
from screens.auth.signup import signUp
from screens.auth.loginGoogle import loginGoogle
from screens.dashboard.dashboard import Dashboard
from screens.dashboard.gastos import Gastos
from screens.dashboard.ingresos import Ingresos
from utils.constants import APP_COLORS

def views_handler(page):
    return {
        "/login": ft.View(
            route="/login",
            bgcolor="white",
            padding=0,
            controls=[
                Login(page)
            ]
        ),
        "/signup": ft.View(route="/signup", bgcolor="white",
            padding=0,
            controls=[
            signUp(page)
        ]),
        "/loginGoogle": ft.View(route="/loginGoogle", bgcolor="white",controls=[
            loginGoogle(page)
        ]),
        "/dashboard": ft.View(route="/dashboard",controls=[
            Dashboard(page)
        ]),
        "/gastos": ft.View(route="/gastos",controls=[
                Gastos(page)
        ]),
        "/ingresos": ft.View(route="/ingresos",controls=[
                Ingresos(page)
        ]),
    }