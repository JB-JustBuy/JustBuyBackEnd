from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time


def test_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://accounts.google.com/signup")

    #open the new tab in driver
    driver.execute_script("window.open('https://www.google.com');")
    time.sleep(2)
    # driver.get('https://www.google.com/webhp?hl=zh-TW&sa=X&ved=0ahUKEwjG-vKNg6zuAhWdL6YKHRizBnUQPAgI')
    # prints parent window title
    print("Parent window title(before switch): " + driver.title)
    driver.switch_to.window(driver.window_handles[1])
    print("Parent window title(after switch): " + driver.title)

    driver.close()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])

    driver.close()
    print("switch to origin tab")

if __name__ == '__main__':
    test_driver()