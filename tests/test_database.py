from praktikum.database import Database
import pytest


class TestDatabaseCollector:

    def test_get_available_buns(self):
        database = Database()
        bans = database.available_buns()
        assert bans[0].get_name() == "black bun"

    def test_get_available_ingredients(self):
        database = Database()
        ingredient = database.available_ingredients()
        assert ingredient[0].get_type() == 'SAUCE' and ingredient[0].get_name() == "hot sauce"
