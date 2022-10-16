from UserInterface import UserInterface
from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order


def test_is_total_ten():
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 1", 11)
    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    user = UserInterface(menu_repository)
    order1 = Order(1, 1)
    order2 = Order(10, 22)
    total1 = UserInterface.get_total_price(user, order1)
    total2 = UserInterface.get_total_price(user, order2)

    assert total1 == 10
    assert total2 != 10


def test_user_input():

    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    user = UserInterface(menu_repository)
    menu = Menu(1, "Test 1", 10)
    menu_repository.set_menu_item(menu)
    order = Order(1, 4)
    teste = user.get_user_input()
    num1 = 1
    num2 = 10
    resul = teste == num1 and teste == num2 and order == num1 and order == num2

    assert resul == num2 and resul == num1

