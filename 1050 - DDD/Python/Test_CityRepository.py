from City import City
from CityRepository import CityRepository


def test_add_city_in_list():
    # Arrange
    city_repository = CityRepository()
    city = City(21, "Rio de Janeiro")

    # Act
    city_repository.add_city_in_list(City(61, "Brasília"))
    city_repository.add_city_in_list(City(71, "Salvador"))
    city_repository.add_city_in_list(City(11, "São Paulo"))

    # Assert
    assert len(city_repository.list_cities) == 3
    assert not city in city_repository.list_cities
    assert type(city_repository.list_cities) == list


def test_check_if_itens_exists():
    # Arrange
    city_repository = CityRepository()

    # Act
    city_repository.add_city_in_list(City(61, "Brasília"))
    resultOK = city_repository.check_if_city_exists(61)
    resultNOK = city_repository.check_if_city_exists(2)

    # Assert
    assert len(city_repository.list_cities) == 1
    assert resultOK == True
    assert resultNOK == False
