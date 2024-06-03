from mvvm.Model import Model
import flet as ft
from orm import AsyncORM
from entities.MenuItem import MenuItem

class ViewModel():
    def __init__(self, model: Model):
        self.model = model
        self.async_orm = AsyncORM()

    def get_selected_tab(self):
        return self.model.app_user.selected_tab

    def change_selected_tab(self, index):
        self.model.app_user.selected_tab = index

    def get_menuItemsModel(self):
        return self.model.menu_items_model.model

    async def get_menuitems_model_from_database(self):
        result = await self.select_model_from_menuItems()
        self.model.menu_items_model.set_model_from_database(result)

    async def select_model_from_menuItems(self):
        return await self.async_orm.select_menuItems()

    async def update_menuItem(self, item_id, name, price, image):
        await self.async_orm.update_menuItems(item_id=item_id, new_name=name, new_price=price, new_image=image)
        self.update_menuItem_in_model(item_id, name, price, image)

    def update_menuItem_in_model(self, item_id, name, price, image):
        menu_item = self.model.menu_items_model.model[item_id]
        updates = {'name': name, 'price': price, 'image': image, 'item_id': item_id}
        menu_item.__dict__.update(updates)
