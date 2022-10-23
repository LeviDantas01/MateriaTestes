from pytest import MonkeyPatch

from CityRepository import CityRepository
from UserInterface import UserInterface


def test_get_user_input(monkeypatch: MonkeyPatch):
    # Arrange
    city_repository = CityRepository()
    user_interface = UserInterface(city_repository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: "71")
    result = user_interface.get_user_input()

    # Assert
    assert result == 71
    assert type(result) == int
