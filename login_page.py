class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_btn = "#login-button"

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)

    def get_error_message(self):
        return self.page.locator("[data-test='error']").inner_text()