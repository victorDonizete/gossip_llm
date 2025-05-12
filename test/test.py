# import os
# import shot

# driver  = shot.web("https://www.facebook.com/rafaela.garcia.743497")
# wait = shot.WebDriverWait(driver,10)
# fechar_botao =  wait.until(shot.EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Fechar"]')))
# location = fechar_botao.location
# x = location['x']
# y = location['y']

# # Clicando diretamente nas coordenadas do botão
# driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)
# driver.execute_script("document.elementFromPoint(arguments[0], arguments[1]).click();", x, y)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Inicializando o WebDriver
# driver = webdriver.Chrome()

# # Acessando a página
# driver.get('https://www.facebook.com/rafaela.garcia.743497')

# # Localizando o botão de fechar
# fechar_botao = driver.find_element(By.XPATH, '//*[@aria-label="Fechar"]')
# print(fechar_botao)
# # Verificando se o botão está visível
# if fechar_botao.is_displayed():
#     print("O botão está visível!")
#     fechar_botao.click()
#     time.sleep(10)
# else:
#     print("O botão não está visível!")
from prompts import Prompts

print(Prompts("youtube").get())