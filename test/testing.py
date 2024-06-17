from src.main import func_data_match


def test_data_match():
    x = func_data_match(2)
    assert x == 4
