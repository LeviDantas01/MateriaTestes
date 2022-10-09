from tkinter import Menu

from Coordinate import Coordinate
from Quadrant import Quadrant
import Menu


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"

def test_should_get_second_quadrant_coordinate():
    a = -5
    b = 6
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Second"


def test_should_get_third_quadrant_coordinate():
    a = -6
    b = 7
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result != "Third"

def test_should_is_valid():
    a = 10
    b = 11

    coordinates = Coordinate(a, b)

    assert coordinates != 0


def test_should_is_string():
    a = "78"
    b = "65"

    coordinates = Coordinate(a, b)

    assert coordinates != str


def test_should_coordinates1_different_coordinates2():
    a = 1
    b = 2
    c = -4
    d = 3

    coordinates1 = Coordinate(a, b)
    coordinates2 = Coordinate(c, b)

    assert coordinates1 != coordinates2

