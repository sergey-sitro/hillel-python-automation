from sqlalchemy import Integer, Column, ForeignKey
from HW21.sql_alchemy.session import Base


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer)
