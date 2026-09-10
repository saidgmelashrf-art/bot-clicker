import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

email = os.environ.get("BOT_EMAIL")
password = os.environ.get("BOT_PASSWORD")

try:
    print("1. تسجيل الدخول...")
    driver.get("https://ahmed-amedo.com/login")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    print("2. بدء المراقبة المستمرة كل ثانية...")
    xpath_btn = "//button[contains(text(), 'تشغيل البوت')]"

    # الحلقة التكرارية تفحص وجود الزرار كل ثانية لمدة 30 دقيقة
    for i in range(1800):
        try:
            # البحث عن الزرار في الصفحة
            buttons = driver.find_elements(By.XPATH, xpath_btn)
            
            if len(buttons) > 0 and buttons[0].is_displayed():
                buttons[0].click()
                print(f"✅ تم العثور على الزرار والضغط عليه بنجاح في الثانية رقم {i+1}!")
                time.sleep(10) # انتظار قليلاً لتأكيد الضغط
            else:
                # إذا لم يكن الزرار موجوداً أو تم الضغط عليه، انتظر ثانية واحدة وكرر الفحص
                pass

        except Exception as inner_e:
            pass

        time.sleep(1) # الفحص كل ثانية واحدة بالضبط

except Exception as e:
    print(f"❌ حدث خطأ الرئيسي: {e}")

finally:
    driver.quit()
