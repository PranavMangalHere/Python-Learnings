# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# driver.get("https://www.google.com")

"""
👉 What’s happening here?
ChromeDriverManager().install() → downloads driver
Service() → connects driver to Selenium
webdriver.Chrome() → launches browser
"""

# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

"""
👉 Useful Options:
--start-maximized
--incognito
--headless (runs without UI 🔥)
"""



"""
🔹 7. Headless Mode (Advanced Insight 👀)
options.add_argument("--headless")

👉 Runs browser in background (no UI)
💡 Used in:
CI/CD pipelines
Fast automation
"""
