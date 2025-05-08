from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import base64
import time


# Abre o site desejado
def shot_instagram(url):
  options = webdriver.ChromeOptions()
 # options.add_argument("--headless=new")# roda sem abrir janela
  options.add_argument('--window-size=1920,1080')  # define o tamanho da janela
  # options.add_argument("--force-device-scale-factor=0.50")  # Zoom out (50%)
  # options.add_argument("--high-dpi-support=1")  # Ajuda com resoluções maiores


  # Inicia o navegador
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  try:
    _url = url  # <-- troque pela URL desejada
    driver.get(_url)
    actions = ActionChains(driver)
    time.sleep(4)
    current_url = driver.current_url
    if "login" in current_url:
      driver.find_element(By.NAME, "username").send_keys("gilbertao11@outlook.com.br")
      driver.find_element(By.NAME, "password").send_keys("TAwqp5YdvpCkXcW" + Keys.RETURN)
      time.sleep(4)
      driver.get(_url)
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='button']")))
    if element:
      actions.move_by_offset(1, 200).click().perform()
      time.sleep(3)
  # Tra o screenshot
    screenshot = driver.execute_cdp_cmd("Page.captureScreenshot", {"captureBeyondViewport": True, "fromSurface": True})
    user = _url.split("/")[-2]
    path_screenshot = f"F:/Usuário/Documents/GitHub/llm_lang/shots/screenshot_{user}.png"
    with open(path_screenshot, "wb") as file:
        file.write(base64.b64decode(screenshot["data"]))
    # driver.save_screenshot(f"F:/Usuário/Documents/GitHub/llm_lang/shots/screenshot_{user}.png")
    print(f"Print salvo como screenshot_{user}.png")
  except Exception as e:
    print(e)
  finally:
        driver.quit()
  return path_screenshot