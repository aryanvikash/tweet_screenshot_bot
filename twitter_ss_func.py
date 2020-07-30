from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import os


class twitter:
    def __init__(self, url, filename):
        # Not deleting taken ss due To heroku have large storage for image Lol
        self.filename = filename
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, 'r-1wbh5a2'))
        WebDriverWait(self.driver, 3).until(element_present)
        self.driver.implicitly_wait(2)

    def light_ss(self):
        filename = f'{str(self.filename)}.png'
        print("Taking  light screenshot of tweet")
        sselement = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div/div/section/div/div/div/div[1]/div/div/article/div/div').screenshot_as_png

        im = Image.open(BytesIO(sselement))
        im.save(filename)
        return filename

    def dark_ss(self):
        filename = f'{str(self.filename)}_dark.png'
        print("Taking Dark screenshot of tweet")
        # Text White
        self.driver.execute_script(
            """for(let i of document.getElementsByClassName('r-1qd0xha')) {i.style.color='white';}""")
        # bg dark
        self.driver.execute_script(
            "document.getElementsByClassName('r-1wbh5a2')[5].style.backgroundColor='#222831'")

        # Take screen shot as png
        sselement = self.driver.find_elements_by_css_selector(
            ".css-1dbjc4n.r-eqz5dr.r-16y2uox.r-1wbh5a2")[1].screenshot_as_png
        im = Image.open(BytesIO(sselement))
        im.save(filename)

        return filename

    def close(self):
        print("closing driver")
        self.driver.quit()


if __name__ == "__main__":

    tw = twitter(
        "your_tweet_url", "test")
    try:
        print(tw.dark_ss())
        print(tw.light_ss())
    finally:
        tw.close()
