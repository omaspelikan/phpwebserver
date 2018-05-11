# test city_country function
""" import and check city_country function """
from city_functions import city_country
import unittest
class Testmyfunction(unittest.TestCase):
    def test_city_country(self):
        city_country_name = city_country('Taipei','Taiwan')
        self.assertEqual(city_country_name,'Taipei, Taiwan')
    def test_city_country_population(self):
        city_country_name = city_country('Taipei','Taiwan','500')
        self.assertEqual(city_country_name,'Taipei, Taiwan - 500')

unittest.main()
