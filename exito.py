
## ******************************************************************************
## no continue con el del exito debido a que fue imposible seleccionar en la fecha, debido a que no es un tabla ul o li
## ******************************************************************************


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

# Ubicación del controlador de Chrome
PATH = "./chromedriver"
options = Options()
service = Service(PATH)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.viajesexito.com/")

# Encontrar el campo de búsqueda de destino y escribir "Jose maria cordova"
time.sleep(2)
destino_textfield = driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
destino_textfield.click()
destino_textfield = driver.find_element(By.ID,"CityPredictiveFrom_netactica_airhotel")
destino_textfield.click()
destino_textfield = driver.find_element(By.ID,"popUpCityPredictiveFrom_netactica_airhotel")
time.sleep(2)
destino_textfield.send_keys('Jose Maria Cordova')
destino_textfield.send_keys(Keys.ENTER)
time.sleep(2)

# Encontrar el campo de búsqueda de destino y escribir "Cancun"
destino_textfield = driver.find_element(By.ID,"CityPredictiveTo_netactica_airhotel")
destino_textfield.click()
destino_textfield = driver.find_element(By.ID,"popUpCityPredictiveTo_netactica_airhotel")
time.sleep(2)
destino_textfield.send_keys('Cancun')
destino_textfield.send_keys(Keys.ENTER)
time.sleep(2)

# Selecciona la fecha de salida"
destino_textfield = driver.find_element(By.ID,"Date_netactica_air_hotel")
destino_textfield.click()
time.sleep(2)
destino_textfield = driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[5]/div[2]/div[1]")
destino_textfield.click()
time.sleep(8)

# destino_textfield = driver.find_element(By.XPATH,"//*[@id='Body']/div[10]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]")
# destino_textfield.click()
# time.sleep(3)


driver.close()