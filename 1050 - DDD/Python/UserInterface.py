from CityRepository import CityRepository


class UserInterface:
    def __init__(self, city_repository: CityRepository) -> None:
        self.city_repository = city_repository

    def get_user_input(self) -> int:
        result = int(input("Inform code of DDD to search destination: "))
        return result

    def get_ddd_by_user(self) -> str:
        ddd = self.get_user_input()

        if (self.city_repository.check_if_city_exists(ddd) == False):
            return "DDD not found!"

        return self.city_repository.get_city(ddd)
