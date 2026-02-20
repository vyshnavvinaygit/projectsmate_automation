from utils.testdata import get_test_user
from pages.login import LoginPage
def test_user_login(page):
    login = LoginPage(page)
    user = get_test_user()
    login.navigate()
    login.login(user["email"],user["password"])
    print("Login Success")
    page.screenshot(path="login.png")
    print(page.url)
    assert "dashboard" in page.url
