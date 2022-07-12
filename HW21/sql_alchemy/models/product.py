from sqlalchemy import Integer, Column, VARCHAR, ForeignKey
from HW21.sql_alchemy.session import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(VARCHAR(255))
    product_price = Column(Integer)

    def __str__(self):
        return f'product_id: {self.product_id}, product_name: {self.product_name}, product_price: {self.product_price}'
