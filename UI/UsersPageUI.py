import flet as ft
from UI.MenuItemUI import MenuItemUI
from ViewModel import ViewModel


class UsersPageUI(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.height = page.height
        self.width = 1440

        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page.on_resize = self.on_page_resize

        self.title = ft.Text(
            value="Пользователи",
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

        self.cards_of_User = ft.Row(
            wrap=True,
            spacing=146,
            run_spacing=100,
            controls=[]
        )

        self.user_list = ft.ListView(
            expand=1,
            controls=[
                self.cards_of_User
            ]
        )

        self.controls = [
            self.title_Row,
            self.user_list
        ]

    def on_page_resize(self, e):
        self.height = self.page.height
        self.page.update()
