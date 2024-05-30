import flet as ft


class UserCard(ft.Row):
    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image

        self.height = 200
        self.width = 647
        self.spacing = 20
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        self.user_name = ft.Text(
            text_align=ft.TextAlign.CENTER,
            value=self.name,
            size=20,
            font_family="SF Pro Display Medium",
        )

        self.about_user_btn = ft.FilledButton(
            text="О пользователе",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=10),
                bgcolor="#e31f2d"
            ),
            on_click=lambda e: self.click_on_edit(
                e=e, name=self.name, price=self.price, image=self.image)
        )

        self.user_info_clmn = ft.Column(
            height=100,
            width=200,
            horizontal_alignment=ft.CrossAxisAlignment.END,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.user_name,
                self.about_user_btn
            ]
        )

        self.user_avatar = ft.CircleAvatar(
            height=300,
            width=300,
            content=ft.Image(
                fit=ft.ImageFit.FIT_WIDTH,
                src=f"/images/food/chicken_cake.png"
            )
        )

        self.controls = [
            self.user_avatar,
            self.user_info_clmn
        ]

    # Abstract
    def click_on_edit(self, e, name, price, image):
        pass
