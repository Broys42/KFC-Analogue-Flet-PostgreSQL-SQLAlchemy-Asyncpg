from MenuItem import MenuItem

class MenuItemModel():
    def __init__(self):
        self.model = [
            MenuItem(name="Азия Ролл с креветками", price="319", image="asia_shrimp_roll"),
            MenuItem(name="Оригинальный Баскет", price="279", image="basket_original"),
            MenuItem(name="Биг Маэстро Бургер Острый", price="314", image="big_maestro_burger_hot"),
            MenuItem(name="Чикен Тортик", price="134", image="chicken_cake"),
            MenuItem(name="Комбо Кофе с Чикенбургером", price="179", image="combo_coffee_chickenburger"),
            MenuItem(name="Маэстро Чиз Бургер", price="399", image="maestro_cheese_burger"),
            MenuItem(name="Ростмастер Чиз", price="419", image="rostmaster_cheese"),
            MenuItem(name="Терияки Рис Боул", price="279", image="teriyaki_rice_bowl")
        ]
