import flet as ft
from Header import Header
from MenuPage import MenuPage


class MainPage(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.header = Header(self.page)
        self.menuPage = MenuPage(self.page)
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.change_page()

    def change_page(self):
        if self.header.selected_index == 0:
            self.controls = [
                self.header,
                self.menuPage
            ]

        if self.header.selected_index == 1:
            self.controls = [
                self.header,
                ft.Text("Кукусики")
            ]
