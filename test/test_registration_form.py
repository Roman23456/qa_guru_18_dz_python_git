import allure
import os
from pages.registration_page import RegistrationPage


def test_registration_form(setup_browser, request):
    site_url = request.config.getoption("--site-url") or os.getenv("SITE_URL")

    registration_page = RegistrationPage(setup_browser, site_url)

    with allure.step('Fill form'):
        registration_page.open()
        registration_page.fill_number(os.getenv("TEST_NUMBER"))
        registration_page.fill_text(os.getenv("TEST_TEXT"))
        registration_page.fill_password(os.getenv("TEST_PASSWORD"))
        registration_page.fill_date(os.getenv("TEST_DATE"))
        registration_page.click_display_inputs()