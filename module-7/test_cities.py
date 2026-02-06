"""Jorge Ibarra
CSD 325 Module 7.2 Assignment
2/4/2026"""

import unittest
from city_functions import format_city_country

#test class to test city_functions.py
class TestCityFunctions(unittest.TestCase):
    #tests format_city_country function
    def test_city_country(self):
        self.assertEqual(
            format_city_country("Santiago", "Chile"),
            "Santiago, Chile"
        )

        self.assertEqual(
            format_city_country("Sydney", "Australia"),
            "Sydney, Australia"
        )

        self.assertEqual(
            format_city_country("Mexico City", "Mexico"),
            "Mexico City, Mexico"
        )

#runs the unit tests
if __name__ == "__main__":
    unittest.main()