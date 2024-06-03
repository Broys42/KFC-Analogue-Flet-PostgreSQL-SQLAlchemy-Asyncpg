class ServiceUser():
    def __init__(self, id, name, fav_menu_items):
        self.id : int
        self.name = name
        self.fav_menu_items : list[int] = fav_menu_items
