import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# базовый url
base_url = 'https://www.saucedemo.com/'

# драйвер для Chrome, открытие браузера
driver_chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
# переход по url в браузере
driver_chrome.get(base_url)
# команда для открытия окна в максимальном для монитора разрешении
driver_chrome.maximize_window()
# таймер на 10 секунд
time.sleep(10)
# закрытие браузера
driver_chrome.close()

# драйвер для Firefox, открытие браузера
driver_firefox = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)
# переход по url в браузере
driver_firefox.get(base_url)
# команда для открытия окна в максимальном для монитора разрешении
driver_firefox.maximize_window()
# таймер на 10 секунд
time.sleep(10)
# закрытие браузера
driver_firefox.close()

# драйвер для Edge, открытие браузера
driver_edge = webdriver.Edge(
    service=EdgeService(EdgeChromiumDriverManager().install())
)
# переход по url в браузере
driver_edge.get(base_url)
# команда для открытия окна в максимальном для монитора разрешении
driver_edge.maximize_window()
# таймер на 10 секунд
time.sleep(10)
# закрытие браузера
driver_edge.close()
