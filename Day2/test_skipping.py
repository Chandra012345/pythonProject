import pytest

class TestClass:
    def test_LoginByEmail(self):
        print("This method is login by email")
        assert True==True

    def test_LoginByFacebook(self):
        print("this method is login by facebook")
        assert True==True

    def test_LoginBytwitter(self):
        print("this method is login by twitter")
        assert True==True
    @pytest.mark.skip
    def test_SignupByEmail(self):
        print("this method is signup by email")
        assert True==True
    @pytest.mark.skip
    def test_SignupByFacebook(self):
        print("this method is signup by facebook")
        assert True==True
    @pytest.mark.skip
    def test_SignupByTwitter(self):
        print("this method is signup by Twitter")
        assert True==True