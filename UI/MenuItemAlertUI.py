import flet as ft
from UI.MenuItemUI import MenuItemUI


class MenuItemAlertUI(ft.AlertDialog):
    def __init__(self, page):
        super().__init__()
        self.modal = True
        self.page = page
        self.menuItem : MenuItemUI

        self.title = ft.Text("Редактировать позицию")
        self.content = ft.Column(
            height=300,
            controls=[]
        )

        self.save_changes_btn = ft.TextButton("Сохранить изменения")
        self.close_dlg_btn = ft.TextButton("Выйти")

        self.actions = [
            self.save_changes_btn,
            self.close_dlg_btn,
        ]

    def update_ui(self):
        self.name_ui = ft.Text("Изменить имя")
        self.name_textfield = ft.TextField(self.menuItem.name)
        self.price_ui = ft.Text("Изменить цену")
        self.price_textfield = ft.TextField(str(self.menuItem.price))
        self.image_ui = ft.Text("Изменить изображение")
        self.image_textfield = ft.TextField(self.menuItem.image)

    def change_menuItem(self, menuItem):
        self.menuItem = menuItem
        self.change_content()

    def change_content(self):
        self.update_ui()
        self.content.controls = [
            self.name_ui,
            self.name_textfield,
            self.price_ui,
            self.price_textfield,
            self.image_ui,
            self.image_textfield,
        ]
        self.page.update()


    def set_page_alert(self):
        self.page.dialog = self
        self.page.update()
