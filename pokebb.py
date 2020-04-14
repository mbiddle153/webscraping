import requests
import smtplib
import ssl
import time
import os
import datetime
import pdb

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

"""
password = input("password:"
ctx = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
    server.login("mbiddle153@gmail.com", password)
"""

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/"

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   options=chrome_options)

while True:
    #response = requests.get("https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253", headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"})

    response = driver.get("https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253")

    pdb.set_trace()

    body = response.content.decode("UTF-8")

    if body.find("Sold Out") < 0:
        os.system('say "Buy now."')
        """
        server.sendmail(
            "mbiddl153@gmail.com",
            "mbiddle153@gmail.com",
            "https://www.bestbuy.com/site/nintendo-switch-32    gb-console-gray-joy-con/6364253.p?skuId=6364253"
        )
        """
    else:
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print("None available as of:", time)

    time.sleep(300)
