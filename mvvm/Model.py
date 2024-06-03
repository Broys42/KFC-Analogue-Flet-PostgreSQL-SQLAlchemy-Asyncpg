from entities.AppUser import AppUser
from models.MenuItemModel import MenuItemModel
from models.ServiceUsersModel import ServiceUsersModel

class Model():
    def __init__(self):
        self.app_user = AppUser()
        self.services_users = ServiceUsersModel()
        self.menu_items_model = MenuItemModel()
