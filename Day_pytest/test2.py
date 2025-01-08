import pytest

class TestClass:
    @pytest.fixture()
    def setup(self):
        print("Launching bowser")
    def test_method1(self,setup):
        print("this is test method1")
    def test_method2(self,setup):
        print("this is test method2")
    def test_method3(self,setup):
        print("this is test method3")