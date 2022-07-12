from HW21.sql_alchemy.models.product import Product
from HW21.sql_alchemy.session import session


class ProductsRepository:
    def __init__(self):
        self.__session = session

    def insert_product(self, product: Product):
        self.__session.add(product)
        self.__session.commit()
