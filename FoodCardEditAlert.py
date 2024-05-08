import flet as ft


class FoodCardEditAlert(ft.AlertDialog):
    def __init__(self, name, price, image, page):
        super().__init__()
        self.name = name
        self.price = price
        self.image = image
        self.open = False
        self.page = page

        self.title = ft.Text("Редактирование позиции")
        self.content = ft.Text(self.name)
        self.actions = [
            ft.TextButton("Yes", on_click=self.close_dlg),
            ft.TextButton("No", on_click=self.close_dlg),
        ]

    def close_dlg(self, e):
        self.open = False
        self.page.update()

    def open_dlg(self, e):
        self.open = False
        self.page.update()
