from ast import Break

from City import City
from CityRepository import CityRepository
from UserInterface import UserInterface

city_repository = CityRepository()
city_repository.add_city_in_list(City(61, "Brasília"))
city_repository.add_city_in_list(City(71, "Salvador"))
city_repository.add_city_in_list(City(11, "São Paulo"))
city_repository.add_city_in_list(City(21, "Rio de Janeiro"))
city_repository.add_city_in_list(City(32, "Juiz de Fora"))
city_repository.add_city_in_list(City(19, "Campinas"))
city_repository.add_city_in_list(City(27, "Vitória"))
city_repository.add_city_in_list(City(31, "Belo Horizonte"))

print(city_repository)

user_interface = UserInterface(city_repository)

while True:
    result = user_interface.get_ddd_by_user()
    if (result == "DDD not found!"):
        print(result)
        break
    else:
        print(result)
