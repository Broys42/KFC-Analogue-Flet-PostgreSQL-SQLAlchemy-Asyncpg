import flet as ft


class MenuItemUI(ft.Column):
    def __init__(self, name, price, image, item_id):
        super().__init__()
        self.name = name
        self.price = price
        self.image = image
        self.item_id = item_id

        self.width = 250
        # self.height = 400
        self.spacing = 15
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.name_Text = ft.Text(
            text_align=ft.TextAlign.CENTER,
            value=self.name,
            size=20,
            height=70,
            font_family="SF Pro Display Medium",
        )

        self.price_Text = ft.Text(
            value=str(self.price) + "₽",
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
                e=e, menuItemUI=self)
        )

        self.price_and_button = ft.Row(
            width=250,
            vertical_alignment=ft.CrossAxisAlignment.END,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.price_Text,
                self.edit_button
            ]
        )

        self.food_Image = ft.Image(
            height=200,
            width=250,
            fit=ft.ImageFit.CONTAIN,
            src=f"/images/food/{image}.png"
        )

        self.controls = [
            self.food_Image,
            self.name_Text,
            self.price_and_button
        ]

    # Abstract
    def click_on_edit(self, e, menuItemUI):
        pass
