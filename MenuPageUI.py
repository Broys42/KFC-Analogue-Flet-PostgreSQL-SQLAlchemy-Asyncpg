import flet as ft
from MenuItemUI import MenuItemUI
from ViewModel import ViewModel


class MenuPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.height = page.height
        self.width = 1440

        self.page.on_resize = self.on_page_resize

        self.title = ft.Text(
            value="Меню",
            font_family="SF-Pro-Display-Black",
            size=30
        )

        self.title_Row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.title,
                ft.Text()
            ]
        )

        self.cards_Of_Food = ft.Row(
            wrap=True,
            spacing=146,
            run_spacing=50,
            controls=[]
        )

        self.food_list = ft.ListView(
            width=1440,
            expand=1,
            controls=[
                self.cards_Of_Food
            ]
        )

        self.controls = [
            self.title_Row,
            self.food_list
        ]

    def on_page_resize(self, e):
        self.height = self.page.height
        self.page.update()
