import pytest
from src.operations_card import mask_card


def test_mask_card(operations_data_card_befor, operations_data_card_after):
    """Тестируем маскировку карты"""

    result = mask_card(operations_data_card_befor)
    assert result == operations_data_card_after
