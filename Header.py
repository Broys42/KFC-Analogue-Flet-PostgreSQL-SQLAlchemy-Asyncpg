import flet as ft


class Header():
    def __init__(self):
        self.selected_index = 0

    def main(self, page: ft.Page):
        self.edit_flag = False

        def change_selected_index(e, key):
            for index, tab in enumerate(self.tabs):
                if index == key:
                    tab.style.color[ft.MaterialState.DEFAULT] = "#e31f2d"
                else:
                    tab.style.color[ft.MaterialState.DEFAULT] = "black"
            page.update()

        self.kfc_logo = ft.Image(src=f"/images/kfc_logo.png")

        self.menu_tab = ft.TextButton(
            text="Меню",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: "#e31f2d",
                    ft.MaterialState.DEFAULT: "#e31f2d"
                }),
            on_click=lambda e: change_selected_index(e=e, key=0)
        )

        self.users_tab = ft.TextButton(
            text="Пользователи",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: "#e31f2d",
                    ft.MaterialState.DEFAULT: "black"
                }),
            on_click=lambda e: change_selected_index(e=e, key=1)
        )

        self.turnON_edit_btn = ft.FilledButton(
            text="Включить редактирование",
            style=ft.ButtonStyle(
                shape=ft.StadiumBorder(),
                bgcolor="#e31f2d"
            ),
            on_click=lambda e: click_turnON_edit_btn(e=e)
        )

        def click_turnON_edit_btn(e: ft.ControlEvent):
            if self.edit_flag:
                self.edit_flag = False
                e.control.text = "Включить редактирование"
                page.update()
            else:
                self.edit_flag = True
                e.control.text = "Отключить редактирование"
                page.update()

        self.tabs = [self.menu_tab, self.users_tab]

        self.header_tabs = ft.Row(
            height=30,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            width=150,
            controls=[
                self.kfc_logo,
                self.menu_tab,
                self.users_tab
            ]
        )

        self.header = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(),
                self.header_tabs,
                self.turnON_edit_btn
            ]
        )
        page.add(self.header)
