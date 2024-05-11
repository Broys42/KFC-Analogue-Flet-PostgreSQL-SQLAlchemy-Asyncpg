import flet as ft
from Window import Window
from ViewModel import ViewModel
from MainPage import MainPage
from Header import Header
from MenuPage import MenuPage
from FoodCard import FoodCard


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

        self.set_Header(page=page)
        self.set_menuPage(page=page)
        self.set_mainPage(page=page)
        self.set_mainWindow(page=page)

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.add(self.mainWindow)

    def set_foodCard(self, page):
        self.foodCard = FoodCard(
            page=self.page,
            name="Privet",
            price="1000",
            image="asdsa")

    def set_Header(self, page):
        self.header = Header(page=page)
        self.header.change_selected_tab = self.clicked_on_tab_in_header

    def set_mainPage(self, page):
        self.mainPage = MainPage(page=page, controls=self.get_mainPage_controls(
            self.viewModel.get_selected_tab()))

    def set_menuPage(self, page):
        self.menuPage = MenuPage(page=page)
        self.set_food_cards_for_menuPage()

    def set_mainWindow(self, page):
        self.mainWindow = Window(page=page, content=self.mainPage)

    def set_food_cards_for_menuPage(self):
        self.menuPage.cards_Of_Food.controls = self.get_food_cards_for_menuPage()
        self.page.update()

    def get_food_cards_for_menuPage(self):
        items = []
        for i in range(30):
            items.append(
                FoodCard(page=self.page, name="Привет", price="3000", image="")
            )
        return items

    def get_mainPage_controls(self, index):
        self.viewModel.change_selected_tab = index
        if index == 0:
            return [
                self.header,
                self.menuPage
            ]

        if index == 1:
            return [
                self.header,
                ft.Text("Кукусики")
            ]

    def clicked_on_tab_in_header(self, e, key):
        self.selected_index = key
        for index, tab in enumerate(self.header.tabs):
            if index == key:
                tab.style.color[ft.MaterialState.DEFAULT] = "#e31f2d"
                self.mainPage.controls = self.get_mainPage_controls(index)
            else:
                tab.style.color[ft.MaterialState.DEFAULT] = "black"
        self.page.update()
