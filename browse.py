from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

from constants import *


def driver() -> webdriver.Chrome:
    # Для option есть два параметра
    # hide_option() - без показа браузера скрапинг
    # view_option() - для отладки с показом на экран
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                               options=hide_option())
    return browser


# Вход на дл через хнурешный аккаунт
def dl_register(browser: webdriver.Chrome, data: dict) -> None:
    browser.get("https://dl.nure.ua")
    button = browser.find_element(by=By.XPATH, value='//*[@id="inst49459"]/div/div/div[2]/div/div[1]/a')
    button.click()
    email = browser.find_element(by=By.ID, value='identifierId')
    email.send_keys(data['email'])
    button = browser.find_element(by=By.ID, value='identifierNext')
    button.click()
    passwd = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.NAME, 'password'))
    )
    passwd.send_keys(data['password'])
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'passwordNext'))
    )
    button.click()
    time.sleep(5)


# Парсинг доступных у вас курсов и записывание их в json
def parser(browser: webdriver.Chrome) -> dict[str, str]:
    page = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'page-container')]"))
    )
    return {"refs":
        list(
            set(
                e.get_attribute('href')
                for e
                in page.find_elements(by=By.TAG_NAME, value='a')
                if e.get_attribute('href').find(PATTERN_COURSE) == 0
            )
        )
    }


# Получение ссылки на вкладку Відвідування
def attendance_link(browser: webdriver.Chrome, subject: str) -> str:
    browser.get(subject)
    return next(e.get_attribute('href')
                for e
                in browser.find_elements(by=By.TAG_NAME, value="a")
                if e.get_attribute('href') is not None and e.get_attribute('href').find(PATTERN_ATTENDANCE) == 0)


# Отмечалка, если находит кнопку - нажимает ее
# В будущем добавлю, чтобы ссылочку на отмечалку отправляло в телегу
def attendance_check(browser: webdriver.Chrome, link: str) -> None:
    browser.get(link)
    try:
        link_att = next(e.get_attribute('href')
                        for e
                        in browser.find_elements(by=By.TAG_NAME, value="a")
                        if
                        e.get_attribute('href') is not None and e.get_attribute('href').find(
                            PATTERN_ATTENDANCE_CHECK) == 0)

        browser.get(link_att)
        button = browser.find_element(by=By.XPATH, value="//*[contains(text(), 'Прис')]")
        button.click()
        button = browser.find_element(by=By.ID, value='id_submitbutton')
        button.click()
        time.sleep(5)
    except StopIteration:
        print(f"Тут нет посещений {link}")
    except NoSuchElementException:
        print(f"Ссылка отмечена без кнопки подтверждения {link}")
