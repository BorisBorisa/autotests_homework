# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

SBIS_SITE = 'https://sbis.ru/'
SABY_APP_FILE_NAME = 'saby-setup.exe'
CURRENT_PATH = str(os.getcwd())
FILE_PATH = os.path.join(CURRENT_PATH, SABY_APP_FILE_NAME)


def wait_file_download(file_path, attempts=10, freq=0.5):
    counter = 0

    while counter <= attempts:
        if not os.path.exists(file_path):
            time.sleep(freq)
            counter += 1
            continue
        else:
            return

    raise TimeoutError('Время ожидания загрузки превышено')


options = ChromeOptions()
options.add_experimental_option(
    "prefs", {
        "download.default_directory": CURRENT_PATH,
        "safebrowsing.enabled": True
    })

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    driver.get(SBIS_SITE)

    footer_download_local_versions_link = driver.find_element(
        By.XPATH, "//*[contains(@class, 'sbisru-Footer')]//*[text()='Скачать локальные версии']"
    )
    footer_download_local_versions_link.click()

    download_button = driver.find_element(
        By.XPATH, f"//a[contains(@href, 'SabyDesktop/master/win32/{SABY_APP_FILE_NAME}')]"
    )

    download_button.click()
    wait_file_download(FILE_PATH)

    file_size = os.path.getsize(FILE_PATH) / (1024 * 1024)

    print(f"Размер файла: {round(file_size, 2)} МБ")

except Exception as err:
    print(err)
finally:
    driver.quit()
