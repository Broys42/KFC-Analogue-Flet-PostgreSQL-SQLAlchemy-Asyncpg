from Model import Model
import flet as ft
from orm import AsyncORM


class ViewModel():
    def __init__(self, model: Model):
        self.model = model
        self.async_orm = AsyncORM()

    def get_selected_tab(self):
        return self.model.user.selected_tab

    def change_selected_tab(self, index):
        self.model.user.selected_tab = index

    def get_menuItemsModel(self):
        return self.model.menuItemsModel.model

    async def get_menuitems_model_from_database(self):
        result = await self.select_model_from_menuItems()
        self.model.menuItemsModel.set_model_from_database(result)

    async def select_model_from_menuItems(self):
        return await self.async_orm.select_menuItems()
