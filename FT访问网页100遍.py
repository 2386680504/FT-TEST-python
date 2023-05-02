from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "YOUR_DEVICE_NAME",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
    "newCommandTimeout": 180,
    "noReset": True 
}



driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


while True:
    
    driver.unlock()
   

    
   
    driver.start_activity("com.android.chrome","com.google.android.apps.chrome.Main")
    
    
    time.sleep(120)
    
    
    driver.close_app()
    
    
    time.sleep(5)
    
    driver.lock()
    
    
    time.sleep(30)