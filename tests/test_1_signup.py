from pages.signup import SignupPage
from utils.testdata import get_test_user

def test_user_signup(page):
    user = get_test_user()
    signup = SignupPage(page)

    signup.navigate()

    page.screenshot(path="signup.png")
    print(page.url)

