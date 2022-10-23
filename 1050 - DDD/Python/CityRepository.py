from City import City


class CityRepository:

    def __init__(self) -> None:
        self.list_cities: list[City] = []

    def add_city_in_list(self, city: City) -> None:
        self.list_cities.append(city)

    def check_if_city_exists(self, ddd: int) -> bool:
        for city in self.list_cities:
            if (ddd == city.ddd):
                return True

        return False

    def get_city(self, ddd: int) -> str:
        for city in self.list_cities:
            if (ddd == city.ddd):
                return city.name_city

        return "City not found!"

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        menu = formatText.format("DDD", "Name of city")

        for city in self.list_cities:
            menu += formatText.format(city.ddd, city.name_city)

        return menu
