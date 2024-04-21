from praktikum.database import Database
from unittest.mock import Mock
import pytest
from data import Data


class TestDatabaseCollector:


    @pytest.mark.parametrize('index,name', Data.index_bun_name)
    def test_get_available_buns(self, database_collector, index, name):
        bans = database_collector.available_buns()
        assert bans[index].get_name() == name

    @pytest.mark.parametrize('index,name', Data.index_souce_name)
    def test_get_available_ingredients_by_name(self, database_collector, index, name):
        ingredient = database_collector.available_ingredients()
        assert ingredient[index].get_name() == name
