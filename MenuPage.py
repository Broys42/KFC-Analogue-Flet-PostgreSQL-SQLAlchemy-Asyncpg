import flet as ft
from FoodCard import FoodCard


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

        self.titleRow = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.title,
                ft.Text()
            ]
        )

        self.cardsOfFood = ft.Row(
            wrap=True,
            spacing=100,
            run_spacing=50,
            controls=self.cardsOfFoodControls()
        )

        self.food = ft.ListView(
            expand=1,
            controls=[
                self.cardsOfFood
            ]
        )

        self.controls = [
            self.titleRow,
            self.food
        ]

    def cardsOfFoodControls(self):
        items = []
        for i in range(30):
            items.append(
                FoodCard(page=self.page, name="Привет", price="3000", image="")
            )
        return items

    def on_page_resize(self, e):
        self.height = self.page.height
        self.page.update()
