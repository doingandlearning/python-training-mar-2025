from maths import add, subtract
import pytest
# Arrange - Given I have ...
# Act     - When I do ...
# Assert  - Then something will be true


# (6,7,13)
# (1.2, 3.4, 4.6)
# decorator!
@pytest.mark.parametrize(
    'number1, number2, expected_result', [
        (6, 7, 13),
        (1.2, 3.4, 4.6),
        (-1, -1, -2),
        (0, 0, 0),
        (10101010, 10101010, 20202020),
        (-1_000_000_000, -1_000_000_000, -2_000_000_000)
    ]
)
def test_adding_two_numbers_produces_a_correct_result(number1, number2, expected_result):
    # Act   - When I used my add function
    actual_result = add(number1, number2)

    # Assert  - Then something will be true
    assert expected_result == actual_result


@pytest.mark.skip(reason="Don't know why it's failing")
def test_something_i_have_not_finished_yet():
    assert False


def test_fails_if_adding_non_numbers():
    with pytest.raises(TypeError):
        add([], {})

def test_fails_if_adding_two_strings():
    with pytest.raises(TypeError):
        add("Hello", "Goodbye")  # "Hello" + "Goodbye" = "HelloGoodbye"


# Subtraction
def test_can_correctly_subtract_two_numbers():
    assert subtract(10, 7) == 3

def test_can_correctly_subtract_two_decimals():
    assert subtract(9.2, 1.2) == pytest.approx(8.)


# Test Driven Development
# -> Red - Green - Refactor

#
# def test_adding_two_floats_is_correct():
#     result = add(1.2, 3.4)
#     assert result == 4.6
