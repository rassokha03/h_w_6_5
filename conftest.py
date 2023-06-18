import pytest
from selene import browser


@pytest.fixture(scope='function', autouse= 'True')
def manag_chrome():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'