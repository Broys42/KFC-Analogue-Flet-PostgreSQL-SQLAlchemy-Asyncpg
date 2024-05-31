import flet as ft
from Window import Window
from ViewModel import ViewModel
from MainPageUI import MainPageUI
from HeaderUI import HeaderUI
from MenuPageUI import MenuPage
from UsersPageUI import UsersPageUI
from UserCardUI import UserCardUI
from MenuItemUI import MenuItemUI
from MenuItem import MenuItem
from MenuItemAlertUI import MenuItemAlertUI


class View():
    def __init__(self, viewModel: ViewModel):
        self.viewModel = viewModel
        ft.app(
            target=self.main,
            assets_dir="assets"
        )

    def main(self, page: ft.Page):
        page.fonts = {
            "SF-Pro-Display-Black": "/fonts/SF-Pro-Display-Black.otf",
            "SF-Pro-Display-Bold": "/fonts/SF-Pro-Display-Bold.otf",
            "SF-Pro-Display-Heavy": "/fonts/SF-Pro-Display-Heavy.otf",
            "SF-Pro-Display-Light": "/fonts/SF-Pro-Display-Light.otf",
            "SF-Pro-Display-Medium": "/fonts/SF-Pro-Display-Medium.otf",
            "SF-Pro-Display-Regular": "/fonts/SF-Pro-Display-Regular.otf",
            "SF-Pro-Display-SemiboldItalic": "/fonts/SF-Pro-Display-SemiboldItalic.otf",
            "SF-Pro-Display-ThinItalic": "/fonts/SF-Pro-Display-ThinItalic.otf",
            "SF-Pro-Display-Ultralight": "/fonts/SF-Pro-Display-Ultralight.otf"
        }
        self.page = page

        self.set_foodCardAlert()
        self.set_userCard()
        self.set_header()
        self.set_userPage()
        self.set_menuPage()
        self.set_mainPage()
        self.set_mainWindow()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.add(self.main_Window)

    def get_menuItemUI(self, menuItem: MenuItem):
        menuItemUI = MenuItemUI(
            name=menuItem.name,
            price=menuItem.price,
            image=menuItem.image)
        menuItemUI.click_on_edit = self.click_on_edit_in_foodCard
        # menuItemUI.change_image(image=menuItem.image)
        return menuItemUI

    def set_userCard(self):
        self.userCard = UserCardUI(
            name="User",
            image="asdsa")

    def set_foodCardAlert(self):
        self.food_card_alert = MenuItemAlertUI(page=self.page)
        self.page.dialog = self.food_card_alert
        self.page.update()

    def set_header(self):
        self.header = HeaderUI(page=self.page)
        self.header.change_selected_tab = self.clicked_on_tab_in_header

    def set_menuPage(self):
        self.menu_Page = MenuPage(page=self.page)
        self.set_menu_cards_for_menuPage()

    def set_userPage(self):
        self.user_Page = UsersPageUI(page=self.page)
        self.set_users_cards_for_userPage()

    def set_mainPage(self):
        self.main_Page = MainPageUI(page=self.page, controls=self.get_mainPage_controls(
            self.viewModel.get_selected_tab()))

    def set_mainWindow(self):
        self.main_Window = Window(page=self.page, content=self.main_Page)

    def set_menu_cards_for_menuPage(self):
        self.menu_Page.cards_Of_Food.controls = self.get_menu_cards_for_menuPage()
        self.page.update()

    def set_users_cards_for_userPage(self):
        self.user_Page.cards_of_User.controls = self.get_user_cards_for_userPage()
        self.page.update()

    def get_menu_cards_for_menuPage(self):
        items = []
        for menuItem in self.viewModel.get_menuModel():
            items.append(
                self.get_menuItemUI(menuItem)
            )
        return items

    def get_user_cards_for_userPage(self):
        items = []
        for i in range(30):
            items.append(
                self.userCard
            )
        return items

    def get_mainPage_controls(self, index):
        self.viewModel.change_selected_tab = index
        if index == 0:
            return [
                self.header,
                self.menu_Page
            ]

        if index == 1:
            return [
                self.header,
                self.user_Page
            ]

    def clicked_on_tab_in_header(self, e, key):
        self.selected_index = key
        for index, tab in enumerate(self.header.tabs):
            if index == key:
                tab.style.color[ft.MaterialState.DEFAULT] = "#e31f2d"
                self.main_Page.controls = self.get_mainPage_controls(index)
            else:
                tab.style.color[ft.MaterialState.DEFAULT] = "black"
        self.page.update()

    def click_on_edit_in_foodCard(self, e, name, price, image):
        self.food_card_alert.change_content(name=name, price=price, image=image)
        self.food_card_alert.open = True
        self.page.update()

    def close_dlg(self, e):
        self.food_card_alert.close_dlg()
        self.food_card_alert.update()
        self.page.update()

    def open_dlg(self, e):
        self.food_card_alert.open_dlg()
        self.food_card_alert.update()
        self.page.update()
