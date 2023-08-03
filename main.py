import sys
import time
import codecs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# First argument is python file location, second one is URL
URL = sys.argv[1]

if len(sys.argv) > 1:

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--detach")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    wait = WebDriverWait(driver, 2)

    # Find all of the comment elements
    commentElements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#-post-rtjson-content p')))
    #commentElements = driver.find_elements_by_css_selector("#-post-rtjson-content p")

    f = codecs.open("comments.txt", "a", "utf-8")

    for element in commentElements:
        comment = element.get_attribute("innerText")

        if comment:
            # Write to file
            f.write(comment + "\n\r")
    
    print("Done!")
    f.close()
    driver.quit()

else:
    print("ERROR: Please enter a post URL")