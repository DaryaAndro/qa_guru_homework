import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def size_window():
    browser.config.window_height = 1080
    browser.config.window_width = 1920


def test_google_search(size_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_not_found(size_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fdfdssddfdsfdfsfd').press_enter()
    browser.element('.card-section').should(have.text('По запросу fdfdssddfdsfdfsfd ничего не найдено.'))
