import pytest
from page.loginPage import LoginPage
from utils.webActions import WebActions

import allure


class TestLogin:
    @allure.feature("Login Feature")
    @allure.story("Login functionality")
    @allure.title("Positive test")
    @pytest.mark.parametrize("username, password, expected_text", [
        ("student", "Password123", "Logged In Successfully"),
        ("incorrectUser", "Password123", "Your username is invalid!"),
        ("student", "incorrectPassword", "Your password is invalid!")
    ])
    def test_login(self, driver, username, password, expected_text):
        with allure.step(f"Loading login page"):
            login_page = LoginPage(driver)
            actions = WebActions(driver)
            login_page.load()

        with allure.step(f"Logging in with username: {username} and password: {password}"):
            login_page.login(username, password)

        with allure.step("Verifying successful login"):
            if expected_text == "Logged In Successfully":
                assert actions.get_element_text(login_page.LOGIN_MESSAGE) == expected_text
                assert actions.is_element_visible(
                    login_page.LOGOUT_BUTTON), "Logout button is not visible, login might have failed"
            else:
                assert actions.get_element_text(login_page.ERROR_MSG) == expected_text