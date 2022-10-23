from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository


def test_new_order_with_product_total_price():
    # Arrange
    customer1 = Customer(1, "Jefté")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Milk", 50, 10)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 5)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert order.total_price == 250

def test_new_order_without_product():
    # Arrange
    customer1 = Customer(1, "Jefté")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Milk", 50, 10)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 15)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert order.total_price == 0

def test_produto():
    product1 = Product(6, "Rice", 50, 20)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order_product1 = OrderProduct()
    order_product1.add_product(product1, 1)

    assert order_product1.product.id == 6
    assert order_product1.quantity != 51
    assert order_product1.value_item != 20

def test_finalizar_produto():
    product1 = Product(8, "Bean", 100, 50)

    order_product1 = OrderProduct()
    order_product1.add_product(product1, 60)
    order_product1.process_product(product1, 20)

    assert product1.stock != 140