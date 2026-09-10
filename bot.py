import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# جلب بيانات الدخول من Secrets
email = os.environ.get("BOT_EMAIL")
password = os.environ.get("BOT_PASSWORD")

# التحقق من وجود البيانات لتفادي خطأ NoneType
if not email or not password:
    print("❌ خطأ: لم يتم العثور على BOT_EMAIL أو BOT_PASSWORD في GitHub Secrets!")
    print("تأكد من إضافة السكرتس من Settings -> Secrets and variables -> Actions")
    exit(1)

# إعداد خيارات المتصفح للعمل بدون شاشة في GitHub Actions
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

try:
    print("1. جاري فتح صفحة تسجيل الدخول...")
    driver.get("https://ahmed-amedo.com/login")
    time.sleep(3)

    print("2. إدخال اسم المستخدم وكلمة السر...")
    email_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' or @type='email' or @name='username' or @name='email']"))
    )
    email_input.clear()
    email_input.send_keys(email)

    pass_input = driver.find_element(By.XPATH, "//input[@type='password' or @name='password']")
    pass_input.clear()
    pass_input.send_keys(password)

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Login') or contains(text(), 'دخول')]")
    login_btn.click()

    print("3. تم الضغط على زر الدخول، جاري الانتظار والتوجيه للوحة التحكم...")
    time.sleep(5)
    driver.get("https://ahmed-amedo.com/dashboard")
    time.sleep(3)

    xpath_btn = "//button[contains(text(), 'تشغيل') or contains(text(), 'Start') or contains(@class, 'start') or contains(@id, 'start')]"

    print("4. البدء في مراقبة زر التشغيل وتجديد الصفحة تلقائياً...")
    
    # حلقة مراقبة تستمر طوال فترة تشغيل السكريبت
    for i in range(1800):
        try:
            # البحث عن زر التشغيل والضغط عليه إن وجد
            buttons = driver.find_elements(By.XPATH, xpath_btn)
            if len(buttons) > 0 and buttons[0].is_displayed():
                buttons[0].click()
                print(f"✅ تم الضغط على زر تشغيل البوت بنجاح عند المحاولة رقم {i+1}!")
                time.sleep(5)

            # تجديد الصفحة كل 300 ثانية (5 دقائق) لمنع الخروج أو انقطاع الجلسة
            if i > 0 and i % 300 == 0:
                print("🔄 جاري إعادة تحميل الصفحة (Refresh) لتجديد الاتصال ومنع خروج البوتات...")
                driver.refresh()
                time.sleep(5)

        except Exception:
            pass
            
        time.sleep(1)

except Exception as e:
    print(f"❌ حدث خطأ أثناء تشغيل السكريبت: {e}")

finally:
    driver.quit()
    print("تم إغلاق المتصفح.")
