from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "https://www.amazon.in/Xiaomi-i5-11320H-Resolution-Thunderbolt-Fingerprint/dp/B0BHZM89M6?ref_=Oct_DLandingS_D_a3d58f76_0&th=1"

try:
    driver.get(url)

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/*[@id="add-to-cart-button"]'))
    )
    add_to_cart_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '.// *[ @ id = "corePriceDisplay_desktop_feature_div"] / div[1] / span[2] / span[2] / span[2]'))
    )

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
