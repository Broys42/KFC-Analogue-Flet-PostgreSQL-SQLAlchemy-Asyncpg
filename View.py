import asyncio
import flet as ft
from UI.WindowUI import WindowUI
from ViewModel import ViewModel
from UI.MainPageUI import MainPageUI
from UI.HeaderUI import HeaderUI
from UI.MenuPageUI import MenuPage
from UI.UsersPageUI import UsersPageUI
from UI.UserCardUI import UserCardUI
from UI.MenuItemUI import MenuItemUI
from entities.MenuItem import MenuItem
from UI.MenuItemAlertUI import MenuItemAlertUI


class View():
    def __init__(self, viewModel: ViewModel):
        self.viewModel = viewModel

    async def show(self):
        await ft.app_async(
            target=self.main,
            assets_dir="assets"
        )

    async def main(self, page: ft.Page):
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

        self.set_menuItemAlert()
        self.set_userCard()
        self.set_header()
        self.set_userPage()
        self.set_menuPage()
        await self.set_menu_cards_for_menuPage()
        self.set_mainPage()
        self.set_mainWindow()

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.add(self.main_Window)

    def get_menuItemUI(self, menuItem: MenuItem):
        menuItemUI = MenuItemUI(
            name=menuItem.name,
            price=menuItem.price,
            image=menuItem.image,
            item_id=menuItem.item_id)
        menuItemUI.click_on_edit = self.click_on_edit_in_menu_item
        # menuItemUI.change_image(image=menuItem.image)
        return menuItemUI

    def set_userCard(self):
        self.userCard = UserCardUI(
            name="User",
            image="asdsa")

    def set_menuItemAlert(self):
        self.menu_item_alert = MenuItemAlertUI(self.page)
        self.menu_item_alert.save_changes_btn.on_click = self.click_save_menuItem_changes
        self.menu_item_alert.close_dlg_btn.on_click = self.click_close_dlg
        self.page.dialog = self.menu_item_alert
        self.page.update()

    def set_header(self):
        self.header = HeaderUI(page=self.page)
        self.header.change_selected_tab = self.clicked_on_tab_in_header

    def set_menuPage(self):
        self.menu_Page = MenuPage(page=self.page)

    def set_userPage(self):
        self.user_Page = UsersPageUI(page=self.page)
        self.set_users_cards_for_userPage()

    def set_mainPage(self):
        self.main_Page = MainPageUI(page=self.page, controls=self.get_mainPage_controls(
            self.viewModel.get_selected_tab()))

    def set_mainWindow(self):
        self.main_Window = WindowUI(page=self.page, content=self.main_Page)

    async def set_menu_cards_for_menuPage(self):
        self.menu_Page.cards_Of_Food.controls = await self.get_menu_cards_for_menuPage()
        self.page.update()

    def set_users_cards_for_userPage(self):
        self.user_Page.cards_of_User.controls = self.get_user_cards_for_userPage()
        self.page.update()

    async def get_menu_cards_for_menuPage(self):
        items = []
        await self.viewModel.get_menuitems_model_from_database()
        for menuItem in self.viewModel.get_menuItemsModel().values():
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

    def click_on_edit_in_menu_item(self, e, menuItemUI):
        self.menu_item_alert.change_menuItem(menuItemUI)
        self.menu_item_alert.open = True
        self.page.update()

    def click_close_dlg(self, e):
        self.menu_item_alert.open = False
        self.page.update()

    async def click_save_menuItem_changes(self, e):
        item_id = self.menu_item_alert.menuItem.item_id

        #Changes parameters
        name = self.menu_item_alert.name_textfield.value
        price = self.menu_item_alert.price_textfield.value
        image = self.menu_item_alert.image_textfield.value

        await self.viewModel.update_menuItem(item_id=item_id, name=name, price=int(price), image=image)
        await self.set_menu_cards_for_menuPage()
        self.menu_item_alert.open = False
        self.page.update()
