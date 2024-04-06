import pytest
from unittest.mock import Mock


class TestBurgerCollector:

    def test_set_buns_by_one_bun(self, burger_collector):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "krendel"
        burger_collector.set_buns(mock_bun)

        assert burger_collector.bun.get_name() == "krendel"

    def test_add_ingredient_by_one_ingredient(self, burger_collector):
        mock_ingredient = Mock()
        burger_collector.add_ingredient(mock_ingredient)

        assert burger_collector.ingredients[0] == mock_ingredient and len(burger_collector.ingredients) == 1

    def test_add_ingredient_by_two_ingredients(self, burger_collector):
        mock_ingredient_one = Mock()
        burger_collector.add_ingredient(mock_ingredient_one)
        mock_ingredient_two = Mock()
        burger_collector.add_ingredient(mock_ingredient_two)

        assert burger_collector.ingredients[1] == mock_ingredient_two and len(burger_collector.ingredients) == 2

    def test_remove_ingredient(self, burger_collector):

        mock_ingredient_one = Mock()
        burger_collector.add_ingredient(mock_ingredient_one)
        mock_ingredient_two = Mock()
        burger_collector.add_ingredient(mock_ingredient_two)
        burger_collector.remove_ingredient(0)

        assert burger_collector.ingredients[0] == mock_ingredient_two and len(burger_collector.ingredients) == 1

    def test_move_ingredient_one_and_two(self, burger_collector):
        mock_ingredient_one = Mock()
        burger_collector.add_ingredient(mock_ingredient_one)
        mock_ingredient_two = Mock()
        burger_collector.add_ingredient(mock_ingredient_two)
        burger_collector.move_ingredient(0, 1)

        assert burger_collector.ingredients[0] == mock_ingredient_two and len(burger_collector.ingredients) == 2

    def test_get_price_by_one_bun_and_one_ingredient(self, burger_collector):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 400
        burger_collector.set_buns(mock_bun)
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_price.return_value = 200
        burger_collector.add_ingredient(mock_ingredient_one)

        assert burger_collector.get_price() == 1000

    def test_get_receipt_by_one_bun_and_one_ingredient(self, burger_collector):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "krendel"
        mock_bun.get_price.return_value = 400
        burger_collector.set_buns(mock_bun)
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_name.return_value = "chili"
        mock_ingredient_one.get_price.return_value = 200
        mock_ingredient_one.get_type.return_value = 'SAUCE'
        burger_collector.add_ingredient(mock_ingredient_one)

        assert "krendel" in burger_collector.get_receipt() and f'Price: 1000' in burger_collector.get_receipt()


