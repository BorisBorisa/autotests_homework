# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
import random
import string

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException


def random_str(min_range: int = 1, max_range: int = 15) -> str:
    random_range = range(random.randrange(min_range, max_range))
    random_string = ''.join((random.choice(string.ascii_lowercase) for _ in random_range))

    return random_string


ONLINE_SBIS_SITE = "https://fix-online.sbis.ru/"
LOGIN = "Демо_тензор"
PASSWORD = "Демо_тензор0@"

TEST_DATA_NAME = "Травина Анна"
RANDOM_MESSAGE = random_str(50, 100)
MESSAGE_DIALOG_ITEM_XPATH = f"//*[contains(@class, 'msg-dialogs-item__message-text')]/*[text()='{RANDOM_MESSAGE}']"

options = ChromeOptions()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

action = ActionChains(driver)

try:
    driver.get(ONLINE_SBIS_SITE)

    # Авторизация
    login_input = driver.find_element(
        By.XPATH, '(//*[@data-qa="controls-Render__field"])[1]/input'
    )
    login_input.send_keys(LOGIN)

    login_check_sign_button = driver.find_element(
        By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__checkSignInTypeButton"]'
    )
    login_check_sign_button.click()

    password_input = driver.find_element(
        By.XPATH, '(//*[@data-qa="controls-Render__field"])[2]/input'
    )
    password_input.send_keys(PASSWORD)

    login_sign_button = driver.find_element(
        By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__signInButton"]'
    )
    login_sign_button.click()
    time.sleep(1)

    # Переход в реестр "Контакты"
    contacts_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='Контакты']")
    action.double_click(contacts_button).perform()
    time.sleep(2)

    # Отправка сообщения самому себе
    add_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='sabyPage-addButton']")
    add_button.click()
    time.sleep(2)

    user_message_item = driver.find_element(By.CSS_SELECTOR, f"[data-qa='tile-container'] [title='{TEST_DATA_NAME}']")
    user_message_item.click()
    time.sleep(2)

    message_input = driver.find_element(By.CSS_SELECTOR, "[data-qa='textEditor_slate_Field']")
    message_input.send_keys(RANDOM_MESSAGE)

    send_message_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_message_button.click()
    time.sleep(1)

    # Проверка, что сообщение появилось в реестре
    message_dialogs_item = driver.find_element(By.XPATH, MESSAGE_DIALOG_ITEM_XPATH)

    assert message_dialogs_item.is_displayed(), "Отправленное сообщение отсутствует"

    # Удаление сообщения
    action.move_to_element(message_dialogs_item).perform()
    del_message_button = driver.find_element(
        By.XPATH,
        MESSAGE_DIALOG_ITEM_XPATH + "/following::*[@data-qa='controls-itemActions__action deleteToArchive']"
    )
    del_message_button.click()
    time.sleep(1)

    # Проверка, что сообщение удалилось
    try:
        message_dialogs_item = driver.find_element(By.XPATH, MESSAGE_DIALOG_ITEM_XPATH)
    except NoSuchElementException:
        pass
    else:
        raise AssertionError("Отправленное сообщение ну удалилось")

    time.sleep(2)

except AssertionError as err:
    print(err)
finally:
    driver.quit()
