import flet as ft
from MainPage import MainPage
from ViewModel import ViewModel


class Window(ft.Container):
    def __init__(self, page: ft.Page, content: MainPage):
        super().__init__()
        self.page = page
        self.content = content
