from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order



def test_set_menu_item():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 2", 5)
    menu3 = Menu(3, "Test 3", 2)
    # Act

    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    # Assert
    assert len(menu_repository.menu_itens) == 2
    assert not menu3 in menu_repository.menu_itens
    assert type(menu_repository.menu_itens) == list


def test_check_if_itens_exists():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []

    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 2", 10)
    menu3 = Menu(3, "Test 3", 10)
    menu4 = Menu(4, "Test 4", 10)
    menu5 = Menu(5, "Test 5", 10)
    # Act


    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)
    menu_repository.set_menu_item(menu3)
    menu_repository.set_menu_item(menu4)
    menu_repository.set_menu_item(menu5)

    order1 = Order(3, 2)
    order2 = Order(6, 25)

    resultOK = menu_repository.check_if_itens_exists(order1)
    resultNOK = menu_repository.check_if_itens_exists(order2)

    # Assert
    assert len(menu_repository.menu_itens) <= 5
    assert resultOK == True
    assert resultNOK == False

