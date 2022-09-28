from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time
import pytest


d = webdriver.Chrome(r"C:\Users\ianve\Documents\Universidad\7 Semestre\Calidad de Software\chromedriver.exe")
d.get("https://www.demoblaze.com/index.html")
d.maximize_window()

dict = {
    0:
        [
            '/html/body/div[5]/div/div[1]/div/a[2]',
            '//*[@id="tbodyid"]/div[1]/div/div/h4/a',
            '//*[@id="tbodyid"]/div[2]/div/div/h4/a'
        ],
    1:
        [
            '/html/body/div[5]/div/div[1]/div/a[3]',
            '//*[@id="tbodyid"]/div[1]/div/div/h4/a',
            '//*[@id="tbodyid"]/div[2]/div/div/h4/a'
        ],
    2:
        [
            '/html/body/div[5]/div/div[1]/div/a[4]',
            '//*[@id="tbodyid"]/div[1]/div/div/h4/a',
            '//*[@id="tbodyid"]/div[2]/div/div/h4/a'
        ]
}


def registrar(d):
    reg = d.find_element(By.ID, "signin2")
    reg.click()

    time.sleep(2)
    d.find_element(By.XPATH, '//*[@id="sign-username"]').send_keys('Usuario123')
    d.find_element(By.ID, "sign-password").send_keys('Contraseña')

    enter = d.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    time.sleep(2)
    enter.click()

    time.sleep(2)
    Alert(d).accept()

def ingresar(d):
    log = d.find_element(By.ID, "login2")
    log.click()

    time.sleep(2)
    d.find_element(By.ID, "loginusername").send_keys('Usuario123')
    d.find_element(By.ID, "loginpassword").send_keys('Contraseña')

    enter = d.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    
    time.sleep(2)
    enter.click()

def seleccion(d):
    for i in range(0, len(dict)):
        for j in range(0, len(dict[i])):
            tmp = str(dict[i][j])
            d.find_element(By.XPATH, str(dict[i][j])).click()
            time.sleep(5)
            if j > 0:
                d.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a").click()
                time.sleep(2)
                Alert(d).accept()
                time.sleep(3)
                d.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
                time.sleep(5)
                d.find_element(By.XPATH, str(dict[i][0])).click()
                time.sleep(3)
        time.sleep(5)
print(len(dict))

registrar(d)
ingresar(d)
seleccion(d)