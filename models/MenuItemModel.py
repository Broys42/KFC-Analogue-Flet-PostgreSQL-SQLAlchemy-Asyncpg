from entities.MenuItem import MenuItem

class MenuItemModel():
    def __init__(self):
        self.model : dict[int: MenuItem] = {}

    def set_model_from_database(self, result):
        for item in result:
            for param in item:
                menuItem = MenuItem(name=param.name, price=param.price, image=param.image, item_id=param.id)
                self.model[param.id] = menuItem
