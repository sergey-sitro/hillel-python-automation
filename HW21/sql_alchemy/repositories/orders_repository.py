from HW21.sql_alchemy.models.order import Order
from HW21.sql_alchemy.session import session


class OrdersRepository:
    def __init__(self):
        self.__session = session

    def insert_order(self, order: Order):
        self.__session.add(order)
        self.__session.commit()
