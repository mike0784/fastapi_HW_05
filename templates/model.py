from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship

from .database import Base

import sqlalchemy

# users = sqlalchemy.Table(
#     'users',
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("surname", String(32), nullable=False),
#     Column("name", String(32), nullable=False),
#     Column("patronymic", String(32)),
#     Column("email", sqlalchemy.String(128), nullable=False),
#     Column("password", String(), nullable=False)
# )

# products = sqlalchemy.Table(
#     'products',
#     metadata,
#     Column("id", Integer, primary_key = True),
#     Column("name", String(128), nullable=False),
#     Column("description", String, nullable=False),
#     Column("price", sqlalchemy.Float, nullable=False)
# )

# orders = sqlalchemy.Table(
#     'orders',
#     metadata,
#     Column("id", Integer, primary_key = True),
#     Column("id_user", Integer, ForeignKey("users.id"), nullable=False),
#     Column("id_products", Integer, ForeignKey("products.id")),
#     Column("date", TIMESTAMP(timezone=True), nullable=False, server_default=func.now()),
#     Column("status", String(32), nullable=False)
# )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String(32))
    name = Column(String(32))
    patronymic = Column(String(32))
    email = Column(String(128))
    password = Column(String)

    #orders = relationship("Orders", back_populates="user")

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable=False)
    description = Column(String, nullable=False)
    price = Column(sqlalchemy.Float, nullable=False)

class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key = True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    id_products = Column(Integer, ForeignKey("products.id"))
    date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    status = Column(String(32), nullable=False)

    user = relationship("User", lazy="joined")