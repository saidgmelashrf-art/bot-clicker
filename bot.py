import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# إعداد خيارات المتصفح للعمل في بيئة GitHub Actions
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # التشغيل الخفي بدون شاشة
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

# جلب بيانات تسجيل الدخول من Secrets الخاص بـ GitHub
USERNAME = os.environ.get("BOT_USERNAME")
PASSWORD = os.environ.get("BOT_PASSWORD")

try:
    print("جاري فتح الموقع...")
    driver.get("https://ahmed-amedo.com/login")  # ضع رابط صفحة تسجيل الدخول هنا

    # تسجيل الدخول
    print("جاري إدخال بيانات تسجيل الدخول...")
    user_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))  # عدل اسم الحقل إذا كان مختلفاً
    pass_input = driver.find_element(By.NAME, "password")
    
    user_input.send_keys(USERNAME)
    pass_input.send_keys(PASSWORD)
    
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    
    time.sleep(3)
    
    # التوجه لصفحة البوت/الزر
    print("جاري الانتقال للوحة التحكم ومراقبة الزر...")
    driver.get("https://ahmed-amedo.com/dashboard")  # ضع رابط لوحة التحكم التي يوجد بها الزر

    # حلقة التكرار لمراقبة والضغط على الزر
    for i in range(10):
        try:
            # ابحث عن الزر باستخدام النص أو ID أو Class
            click_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'تشغيل') or contains(text(), 'Start')]")))
            click_btn.click()
            print(f"تم الضغط على الزر بنجاح! (محاولة {i+1})")
        except Exception as e:
            print(f"لم يتم العثور على الزر أو غير قابل للضغط حالياً: {e}")
        
        time.sleep(5)

except Exception as main_e:
    print(f"حدث خطأ أثناء تنفيذ السكريبت: {main_e}")

finally:
    driver.quit()
    print("تم إغلاق المتصفح.")
