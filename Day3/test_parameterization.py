import pytest

class TestClass:
    @pytest.mark.parametrize('mark1,mark2',[(1,1),(4,5),(10,10),(10,8)])
    def test_calculation(self,mark1,mark2):
        assert mark1==mark2
