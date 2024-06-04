import flet as ft
from UI.MenuItemUI import MenuItemUI
from mvvm.ViewModel import ViewModel


class MenuPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.width = 1440
        self.height = self.page.height

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

        self.cards_Of_menu_items = ft.Row(
            wrap=True,
            spacing=146,
            run_spacing=50,
            controls=[]
        )

        self.download_app_banner_image = ft.Image(
            width=1440,
            fit=ft.ImageFit.COVER,
            src=f"/images/banners/banner 1.jpg"
        )

        # self.gift_banner_image = ft.Image(
        #     width=1440,
        #     fit=ft.ImageFit.COVER,
        #     src=f"/images/banners/banner 2.jpg"
        # )

        self.menu_page_list = ft.ListView(
            expand=1,
            controls=[
                self.download_app_banner_image,
                self.cards_Of_menu_items,
                # self.gift_banner_image
            ]
        )

        self.controls = [
            self.title_Row,
            self.menu_page_list,
        ]

    def on_page_resize(self, e):
        self.height = self.page.height
        self.page.update()
