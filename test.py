import unittest

class TestClass(unittest.TestCase):
    pass


def make_dynamic_test_function(text: str):
    def test_function(self):
        self.assertEqual(text, "Correct")

    return test_function

test_parameters = [
    "Incorrect",
    "Correct",
]

for item in test_parameters:
    setattr(TestClass,
        f"test_text__{item}",
        make_dynamic_test_function(item))
