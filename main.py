import flet as ft
from MainPage import MainPage

def main(page: ft.Page):
    page.fonts = {
        "SF-Pro-Display-Black": "/fonts/SF-Pro-Display-Black.otf",
        "SF-Pro-Display-Bold": "/fonts/SF-Pro-Display-Bold.otf",
        "SF-Pro-Display-Heavy": "/fonts/SF-Pro-Display-Heavy.otf",
        "SF-Pro-Display-Light": "/fonts/SF-Pro-Display-Light.otf",
        "SF-Pro-Display-Medium": "/fonts/SF-Pro-Display-Medium.otf",
        "SF-Pro-Display-Regular": "/fonts/SF-Pro-Display-Regular.otf",
        "SF-Pro-Display-SemiboldItalic": "/fonts/SF-Pro-Display-SemiboldItalic.otf",
        "SF-Pro-Display-ThinItalic": "/fonts/SF-Pro-Display-ThinItalic.otf",
        "SF-Pro-Display-Ultralight": "/fonts/SF-Pro-Display-Ultralight.otf"
    }
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(MainPage(page))

ft.app(
    target=main,
    assets_dir="assets"
)
