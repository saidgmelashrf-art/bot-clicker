import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

email = os.environ.get("BOT_EMAIL")
password = os.environ.get("BOT_PASSWORD")

try:
    print("1. فتح صفحة تسجيل الدخول...")
    driver.get("https://ahmed-amedo.com/login")
    time.sleep(2)

    print("2. كتابة بيانات الدخول...")
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    print("3. جاري مراقبة الشاشة لانتظار ظهور زرار 'تشغيل البوت'...")
    
    xpath_btn = "//button[contains(text(), 'تشغيل البوت')]"
    
    start_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, xpath_btn))
    )

    start_button.click()
    print("✅ تم العثور على الزرار والضغط عليه بنجاح!")

except Exception as e:
    print(f"❌ حدث خطأ أو لم يظهر الزرار في الوقت المحدد: {e}")

finally:
    driver.quit()
