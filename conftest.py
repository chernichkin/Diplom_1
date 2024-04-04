import pytest
from praktikum.ingredient import Ingredient
from data import Data

@pytest.fixture(scope='function') #запускаем перед каждым тестом
def ingredients_collector():
    ingredients_collector = Ingredient(*Data.ingredients_data)
    return ingredients_collector

