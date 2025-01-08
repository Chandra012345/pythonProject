import pytest

class TestClass:
    @pytest.mark.sanity
    def test_login(self):
        print("This test is login ")
        assert True

    @pytest.mark.regression
    def test_signup(self):
        print("this test is signup")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_forgotpwd(self):
        print("this test is forgot password")
        assert True

    @pytest.mark.sanity
    def test_homepage(self):
        print("this test is Homepage")
        assert True

    @pytest.mark.regression
    def test_search(self):
        print("this test is search")
        assert True