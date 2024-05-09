import flet as ft
from MainPage import MainPage


class MainWindow(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.content = MainPage(page)
