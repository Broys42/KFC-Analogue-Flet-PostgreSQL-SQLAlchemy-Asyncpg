import flet as ft
from UI.MainPageUI import MainPageUI
from mvvm.ViewModel import ViewModel

class WindowUI(ft.Container):
    def __init__(self, page: ft.Page, content: MainPageUI):
        super().__init__()
        self.page = page
        self.content = content
