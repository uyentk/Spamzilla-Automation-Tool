from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 

def App():
    options = uc.ChromeOptions()
    prefs = {"credentials_enable_service": False,
            "profile.password_manager_enabled": False, 
            "download.default_directory" : "D:\ASM\SpamzillaExport\Spamzilla-Automation-Tool\data"}
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(use_subprocess=True, options=options)
    wait = WebDriverWait(driver, 20)

    user = "asmmoneysite"
    password = "$10k1month"
    url = "https://members.azadseo.com/login"
    driver.get(url)

    # Login 
    wait.until(EC.visibility_of_element_located((By.NAME, 'amember_login'))).send_keys(user)
    wait.until(EC.visibility_of_element_located((By.NAME, 'amember_pass'))).send_keys(password)
    wait.until(EC.visibility_of_element_located((By.ID, 'submit'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Spamzilla")]'))).click()

    # Switch to Spamzilla dashboard
    p = driver.current_window_handle
    parent = driver.window_handles[0]
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    # print(driver.title) 

    # Set filter
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title = 'Filters']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Reset Filter')]"))).click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    wait.until(EC.visibility_of_element_located((By.NAME, "Filter[majestic_tf_from]"))).send_keys(9)
    wait.until(EC.visibility_of_element_located((By.NAME, "Filter[moz_da_from]"))).send_keys(30)
    wait.until(EC.visibility_of_element_located((By.NAME, "Filter[expiry_period]"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "Filter[remove_reviewed]"))).click()
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Apply Filter')]"))).click()
    time.sleep(20)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title = 'Export']"))).click()
    Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='domainsCount']")))).select_by_value('5000')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#exportModal > div > div > div.modal-body > form > a:nth-child(4)"))).click()
    time.sleep(50)

# App()
