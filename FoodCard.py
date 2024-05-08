import flet as ft


class FoodCard():
    def __init__(self):
        pass

    def main(self, page: ft.Page):
        foodCard = self.container = ft.Container(
            ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=250,
                height=250,
                controls=[
                    ft.Image(
                        src=f"/images/kfc_logo.png"
                    ),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value="Название блюда"
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text(
                                        value="1000",
                                    ),
                                    ft.FilledButton(
                                        text="В корзину",
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(
                                                radius=10),
                                            bgcolor="#e31f2d"
                                        )
                                    )
                                ]
                            )
                        ]
                    ),
                ])
        )
        page.add(foodCard)


ft.app(
    target=FoodCard().main,
    assets_dir="assets"
)
