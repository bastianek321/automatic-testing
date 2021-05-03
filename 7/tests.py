import pytest
import calculator as calc

calculator = calc.Calculator()
table = calc.Table()


@pytest.mark.parametrize(
    "a, b, expected", 
    [
        pytest.param(
            2, 5, 7
        ),
        pytest.param(
            -10, 0, -10
        ),
        pytest.param(
            200, 15, 215
        ),
        pytest.param(
            -10, -100, -110
        ),
        pytest.param(
            2400, 1355, 3755
        ),
        pytest.param(
            -1099, 10, -1089
        )
    ]
)
def test_add(a, b, expected):
    assert(calculator.add(a, b), expected)

@pytest.mark.parametrize(
    "a, b, expected", 
    [
        pytest.param(
            2, 5, -3
        ),
        pytest.param(
            -10, 0, -10
        ),
        pytest.param(
            200, 15, 185
        ),
        pytest.param(
            -10, -100, 90
        ),
        pytest.param(
            2400, 1355, 1045
        ),
        pytest.param(
            -1099, 10, -1109
        )
    ]
)
def test_subtract(a, b, expected):
    assert(calculator.subtract(a, b), expected)

@pytest.mark.parametrize(
    "a, b, expected", 
    [
        pytest.param(
            2, 5, 10
        ),
        pytest.param(
            -10, 0, 0
        ),
        pytest.param(
            200, 15, 3000
        ),
        pytest.param(
            -10, -100, 1000
        ),
        pytest.param(
            2400, 12, 28800
        ),
        pytest.param(
            -2, 10, -20
        )
    ]
)
def test_multiply(a, b, expected):
    assert(calculator.multiply(a, b), expected)

@pytest.mark.parametrize(
    "a, b, expected", 
    [
        pytest.param(
            5, 2, 2
        ),
        pytest.param(
            -10, -1, 10
        ),
        pytest.param(
            200, 15, 13
        ),
        pytest.param(
            -10, -100, -0.1
        ),
        pytest.param(
            2400, -1200, -2
        ),
        pytest.param(
            -1090, -10, 109
        )
    ]
)
def test_divide(a, b, expected):
    assert(calculator.divide(a, b), expected)

@pytest.mark.parametrize(
    "array, expected", 
    [
        pytest.param(
            [10, 5, 2], 17
        ),
        pytest.param(
            [12, 3, 4], 19
        ),
        pytest.param(
            [10, 3, 3], 16
        ),
        pytest.param(
            [-10, 5, 20], 15
        ),
        pytest.param(
            [-12, -3, -4], -19
        ),
        pytest.param(
            [10, 3, -3], 10
        )
    ]
)
def test_array_sum(array, expected):
    assert(table.sum(array), expected)

@pytest.mark.parametrize(
    "array, x, expected", 
    [
        pytest.param(
            [10, 5, 2], 17, False
        ),
        pytest.param(
            [12, 3, 4], 4, True
        ),
        pytest.param(
            [10, 3, 3], 'test', False
        ),
        pytest.param(
            ['sample', 'text'], 2, False
        ),
        pytest.param(
            ['sample', 'text', 1, 5], 'sample', True
        )
    ]
)
def test_array_has_number(array, x, expected):
    assert(table.has_number(array, x), expected)