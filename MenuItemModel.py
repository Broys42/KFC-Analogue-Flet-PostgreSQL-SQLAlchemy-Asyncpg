from MenuItem import MenuItem

class MenuItemModel():
    def __init__(self):
        self.model = []

    def set_model_from_database(self, result):
        for item in result:
            for param in item:
                self.model.append(MenuItem(name=param.name, price=param.price, image=param.image))
