class SignupPage:

    def __init__(self, page):
        self.page = page
        self.name_input = page.locator("input[name='name']")
        self.email_input = page.locator("input[name='email']")
        self.password_input = page.locator("input[name='password']")
        self.org_input = page.locator("input[name='organisationName']")
        self.signup_button = page.locator("button[type='submit']")

    def navigate(self):
        self.page.goto("https://architect-testing.projectsmate.com/signup")

    def signup(self, name, email, password, organisation):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.org_input.fill(organisation)
        self.signup_button.click()
        self.page.wait_for_load_state("networkidle")
