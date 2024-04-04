import pytest
from praktikum.ingredient import Ingredient


class TestIngredientCollector:

    def test_get_type(self, ingredients_collector):
        type = ingredients_collector.get_type()
        assert type == 'SAUCE'

    def test_get_name(self, ingredients_collector):
        name = ingredients_collector.get_name()
        assert name == "hot sauce"

    def test_get_price(self, ingredients_collector):
        price = ingredients_collector.get_price()
        assert price == 100
