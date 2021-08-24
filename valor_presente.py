from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

class PresentValue:
    def __init__(self, driver_path = "..", application_path="https://administracao-financeira.vercel.app/valor-presente"):
        # Instancia do driver
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(application_path)

        # Encontra os inputs
        self.valor_futuro = self.driver.find_element_by_id("valor_futuro")
        self.taxa = self.driver.find_element_by_id("taxa_valor_futuro")
        self.periodos = self.driver.find_element_by_id("periodos_valor_futuro")

        # Encontra o elemento do resultado
        self.resultado = self.driver.find_element_by_id("resultado")

        # Encontra o botão de submit
        self.submit = self.driver.find_element_by_id("submit")

    def calculate(self, value, i, t):
        # Atribui os valores do objeto atual
        self.value = value
        self.i = i
        self.t = t

        # Preenche os dados
        self.valor_futuro.send_keys(str(self.value))
        self.taxa.send_keys(str(self.i))
        self.periodos.send_keys(str(self.t))

        # Pressionar o botao
        self.submit.click()

        # Valor do resultado
        self.result = re.findall("((\d+)\.(\d+))", self.resultado.get_attribute("innerText"))
        self.result = float([i[0] for i in self.result][0])

        self.driver.close()

        return self.result