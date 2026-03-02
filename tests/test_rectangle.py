import pytest

from lib.rectangle import Rectangle


@pytest.mark.parametrize(
    "width, height",
    [
        (1, 1),
        (1, 3),
        (3, 4),
        (4, 6),
    ],
)
def test_width_should_be_assigned_correctly(width, height):
    rectangle = Rectangle(width, height)

    assert rectangle.width == width


@pytest.mark.parametrize(
    "width, height",
    [
        (1, 1),
        (1, 3),
        (3, 4),
        (4, 6),
    ],
)
def test_height_should_be_assigned_correctly(width, height):
    rectangle = Rectangle(width, height)

    assert rectangle.height == height


@pytest.mark.parametrize(
    "width, height, area",
    [
        (1, 1, 1),
        (1, 3, 3),
        (3, 4, 12),
        (4, 6, 24),
    ],
)
def test_area_should_be_calculated_correctly(width, height, area):
    rectangle = Rectangle(width, height)

    assert rectangle.area() == area


@pytest.mark.parametrize("width, height, perimeter", [
    (5, 6, 22),
    (4, 10, 28),
    (7, 8, 30)
])
def test_perimeter_should_be_calculated_correctly(width, height, perimeter):
    rectangle = Rectangle(width, height)

    assert rectangle.perimeter() == perimeter