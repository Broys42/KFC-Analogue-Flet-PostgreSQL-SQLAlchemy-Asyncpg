import flet as ft


class FoodCard():
    def __init__(self):
        pass

    def main(self, page: ft.Page):
        page.fonts = {
            "SF Pro Display Black": "/fonts/SF-Pro-Display-Black.otf",
            "SF Pro Display Bold": "/fonts/SF-Pro-Display-Bold.otf",
            "SF Pro Display Heavy": "/fonts/SF-Pro-Display-Heavy.otf",
            "SF Pro Display Light": "/fonts/SF-Pro-Display-Light.otf",
            "SF Pro Display Medium": "/fonts/SF-Pro-Display-Medium.otf",
            "SF Pro Display Regular": "/fonts/SF-Pro-Display-Regular.otf",
            "SF Pro Display Semibold": "/fonts/SF-Pro-Display-Semibold.otf",
            "SF Pro Display Ultralight": "/fonts/SF-Pro-Display-Ultralight.otf",
        }

        foodCard = self.container = ft.Container(
            ft.Column(
                spacing=30,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=250,
                height=500,
                controls=[
                    ft.Image(
                        src=f"/images/food/chicken_cake.png"
                    ),
                    ft.Column(
                        spacing=30,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                text_align=ft.TextAlign.CENTER,
                                value="Маэстро чизбургер делюкс hot",
                                size=20,
                                font_family="SF Pro Display Medium",
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text(
                                        value="1000" + "₽",
                                        size=20,
                                        font_family="SF Pro Display Bold",
                                    ),
                                    ft.FilledButton(
                                        text="Редактировать",
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
