import pytest
from selene.support.shared import browser
from selene import be, have, by

@pytest.fixture
def size_window():
    browser.config.window_height = 1080
    browser.config.window_width = 1920

@pytest.fixture
def chrome(size_window):
    browser.open('https://google.com')

def test_google_search_not_found(chrome):
    browser.element('[name="q"]').should(be.blank).type('fdfdssddfdsfdfsfd').press_enter()
    browser.element('.card-section').should(have.text('По запросу fdfdssddfdsfdfsfd ничего не найдено.'))