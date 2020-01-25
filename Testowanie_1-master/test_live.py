import unittest

class BaseTestExample(unittest.TestCase):
    def setup(self) -> None:
        super().setup()
        self.example = 5

    def test_say_name_with_titles(self):
        self.assertEquals(self.example, 5)

import os

os.remove()

