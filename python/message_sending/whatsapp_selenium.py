from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("\nScan QR Code, And then press Enter")
input()
print("Successfully Logged In")



driver.quit()