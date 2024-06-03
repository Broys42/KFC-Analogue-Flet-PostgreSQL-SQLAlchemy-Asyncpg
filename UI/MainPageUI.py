import flet as ft
from UI.HeaderUI import HeaderUI
from UI.MenuPageUI import MenuPage
from mvvm.ViewModel import ViewModel


class MainPageUI(ft.Column):
    def __init__(self, page: ft.Page, controls: ft.Column.controls):
        super().__init__()
        self.page = page
        self.controls = controls
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def change_page(self, index):
        pass
