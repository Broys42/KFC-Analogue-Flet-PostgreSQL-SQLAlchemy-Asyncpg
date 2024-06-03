from User import User
from MenuItemModel import MenuItemModel
from orm import AsyncORM

class Model():
    def __init__(self):
        self.user = User()
        self.menu_items_model = MenuItemModel()
