import flet as ft


class FoodCardEditAlert(ft.AlertDialog):
    def __init__(self, page):
        super().__init__()
        self.open = False
        self.page = page

        self.title = ft.Text("Редактировать позицию")
        self.content = ft.Column(
            height=300,
            controls=[]
        )

        self.actions = [
            ft.TextButton("Yes", on_click=self.close_dlg),
            ft.TextButton("No", on_click=self.close_dlg),
        ]

    def change_content(self, name, price, image):
        self.content.controls = [
            ft.Text("Название блюда"),
            ft.TextField(name),
            ft.Text("Цена блюда"),
            ft.TextField(price),
            ft.Text("Изображение"),
            ft.TextField(image),
        ]

    def change_title(self, name):
        self.title = ft.Text(name)

    #Abstract
    def close_dlg(self, e):
        self.open = False
        self.page.update()

    #Abstract
    def open_dlg(self, e):
        self.open = True
        self.page.update()
