import pytest


@pytest.mark.main
class TestLog:
    data = [
        {"aa": 11, "bb": 22, "cc": 33},
        {"a": 1, "b": 2, "c": 3}
    ]

    @pytest.mark.parametrize("item", data)
    def test_000(self, item):
        print(item)
