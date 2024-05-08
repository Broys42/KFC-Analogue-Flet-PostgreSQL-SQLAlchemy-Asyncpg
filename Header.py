import flet as ft
from FoodCard import FoodCard
from FoodCardEditAlert import FoodCardEditAlert


class Header(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.selected_index = 0
        self.page = page

        self.kfc_logo = ft.Image(src=f"/images/kfc_logo.png")

        self.menu_tab = ft.TextButton(
            text="Меню",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: "#e31f2d",
                    ft.MaterialState.DEFAULT: "#e31f2d"
                }),
            on_click=lambda e: self.change_selected_index(
                e=e, key=0)
        )

        self.users_tab = ft.TextButton(
            text="Пользователи",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: "#e31f2d",
                    ft.MaterialState.DEFAULT: "black"
                }),
            on_click=lambda e: self.change_selected_index(
                e=e, key=1)
        )

        self.tabs = [self.menu_tab, self.users_tab]

        self.height = 30
        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 20
        self.controls = [
            self.kfc_logo,
            self.menu_tab,
            self.users_tab
        ]

    def change_selected_index(self, e, key):
        self.selected_index = key
        print(self.selected_index)
        for index, tab in enumerate(self.tabs):
            if index == key:
                tab.style.color[ft.MaterialState.DEFAULT] = "#e31f2d"
            else:
                tab.style.color[ft.MaterialState.DEFAULT] = "black"
        self.page.update()
