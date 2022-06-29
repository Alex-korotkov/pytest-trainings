import pytest 
import telegram
from playwright.sync_api import sync_playwright

from settings_cred import api_key, user_id

def test_title(sign_in_to_olx):
    assert sign_in_to_olx.title() == 'Сервис объявлений OLX: сайт частных объявлений в Украине - купля/продажа б/у товаров на OLX.ua' or 'Сервис объявлений OLX: сайт объявлений в Украине - новые и бу товары на OLX.ua'

@pytest.mark.smoke
def test_availability(olx):
    assert olx.title() == 'Сервис объявлений OLX: сайт объявлений в Украине - новые и бу товары на OLX.ua' 

# @pytest.mark.in_progress
def test_flats(pars_flats):
    assert True


@pytest.mark.target
def test_check_new_flats(sign_in_to_olx):
    bot = telegram.Bot(token=api_key)
    page = sign_in_to_olx
    with page as p:
        p.goto("https://www.olx.ua/favorites/search/")
        
        news = p.locator('a.searchLink')
        if not news.text_content() == 'показать новое: 0 объявлений': 
            p.locator('a.searchLink').click()
            
            message = ""
            p.locator('//div[@data-cy="l-card"]/a').first.wait_for()
            rows = p.locator('//div[@data-cy="l-card"]/a')
            count = rows.count()
            for i in range(count):
                message += '--------------------------------------\n<a href="https://www.olx.ua/'+rows.nth(i).get_attribute('href')+'">'+rows.nth(i).text_content()+'</a>\n'
                
            bot.send_message( parse_mode='html', chat_id=user_id, text=message)
            
            bot.send_message( parse_mode='html', chat_id='500261930', text=message)
        else:

            bot.send_message( parse_mode='html', chat_id='500261930', text='there are no news about flats for Odesskay')
            
            bot.send_message( parse_mode='html', chat_id=user_id, text='there are no news about flats for Odesskay')
    assert True