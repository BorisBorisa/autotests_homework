# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

SBIS_SITE = 'https://sbis.ru/'
TENSOR_ABOUT = "https://tensor.ru/about"

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(SBIS_SITE)

    contacts_button = driver.find_element(By.XPATH, "//*[@class='sbisru-Header']//*[text()='Контакты']")
    contacts_button.click()
    time.sleep(1)

    contacts_popup_menu_link = driver.find_element(By.CSS_SELECTOR, "#popup .sbisru-link")
    contacts_popup_menu_link.click()

    tensor_logo = driver.find_element(By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__logo-tensor")
    tensor_logo.click()

    driver.switch_to.window(driver.window_handles[-1])

    about_team_block_title = driver.find_element(
        By.CSS_SELECTOR,
        ".tensor_ru-Index__block4-bg .tensor_ru-Index__card-title"
    )
    about_team_block_more_link = driver.find_element(
        By.CSS_SELECTOR,
        ".tensor_ru-Index__block4-bg .tensor_ru-link"
    )

    assert about_team_block_title.is_displayed(), 'Заголовок блока "Сила в людях" не отображается'

    about_team_block_more_link.click()

    assert driver.current_url == TENSOR_ABOUT, "Неверный адрес"
    time.sleep(2)

except AssertionError as err:
    print(err)
finally:
    driver.quit()
