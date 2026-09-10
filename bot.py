import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# جلب البيانات من Secrets
email = os.environ.get("BOT_EMAIL")
password = os.environ.get("BOT_PASSWORD")

if not email or not password:
    print("❌ خطأ: لم يتم العثور على BOT_EMAIL أو BOT_PASSWORD في GitHub Secrets!")
    exit(1)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    print("1. فتح صفحة الدخول...")
    driver.get("https://ahmed-amedo.com/login")
    time.sleep(2)

    print("2. جاري إدخال بيانات تسجيل الدخول...")
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @name='email' or @name='username' or @type='text']")))
    email_input.send_keys(email)

    pass_input = driver.find_element(By.XPATH, "//input[@type='password']")
    pass_input.send_keys(password)

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()

    print("3. انتظار الانتقال للوحة التحكم ومراقبة الزر...")
    time.sleep(5)
    driver.get("https://ahmed-amedo.com/dashboard")

    xpath_btn = "//button[contains(text(), 'تشغيل') or contains(text(), 'Start')]"

    for i in range(1800):
        try:
            buttons = driver.find_elements(By.XPATH, xpath_btn)
            if len(buttons) > 0 and buttons[0].is_displayed():
                buttons[0].click()
                print(f"✅ تم الضغط على زر تشغيل البوت بنجاح عند المحاولة {i+1}!")
                time.sleep(10)
        except Exception:
            pass
        time.sleep(1)

except Exception as e:
    print(f"❌ حدث خطأ أثناء تنفيذ السكريبت: {e}")

finally:
    driver.quit()
    print("تم إغلاق المتصفح.")
