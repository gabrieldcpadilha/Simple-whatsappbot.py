# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# definir contatos e mensagem a ser enviada
contatos = ['Eliana Nogueira', 'Aníbal Padilha', 'Amor']
mensagem = 'Teste N2: Testando script de envio de mensagens automáticas. :D :D :D'


# campo de pesquisa 'copyable-text selectable-text' OBS: index[0]
def buscar_contato(contato):
    campo_pesquisa_contato = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]'
    )
    time.sleep(5)
    campo_pesquisa_contato.click()
    campo_pesquisa_contato.send_keys(contato)
    campo_pesquisa_contato.send_keys(Keys.ENTER)


# campo de mensagem privada 'copyable-text selectable-text' OBS: index[1]
def enviar_mensagem(mensagem):
    campo_pesquisa_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]'
    )
    time.sleep(5)
    campo_pesquisa_mensagem[1].click()
    campo_pesquisa_mensagem[1].send_keys(mensagem)
    campo_pesquisa_mensagem[1].send_keys(Keys.ENTER)


# buscar contatos e enviar mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
