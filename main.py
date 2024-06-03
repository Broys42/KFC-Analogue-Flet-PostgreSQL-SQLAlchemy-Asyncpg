import flet as ft
import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], 'src'))

from src.config import settings
from src.orm import SyncORM, AsyncORM
from src.core import SyncCore

from UI.WindowUI import WindowUI
from mvvm.Model import Model
from mvvm.ViewModel import ViewModel
from mvvm.View import View

class Starter():
    def __init__(self):
        pass

    async def main(self):
        self.async_orm = AsyncORM()

        if settings.CREATE_DB:
            await self.create_database()

        self.model = Model()
        self.viewModel = ViewModel(self.model)
        self.view = View(self.viewModel)
        await self.view.show()

    async def create_database(self):
        await self.create_tables()
        await self.add_menuItems_in_database()

    async def create_tables(self):
        await self.async_orm.create_tables()

    async def add_menuItems_in_database(self):
        await self.async_orm.insert_data_into_menuitems()

if __name__ == "__main__":
    starter = Starter()
    asyncio.run(starter.main())
