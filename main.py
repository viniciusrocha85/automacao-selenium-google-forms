from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

url = r'https://docs.google.com/forms/d/e/1FAIpQLSc6rujMUWQR2us3-eHxRdSmoyvVIanFSUrc-LETTyECjgB4qQ/viewform'
navegador.get(url=url)
time.sleep(5)

navegador.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('João Vinicius Araújo Rocha')
navegador.find_element('xpath', r'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('viniciusrocha6272@gmail.com')
time.sleep(5)
navegador.find_element('xpath', r'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
time.sleep(5)

navegador.quit()