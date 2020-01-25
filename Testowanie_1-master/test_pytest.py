# ## Pytest
# ### Zadanie 4.
# 1. Uzywając `mark.parametrize` napisz testy które sprawdzą funkcję `is_odd`.
# 2. Napisz logikę funkcji
import pytest
from pytest import mark

# from functions_pytest import is_odd
#
# @mark.parametrize("input_data, expected", [
#     (1, True),
#     (2, False),
#     (0, False),
# ])
# def test_basic(input_data, expected):
#         # When
#     output = is_odd(input_data)
#         # Then
#     assert output == expected
#
# from pytest import mark
# from functions_pytest import Dog, Cat
#
# @pytest.fixture()
# def dog_fixture():
#     return [Dog("Rex"), Dog("Lucky"), Dog("Pimpek")]
#
# @pytest.fixture()
# def cat_fixture():
#     return Cat()
#
#
#
# def test_cat_sound(cat_fixture):
#     assert cat_fixture.speak() == "Miau"
#
# def test_dogs_sounds(dog_fixture):
#     assert len(dog_fixture) == 3
#     for dog in dog_fixture:
#         assert dog.speak() == "Hau"

#================================================================
# from unittest import mock
#
# from functions_pytest import is_correct_website
# import status_code
#
# @mark.parametrize("input_data",
#                   [(("https://google.com", 200),  True),
#                     (("https://onet.pl", 200), True),
#                     (("https://wp.pl", 200), True),
#                    ])
#
# @mock.patch('function_pytest.requests.get')
# def test_is_correct_website(mock_get, input_data, expected):
#     # Given
#     input_website_url, input_status_code - input_data
#     mock_get.return_value.status_code = input_status_code
#     # When
#     output = is_correct_website(input_data)
#     # Then
#     assert output == expected