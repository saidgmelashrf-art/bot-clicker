import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://ahmed-amedo.com/dashboard")
    time.sleep(5)
    print("تم الدخول للموقع بنجاح!")
except Exception as e:
    print(f"حدث خطأ: {e}")
finally:
    driver.quit()
