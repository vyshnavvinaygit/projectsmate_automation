class LoginPage:

    def __init__(self, page):
        self.page = page
        self.email_input = page.locator("input[name='email']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.get_by_role("button", name="Login")


    def navigate(self):
        self.page.goto("https://architect-testing.projectsmate.com/login")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")

