from sqlalchemy import select, text, insert, func, cast
import asyncio
from database import sync_engine, async_engine, session_factory, async_session_factory, Base
from db_models import MenuItemsOrm, menuItem_table

class SyncORM():
    def __init__(self):
        pass

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        sync_engine.echo = False
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = False

    @staticmethod
    def insert_data_into_menuitems():
        with session_factory() as session:
            item1 = MenuItemsOrm(name="Азия Ролл с креветками", price=319, image="asia_shrimp_roll")
            item2 = MenuItemsOrm(name="Оригинальный Баскет", price=279, image="basket_original")
            item3 = MenuItemsOrm(name="Биг Маэстро Бургер Острый", price=314, image="big_maestro_burger_hot")
            item4 = MenuItemsOrm(name="Чикен Тортик", price=134, image="chicken_cake")
            item5 = MenuItemsOrm(name="Комбо Кофе с Чикенбургером", price=179, image="combo_coffee_chickenburger")
            item6 = MenuItemsOrm(name="Маэстро Чиз Бургер", price=399, image="maestro_cheese_burger")
            item7 = MenuItemsOrm(name="Ростмастер Чиз", price=419, image="rostmaster_cheese")
            item8 = MenuItemsOrm(name="Терияки Рис Боул", price=279, image="teriyaki_rice_bowl")
            session.add_all([item1, item2, item3, item4, item5, item6, item7, item8])
            session.commit()

    @staticmethod
    def select_menuItems():
        with async_session_factory() as session:
            query = (
                select(MenuItemsOrm)
            )
            results = session.execute(query).all()
            return results

    # @staticmethod
    # def update_menuItems(item_id: int = 1, new_name: str = "Burger 3"):
    #     with session_factory() as session:
    #         item = session.get(MenuItemsOrm, item_id)
    #         item.name = new_name
    #         session.commit()

class AsyncORM():
    def __init__(self):
        pass

    @staticmethod
    async def create_tables():
        async_engine.echo = False
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        async_engine.echo = False

    @staticmethod
    async def insert_data_into_menuitems():
        async with async_session_factory() as session:
            item1 = MenuItemsOrm(name="Азия Ролл с креветками", price=319, image="asia_shrimp_roll")
            item2 = MenuItemsOrm(name="Оригинальный Баскет", price=279, image="basket_original")
            item3 = MenuItemsOrm(name="Биг Маэстро Бургер Острый", price=314, image="big_maestro_burger_hot")
            item4 = MenuItemsOrm(name="Чикен Тортик", price=134, image="chicken_cake")
            item5 = MenuItemsOrm(name="Комбо Кофе с Чикенбургером", price=179, image="combo_coffee_chickenburger")
            item6 = MenuItemsOrm(name="Маэстро Чиз Бургер", price=399, image="maestro_cheese_burger")
            item7 = MenuItemsOrm(name="Ростмастер Чиз", price=419, image="rostmaster_cheese")
            item8 = MenuItemsOrm(name="Терияки Рис Боул", price=279, image="teriyaki_rice_bowl")
            session.add_all([item1, item2, item3, item4, item5, item6, item7, item8])
            await session.commit()

    @staticmethod
    async def select_menuItems():
        async_engine.echo = False
        async with async_session_factory() as session:
            query = (
                select(MenuItemsOrm)
            )
            results = await session.execute(query)
            return results.all()

    @staticmethod
    async def update_menuItems(item_id, new_name, new_price, new_image):
        async_engine.echo = True
        async with async_session_factory() as session:
            item = await session.get(MenuItemsOrm, item_id)
            item.name = new_name
            item.price = new_price
            item.image = new_image
            await session.commit()
