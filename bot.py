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
    print("1. فتح صفحة الدخول...")
    driver.get("https://ahmed-amedo.com/login")
    time.sleep(3)

    print("2. إدخال البيانات...")
    # إدخال البيانات باستخدام اسم العنصر بدلاً من الـ XPath العام
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys(email)

    pass_input = driver.find_element(By.NAME, "password")
    pass_input.send_keys(password)

    # الضغط على زر الدخول
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()

    print("3. انتظار الانتقال للوحة التحكم والبحث عن الزرار...")
    time.sleep(5)

    # الانتقال للوحة التحكم مباشرة للتأكيد
    driver.get("https://ahmed-amedo.com/dashboard")
    time.sleep(3)

    xpath_btn = "//button[contains(text(), 'تشغيل البوت')]"

    # التكرار لمدة 30 دقيقة يفحص وجود الزرار كل ثانية
    for i in range(1800):
        try:
            buttons = driver.find_elements(By.XPATH, xpath_btn)
            if len(buttons) > 0 and buttons[0].is_displayed():
                buttons[0].click()
                print(f"✅ تم الضغط على زر تشغيل البوت بنجاح عند المحاولة {i+1}!")
                time.sleep(15)
        except Exception:
            pass
        time.sleep(1)

except Exception as e:
    print(f"❌ حدث خطأ: {e}")

finally:
    driver.quit()
