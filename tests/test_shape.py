import pytest

from lib.shape import Shape


@pytest.mark.skip(reason="This test is currently under development")
def test_shape_class_should_be_implmented():
    shape = Shape()

    assert shape is not None
