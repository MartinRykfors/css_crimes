import unittest
import lib.cohost as cohost


class TestCohost(unittest.TestCase):
    def test_build_style_string(self):
        expected = "display: flex; border: 2px solid;"
        actual = cohost.style({"display": "flex", "border": "2px solid"})
        self.assertEqual(expected, actual)
