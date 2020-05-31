from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

chromeDriver ='driver/chromedriverMac'
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=profile/candra")
driver = webdriver.Chrome(chromeDriver, options=chrome_options)

sleep(1)
driver.get('https://web.whatsapp.com')
sleep(17)   # kasih waktu untuk melakukan scan QrCode

def sendMessage(name,message):
    input_box = driver.find_element_by_css_selector("._2S1VP")
    input_box.click()
    input_box.send_keys(name + Keys.ENTER)
    sleep(1)
    inputbox = driver.find_element_by_css_selector("div[data-tab='1']")
    inputbox.click()
    sleep(1)
    inputbox.send_keys(message)
    send_button = driver.find_element_by_css_selector("span[data-icon='send']")
    sleep(1)
    send_button.click()

sendMessage("Javas","Hai, ini pesan dari Python ")
sleep(1)
sendMessage("Javas","Menggunakan Selenium dan ChromeDriver")
sleep(1)
sendMessage("Javas","Terima kasih...")
sleep(3)
driver.close();