from maths import add
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

#
# def test_adding_two_floats_is_correct():
#     result = add(1.2, 3.4)
#     assert result == 4.6
