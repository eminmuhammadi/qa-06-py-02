import pytest

from lib.circle import Circle


@pytest.fixture
def radius_fixture():
    return 5


@pytest.mark.parametrize(
    "radius",
    [
        (1),
        (2),
        (3),
        (4),
    ],
)
def test_radius_should_be_assigned_correctly(radius):
    circle = Circle(radius)

    assert circle.radius == radius


@pytest.mark.parametrize(
    "radius",
    [
        (1),
        (2),
        (3),
        (4),
    ],
)
def test_area_should_be_calculated_correctly(radius):
    circle = Circle(radius)

    assert circle.area() == 3.14 * (radius * radius)


def test_area_with_fixture(radius_fixture):
    circle = Circle(radius_fixture)

    assert circle.area() == 3.14 * (radius_fixture * radius_fixture)
