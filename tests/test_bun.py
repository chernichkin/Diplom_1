import pytest
from praktikum.bun import Bun


class TestBunCollector:

    def test_get_name_add_new_name(self):
        bun = Bun("Prrpr", 2)
        assert bun.get_name() == "Prrpr"

    def test_get_price_add_new_price(self):
        bun = Bun("Prrpr", 2)
        assert bun.get_price() == 2
