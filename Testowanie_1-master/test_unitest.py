import unittest

### Zadanie 1.
# 1. Napisz testy do funkcji is_even sprawdzający przypadki pozytywne
# 2. Napisz testy obsługujące przypadki negatywne (obsługa wyjątków)
# 3. Napisz logikę funkcji
from unittest import mock

from functions_unittest import is_even, Person, remove_file


# class BasicTestCase(unittest.TestCase):
#
#     def test_basic(self):
#         self.assertTrue(False)
#
# class IsEvenTestCase(unittest.TestCase):
#
#     def test_is_even_returning_true(self):
#
#         # given
#         input_data = 4
#
#         # when
#         output = is_even(input_data)
#
#         # then
#         self.assertEqual(output, True)
#
#     def test_is_even_returning_false(self):
#         # given
#         input_data = 5
#
#         # when
#         output = is_even(input_data)
#
#         # then
#         self.assertEqual(output, False)


class PersonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        # given
        self.person = Person('John', 'Snow', 30)

    def test_say_name_with_mr(self):
        # when
        output = self.person.say_name_with_titles('Mr.')
        # then
        self.assertEqual(output, 'Mr. John Snow')

    def test_say_name_with_mrs(self):
        # when
        output = self.person.say_name_with_titles('Mrs.')
        # then
        self.assertEqual(output, 'Mrs. John Snow')


### Zadanie 3.
# Napisz funkcję `remove_file` która jako parametr przyjmie nazwę pliku do usunięcia.
# Napisz test który zamockuje jego usuwanie i sprawdzi tylko czy moduł `os` został wywołany z
# przekazanym parametrem.

class test_remove_file(unittest.TestCase):
    @mock.patch('functions_unittest.os.path.isfile')
    @mock.patch('functions_unittest.os.remove')
    def test_removw_file(self, mock_isfile, mock_remove):
        mock_isfile.return_value = False
        # when
        remove_file("c:\\Users\\eliza\\Desktop\\Python\\git\\SDA_TDD - master\\usuwaj.txt")

        # then
        mock_isfile.assert_called()
        mock_remove.assert_called_with("c:\\Users\\eliza\\Desktop\\Python\\git\\SDA_TDD - master\\usuwaj.txt")
