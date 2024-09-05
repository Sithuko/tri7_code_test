import uiautomator2 as u2
import time


device = u2.connect()  

device.app_start("com.miui.calculator")  
time.sleep(2)  

converter_tab = device(text="Converter")
if converter_tab.exists:
    converter_tab.click()
    time.sleep(1)

currency_tab = device(text="Currency")
if currency_tab.exists:
    currency_tab.click()
    time.sleep(1)

thai_baht_dropdown = device(text="Thai baht")
if thai_baht_dropdown.exists:
    thai_baht_dropdown.click()
    time.sleep(1)
    device(text="Thai baht").click()  
    time.sleep(1)

quantity_field = device(className="android.widget.EditText", text="1")
if quantity_field.exists:
    quantity_field.click()
    device.clear_text()  
    device.send_keys("1")
    time.sleep(1)
  
usd_dropdown = device(text="USD")
if usd_dropdown.exists:
    usd_dropdown.click()
    time.sleep(1)
    device(text="United States dollar").click() 
    time.sleep(1)
    
usd_value = device.xpath('//android.widget.TextView[contains(@text,"0.")]') 
if usd_value.exists:
    print("USD equivalent:", usd_value.text)

eur_dropdown = device(text="EUR")
if eur_dropdown.exists:
    eur_dropdown.click()
    time.sleep(1)
    device(text="Euro").click()  
    time.sleep(1)

eur_value = device.xpath('//android.widget.TextView[contains(@text,"0.")]') 
if eur_value.exists:
    print("EUR equivalent:", eur_value.text)
