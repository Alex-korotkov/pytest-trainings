import pytest

from os import path
from playwright.sync_api import sync_playwright




@pytest.fixture(scope="session")
def olx():
    """Initialization of playwright for OLX"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=100)
        #if path.exists("state.json"): 
            
        #    context = browser.new_context(storage_state="state.json")
        #else:
        context = browser.new_context() 
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto("https://olx.ua")

        yield page, context

        context.tracing.stop(path = "/Users/alex/Google Drive/My Drive/WEB/Pytest/olx/trace.zip")
        browser.close()

@pytest.fixture(scope="function")
def sign_in_to_olx(olx):
    page, context = olx
    #if not path.exists("sstate.json"):
    #page.pause()
    page.locator("text=Мой профиль").first.click()
    page.fill('#userEmail', 'korotkov@qarea.com')
    page.fill('#userPass', '147258369olx')
    page.wait_for_timeout(5000)
    page.click('button#se_userLogin')
    #context.storage_state(path="state.json")
    page.wait_for_timeout(5000) 
    #page.locator('text=Не показывать в течение недели').wait_for()
    #page.locator('text=Не показывать в течение недели').click()
    yield page


@pytest.fixture(scope='function')
def pars_flats(sign_in_to_olx):
    with sign_in_to_olx as p:
        p.goto('https://www.olx.ua/d/nedvizhimost/kvartiry/')
        p.locator("text=Все объявления").first.click()
        p.locator('text=Продажа квартир').first.click()
        p.wait_for_load_state('domcontentloaded')
        p.locator('input:near(:text(\"Этаж\"))').first.click()
        p.locator('text=2').first.click()
        p.fill('#search', 'Одесская')
        p.locator('data-testid=search-submit').click()
