import flet as ft

class Header():
    def __init__(self):
        self.selected_index=0

    def main(self, page: ft.Page):
        def change_selected_index(e, key):
            print(page.width)
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

        self.turnON_edit_btn = ft.TextButton("Включить редактирование")

        self.tabs=[self.menu_tab, self.users_tab]
        self.container = ft.Container(
            bgcolor = None
        )

        self.header_tabs = ft.Row(
            height=30,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.kfc_logo,
                self.menu_tab,
                self.users_tab
                ]
            )

        self.header = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(),
                self.header_tabs,
                self.turnON_edit_btn
            ]
        )

        page.add(self.header)

ft.app(
    target=Header().main,
    assets_dir="assets"
)
