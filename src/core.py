from sqlalchemy import select, text, insert, update
import asyncio
from database import sync_engine, async_engine
from models import menuItem_table, metadata_obj


class SyncCore:
    def __init__(self):
        pass

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_data():
        with sync_engine.connect() as conn:
            # stmt = """INSERT INTO menuitems (name, price, image) VALUES
            # ('Test', '123', 'ImageTest'),
            # ('asd', '15124', 'fdgsd');"""
            stmt = insert(menuItem_table).values(
                [
                    {"name":"test", "price":123124, "image":"asfsad"}
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_menuItems():
        with sync_engine.connect() as conn:
            query = select(menuItem_table)
            result = conn.execute(query)
            menuItems = result.all()
            print(f"{menuItems=}")
            conn.commit()

    @staticmethod
    def update_menuItems(item_id: int = 1, new_name: str = "Burger"):
        with sync_engine.connect() as conn:
            # stmt = text("UPDATE menuitems SET name=:new_name WHERE id=:id")
            # stmt = stmt.bindparams(new_name=new_name, id=item_id)
            stmt = (
                update(menuItem_table)
                .values(name=new_name)
                # .where(menuItem_table.c.id==id)
                .filter_by(id=item_id)
            )
            conn.execute(stmt)
            conn.commit()
