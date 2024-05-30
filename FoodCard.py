import flet as ft
from FoodCardEditAlert import FoodCardEditAlert


class FoodCard(ft.Column):
    def __init__(self, name, price, image):
        super().__init__()
        self.name = name
        self.price = price
        self.image = image

        self.width = 250
        self.height = 450
        self.spacing = 30
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.food_Name = ft.Text(
            text_align=ft.TextAlign.CENTER,
            value=self.name,
            size=20,
            font_family="SF Pro Display Medium",
        )

        self.price_Text = ft.Text(
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
                e=e, name=self.name, price=self.price, image=self.image)
        )

        self.price_and_button = ft.Row(
            width=250,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.price_Text,
                self.edit_button
            ]
        )

        self.food_Image = ft.Image(
            fit=ft.ImageFit.FIT_WIDTH,
            src=f"/images/food/chicken_cake.png"
        )

        self.controls = [
            self.food_Image,
            self.food_Name,
            self.price_and_button
        ]

    # Abstract
    def click_on_edit(self, e, name, price, image):
        pass
