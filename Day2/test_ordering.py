import pytest
class TestClass:

    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("this is test method C")
        assert True==True

    @pytest.mark.run(order=2)
    def test_methodB(self):
        print("this is test method B")
        assert True==True

    @pytest.mark.run(order=5)
    def test_methodE(self):
        print("this is test method E")
        assert True == True

    @pytest.mark.run(order=4)
    def test_methodD(self):
        print("this is test method D")
        assert True==True

    @pytest.mark.run(order=1)
    def test_methodA(self):
        print("this is test method A")
        assert True==True

    @pytest.mark.run(order=6)
    def test_methodF(self):
        print("this is test method F")
        assert True==True