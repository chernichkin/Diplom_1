import pytest
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from data import Data

@pytest.fixture(scope='function') #запускаем перед каждым тестом
def ingredients_collector():
    ingredients_collector = Ingredient(*Data.ingredients_data)
    return ingredients_collector

@pytest.fixture(scope='function') #запускаем перед каждым тестом
def burger_collector():
    burger_collector = Burger()
    return burger_collector

@pytest.fixture(scope='function') #запускаем перед каждым тестом
def database_collector():
    database_collector = Database()
    return database_collector

