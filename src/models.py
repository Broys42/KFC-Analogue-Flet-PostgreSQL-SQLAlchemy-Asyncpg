from typing import Annotated
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]

class MenuItemsOrm(Base):
    __tablename__ = "menuitems"
    id: Mapped[intpk]
    name: Mapped[str_256]
    price: Mapped[int]
    image: Mapped[str_256]

class UsersOrm(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    name: Mapped[str_256]

class UsersFavouriteMenuItems(Base):
    __tablename__ = "usersfavmenuitems"
    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    menuitem_id = mapped_column(ForeignKey("menuitems.id", ondelete="CASCADE"), primary_key=True)


metadata_obj = MetaData()

menuItem_table = Table(
    "menuitems",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("price", Integer),
    Column("image", String)
)
