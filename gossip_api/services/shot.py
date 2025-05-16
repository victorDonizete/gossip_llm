import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import base64
import time

load_dotenv()
def web(url):
    # Configure Chrome options for headless operation with Docker
    options = Options()
    options.add_argument("--headless") # roda sem abrir janela
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080") # define o tamanho da janela
    options.binary_location = "/opt/chrome-linux64/chrome" # caminho do chromeDriver
    # options.add_argument("--force-device-scale-factor=0.50")  # Zoom out (50%)
    # options.add_argument("--high-dpi-support=1")  # Ajuda com resoluções maiores
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.get(url)
    time.sleep(3)
    return driver


def login(driver, url, username=None, password=None):
    current_url = driver.current_url
    if "login" in current_url:
        # Encontra os campos de login e senha
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        # Preenche os campos com as credenciais
        username_field.send_keys(username)
        password_field.send_keys(password + Keys.RETURN)
        # Envia o formulário
        # password_field.send_keys(Keys.RETURN)
        # Aguarda o carregamento da página após o login
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
        time.sleep(4)
        driver.get(url)
        time.sleep(3)
    else:
        print("already logged in")


def get_screenshot(driver):
    # Executa o comando para capturar a tela
    screenshot = driver.execute_cdp_cmd(
        "Page.captureScreenshot", {"captureBeyondViewport": True, "fromSurface": True}
    )
    return screenshot


def makefolder(web_source: str, path=None):
    if path is None:
        path = os.path.join(os.getcwd(), f"shots/{web_source}/")
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def save_screenshot(path_screenshot, screenshot):
    # Salva o screenshot em um arquivo
    with open(path_screenshot, "wb") as file:
        file.write(base64.b64decode(screenshot["data"]))


def shot_instagram(url, path=None):
    save_path = makefolder("instagram", path)
    try:
        driver = web(url)
        actions = ActionChains(driver)
        credentials = json.loads(os.getenv("IG"))
        username = credentials.get("username")
        password = credentials.get("password")
        login(driver, url, username, password)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='button']"))
        )
        if element:
            actions.move_by_offset(1, 200).click().perform()
            time.sleep(5)
        # Tra o screenshot
        screenshot = get_screenshot(driver)
        user = url.split("/")[-2]
        path_screenshot = os.path.join(save_path, f"shot_{user}.png")
        save_screenshot(path_screenshot, screenshot)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    return path_screenshot


def shot_facebook(url, save_path=None):
    save_path = makefolder("facebook", save_path)
    # Inicia o navegador
    try:
        driver = web(url)
        login(driver, url)
        element = driver.find_element(By.XPATH, '//*[@aria-label="Fechar"]')
        if element.is_displayed():
            element.click()
            time.sleep(3)
        # Tra o screenshot
        screenshot = get_screenshot(driver)
        user = url.split("/")[-2]
        path_screenshot = os.path.join(save_path, f"shot_{user}.png")
        save_screenshot(path_screenshot, screenshot)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    return path_screenshot


def shot_youtube(url, save_path=None):
    save_path = makefolder("youtube", save_path)
    try:
        driver = web(url)
        screenshot = get_screenshot(driver)
        user = url.split("/")[-1]
        path_screenshot = os.path.join(save_path, f"shot_{user}.png")
        save_screenshot(path_screenshot, screenshot)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    return path_screenshot


def screen_shot(url, save_path=None):
    if "instagram" in url:
        return shot_instagram(url, save_path), "instagram"
    elif "youtube" in url:
        return shot_youtube(url, save_path), "youtube"
    elif "facebook" in url:
        return shot_facebook(url, save_path), "facebook"
    else:
        print("URL não suportada")

   
