from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


# Ubicación del controlador de Chrome
PATH = "./chromedriver"
options = Options()
service = Service(PATH)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.carulla.com")

# se selecciona el menu hamburguesa y se da click
apuntador = driver.find_element(By.ID,"category-menu")
apuntador.click()
time.sleep(3)

# se posiciona en vida sana y le da click
apuntador = driver.find_element(By.ID,"undefined-nivel2-Vida sana")
apuntador.click()
time.sleep(3)

# se va hasta gluten y da click
apuntador = driver.find_element(By.ID,"Categorías-nivel2-Libre de gluten")
apuntador.click()
time.sleep(10)

# escribe medellin en el input del selector y se da enter
apuntador = driver.find_element(By.XPATH,"/html/body/div[10]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div/div/input")
apuntador.send_keys('Medellin')
apuntador.send_keys((Keys.ENTER))
time.sleep(5)

# escribe el carulla en el input del selector y se da enter
apuntador = driver.find_element(By.XPATH,"/html/body/div[10]/div[1]/div/div/div[2]/div[4]/div[3]/div[2]/div/div/div/div[1]/div/div/input")
apuntador.send_keys('Carulla san lucas')
apuntador.send_keys((Keys.ENTER))
time.sleep(5)

# se presiona el boton confirmar
apuntador = driver.find_element(By.CLASS_NAME,"exito-geolocation-3-x-primaryButtonEnable")
apuntador.click()
time.sleep(7)

# se seleciona los cerales avenas y granolas
apuntador = driver.find_element(By.ID,"category-2-cereales-avena-y-granolas")
apuntador.click()
time.sleep(8)

# Localiza el elemento de la pantalla del que deseas tomar el texto
nombre = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[1]/section/a/article/div[3]/div[2]/div/div/div/div[2]/div/span")
descripcion = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[1]/section/a/article/div[3]/div[2]/div/div/div/div[3]/div/div/div/h3/span")
precio = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[1]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span")
time.sleep(1)
texto1 = nombre.text
texto3 = precio.text
texto2 = descripcion.text

# Localiza el elemento de la pantalla del que deseas tomar el texto
nombre = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[2]/section/a/article/div[3]/div[2]/div/div/div/div[3]")
descripcion = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[2]/section/a/article/div[3]/div[2]/div/div/div/div[3]/div/div/div/h3/span")
precio = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[2]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span")
time.sleep(1)
texto4 = nombre.text
texto5 = descripcion.text
texto6 = precio.text

# Localiza el elemento de la pantalla del que deseas tomar el texto
nombre = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[2]/div/span")
descripcion = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[3]/div/div/div/h3/span")
precio = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span")
time.sleep(1)
texto7 = nombre.text
texto8 = descripcion.text
texto9 = precio.text

# Localiza el elemento de la pantalla del que deseas tomar el texto
nombre = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[4]/section/a/article/div[3]/div[2]/div/div/div/div[2]/div/span")
descripcion = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[4]/section/a/article/div[3]/div[2]/div/div/div/div[3]/div/div/div/h3/span")
precio = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[4]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span")
time.sleep(1)
texto10 = nombre.text
texto11 = descripcion.text
texto12 = precio.text

# Imprime el texto por consola
print(texto1, texto2, texto3)
print(texto4, texto5, texto6)
print(texto7, texto8, texto9)
print(texto10, texto11, texto12)
time.sleep(5)

# ingresa a uno de los productos buscados
apuntador = driver.find_element(By.XPATH,"//*[@id='gallery-layout-container']/div[1]")
apuntador.click()
time.sleep(3)

# Se realiza el scroll hacia abajo y se a click en el icono youtube
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
apuntador = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div/div[2]/section/div/div[3]/div/div[2]/div/div[1]/div[2]/a[4]")
apuntador.click()
time.sleep(8)

# Cerrar el controlador de Chrome y el navegador
driver.close()
