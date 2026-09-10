import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# اكتب بيانات دخولك هنا مباشرة بين التنصيص
USERNAME = "fifa222"
PASSWORD = "FIFA13133144"
# ==========================================

# إعداد خيارات المتصفح للعمل في بيئة GitHub Actions
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

    print("2. إدخال اليوزر نيم والباسورد...")
    user_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' or @type='email' or @name='username' or @name='email']"))
    )
    user_input.clear()
    user_input.send_keys(USERNAME)

    pass_input = driver.find_element(By.XPATH, "//input[@type='password' or @name='password']")
    pass_input.clear()
    pass_input.send_keys(PASSWORD)

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Login') or contains(text(), 'دخول')]")
    login_btn.click()

    print("3. الانتقال إلى لوحة التحكم...")
    time.sleep(5)
    driver.get("https://ahmed-amedo.com/dashboard")
    time.sleep(3)

    print("4. بدء حلقة عمل Refresh للصفحة كل دقيقة لمنع خروج البوتات...")
    
    # يعمل لمدة 30 دقيقة (مُدة التشغيل الافتراضية للجيت هب)
    for minute in range(1, 31):
        time.sleep(60)  # الانتظار 60 ثانية
        driver.refresh()
        print(f"🔄 تم عمل Refresh للصفحة بنجاح (الدقيقة {minute}/30)")

except Exception as e:
    print(f"❌ حدث خطأ أثناء تنفيذ السكريبت: {e}")

finally:
    driver.quit()
    print("تم إغلاق المتصفح.")
