from abc import abstractmethod
import flet as ft
from FoodCardEditAlert import FoodCardEditAlert


class FoodCard(ft.Column):
    def __init__(self, page, name, price, image):
        super().__init__()
        self.page = page
        self.name = name
        self.price = price
        self.image = image

        self.width = 250
        self.spacing = 30

        self.foodNameText = ft.Text(
            text_align=ft.TextAlign.CENTER,
            value=self.name,
            size=20,
            font_family="SF Pro Display Medium",
        )

        self.priceText = ft.Text(
            value=self.price + "₽",
            size=20,
            font_family="SF Pro Display Bold",
        )

        self.edit_button = ft.FilledButton(
            text="Редактировать",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=10),
                bgcolor="#e31f2d"
            ),
            on_click=lambda e: self.click_on_edit(
                e=e)
        )

        self.priceAndButton = ft.Row(
            width=250,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.priceText,
                self.edit_button
            ]
        )

        self.foodImage = ft.Image(
            fit=ft.ImageFit.FIT_WIDTH,
            src=f"/images/food/chicken_cake.png"
        )

        self.controls=[
                self.foodImage,
                self.foodNameText,
                self.priceAndButton
            ]

    def click_on_edit(self, e):
        self.alert = FoodCardEditAlert(
            self.name, self.price, self.image, page=self.page)
        self.page.dialog = self.alert
        self.alert.open = True
        self.page.update()
