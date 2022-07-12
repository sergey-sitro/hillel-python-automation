from HW21.sql_alchemy.models.product import Product
from HW21.sql_alchemy.session import session


class ProductsRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self, id_value: int):
        product = self.__session.get(Product, {'product_id': id_value})
        return product
