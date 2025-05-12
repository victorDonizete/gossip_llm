import os
from dotenv import load_dotenv
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

load_dotenv()

def web(url):
  options = webdriver.ChromeOptions()
 # options.add_argument("--headless=new")# roda sem abrir janela
  options.add_argument('--window-size=1920,1080')  # define o tamanho da janela
  # options.add_argument("--force-device-scale-factor=0.50")  # Zoom out (50%)
  # options.add_argument("--high-dpi-support=1")  # Ajuda com resoluções maiores
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  driver.get(url)
  time.sleep(4)
  return driver

def login(driver,url,username=None,password=None):
  current_url = driver.current_url
  if "login" in current_url:
  # Encontra os campos de login e senha
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    # Preenche os campos com as credenciais
    username_field.send_keys(username)
    password_field.send_keys(password)
    # Envia o formulário
    password_field.send_keys(Keys.RETURN)
    # Aguarda o carregamento da página após o login
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    time.sleep(3)
    driver.get(url)
    time.sleep(3)
  else:
    print("already logged in")

def get_screenshot(driver):
  # Executa o comando para capturar a tela
  screenshot = driver.execute_cdp_cmd("Page.captureScreenshot", {"captureBeyondViewport": True, "fromSurface": True})
  return screenshot


def makefolder(web_source:str,path=None):
  if path is None:
    path = os.path.join(os.getcwd(),f"shots/{web_source}/")
  if not os.path.exists(path):
    os.makedirs(path) 
  return path

def save_screenshot(path_screenshot,screenshot):
  # Salva o screenshot em um arquivo
  with open(path_screenshot, "wb") as file:
      file.write(base64.b64decode(screenshot["data"]))
  
def shot_instagram(url,path=None):
  save_path = makefolder("instagram",path)
  try:
    driver = web(url)
    username = os.getenv("IG").username
    password = os.getenv("IG").password
    login(driver,url, username, password)
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='button']")))
    if element:
      actions = ActionChains(driver)
      actions.move_by_offset(1, 200).click().perform()
      time.sleep(3)
  # Tra o screenshot
    screenshot =  get_screenshot(driver)
    user = url.split("/")[-2]
    path_screenshot = os.path.join(save_path,f"shot_{user}.png")
    save_screenshot(path_screenshot,screenshot)
  except Exception as e:
    print(e)
  finally:
        driver.quit()
  return path_screenshot


def shot_facebook(url,save_path=None):
  save_path = makefolder("facebook",save_path)
  # Inicia o navegador
  try:
    driver = web(url)
    login(driver,url)
    element =  driver.find_element(By.XPATH, '//*[@aria-label="Fechar"]')
    if element.is_displayed():
      element.click()
      time.sleep(3)
  # Tra o screenshot
    screenshot =  get_screenshot(driver)
    user = url.split("/")[-2]
    path_screenshot = os.path.join(save_path,f"shot_{user}.png")
    save_screenshot(path_screenshot,screenshot)
  except Exception as e:
    print(e)
  finally:
        driver.quit()
  return path_screenshot

def shot_youtube(url,save_path=None):
  save_path = makefolder("youtube",save_path)
  try:    
    driver = web(url)
    screenshot =  get_screenshot(driver)
    user = url.split("/")[-1]
    path_screenshot =  os.path.join(save_path,f"shot_{user}.png")
    save_screenshot(path_screenshot,screenshot)
  except Exception as e:
    print(e)
  finally:
    driver.quit()
  return path_screenshot

def screen_shot(url,save_path=None):
  if "instagram" in url:
    return shot_instagram(url,save_path),"instagram"
  elif "youtube" in url:
    return shot_youtube(url,save_path),"youtube"
  elif "facebook" in url:
    return shot_facebook(url,save_path),"facebook"
  else:
    print("URL não suportada")




  """  <i data-visualcompletion="css-img"
    class="x1b0d499 x1d69dk1" 
    aria-hidden="true" 
    style="background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v4/yF/r/FC6fVVGEdvy.png&quot;);" \
    " background-position: -84px -80px;" \
    " background-size: auto; width: 20px; " \
    "height: 20px;" \
    " background-repeat: no-repeat;" \
    " display: inline-block;"></i>

<div aria-label="Fechar" 
class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xzolkzo x12go9s9 x1rnf11y xprq8jg x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1"
role="button"
tabindex="0">
<i data-visualcompletion="css-img" class="x1b0d499 x1d69dk1" aria-hidden="true" style="background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v4/yF/r/FC6fVVGEdvy.png&quot;); background-position: -84px -80px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;">
</i><div class="x1ey2m1c xds687c x17qophe xg01cxk x47corl x10l6tqk x13vifvy x1ebt8du x19991ni x1dhq9h xzolkzo x12go9s9 x1rnf11y xprq8jg" role="none" data-visualcompletion="ignore" style="inset: 0px;"></div></div>
"""