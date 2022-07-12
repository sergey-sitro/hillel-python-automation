from HW21.sql_alchemy.models.order import Order
from HW21.sql_alchemy.models.product import Product
from HW21.sql_alchemy.repositories.orders_repository import OrdersRepository
from HW21.sql_alchemy.repositories.products_repository import ProductsRepository
from HW21.sql_alchemy.session import create_db
from session import __session

product_repo = ProductsRepository()
order_repo = OrdersRepository()

create_db()
product_repo.insert_product(Product(product_name='iPhone', product_price=1000))
product_repo.insert_product(Product(product_name='Tablet', product_price=1200))
product_repo.insert_product(Product(product_name='MacBook', product_price=1500))
product_repo.insert_product(Product(product_name='Apple Watch', product_price=800))
product_repo.insert_product(Product(product_name='iMac', product_price=2000))

order_repo.insert_order(Order(product_id=1, quantity=3))
order_repo.insert_order(Order(product_id=2, quantity=2))
order_repo.insert_order(Order(product_id=3, quantity=1))
order_repo.insert_order(Order(product_id=4, quantity=5))
order_repo.insert_order(Order(product_id=5, quantity=1))

results = __session().query(Product, Order).join(Order).all()
print("name", "price", "qty", "total")
for product, order in results:
    print(product.product_name, product.product_price, order.quantity, product.product_price * order.quantity)
