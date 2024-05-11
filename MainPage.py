import flet as ft
from Header import Header
from MenuPage import MenuPage
from ViewModel import ViewModel


class MainPage(ft.Column):
    def __init__(self, page: ft.Page, controls: ft.Column.controls):
        super().__init__()
        self.page = page
        self.controls = controls
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def change_page(self, index):
        pass
