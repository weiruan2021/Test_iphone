# from selenium.webdriver.support import  expected_conditions as EC
import csv
import os
import sys
import time
import unittest
from ast import Suite
from time import sleep
from unittest import suite

from appium import webdriver

# from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class test_about(unittest.TestCase):
    # Start of script
    def setUp(self):
        desired_caps = dict(
            platformName="iOS",
            platformVersion="15.4",
            automationName="xcuitest",
            deviceName="iPhone 11",
            browserName="Safari",
        )
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.get("https://healthcare-tech.co.jp")
        sleep(2)
        screenshot_folder = os.getenv("SCREENSHOT_PATH", "/tmp")
        self.driver.save_screenshot(screenshot_folder + "/devicefarm.png")
        sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_about(self):
        el1 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/div/header/div/div[2]"
        )
        time.sleep(1)
        el1.click()
        # About start
        el2 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div/div[2]/nav/ul[1]/li[1]/a"
        )

        el2.click()
        time.sleep(5)
        el3 = self.driver.find_element(by=By.CLASS_NAME, value="about__bg_picture_file")
        assert (
            el3.get_attribute("src")
            == "https://healthcare-tech.co.jp/elements/images/about/main.jpg"
        )
        time.sleep(3)

        el4 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/main/section[1]/div[2]"
        )
        assert el4.get_attribute("class") == "about__detail_content"
        time.sleep(1)
        el4.click()

    def test_message(self):
        el1 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/div/header/div/div[2]"
        )
        time.sleep(1)
        el1.click()
        # About start
        el2 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div/div[2]/nav/ul[1]/li[1]/a"
        )

        el2.click()
        time.sleep(1)
        # scroll
        size = self.driver.get_window_size()
        starty = size.get("height") * 0.80
        endy = size.get("height") * 0.20
        startx = size.get("width") / 2
        self.driver.swipe(startx, starty, startx, endy, 3000)

        el5 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/main/section[2]/div"
        )
        time.sleep(1)
        el5.click()

        el7 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/main/section[2]/div/div[2]"
        )
        el7.text == "世界トップレベルと言われる日本の医療。\nその高い質の維持は、医療やヘルスケア業界に携わる人々の献身的な努力によって支えられてきました。\nしかし、かつて人類が経験したことのない超高齢化社会を目前にし、当たり前のように存在していた、だれでも・いつでも・どこでも受けられる“保健医療の安心”を、従来の方法で維持していくことは困難となってきています。\n医療費の増大や医療従事者の疲弊、家族を取り巻く環境の変化といった課題を、どのように解決していくべきか。\n そのひとつの答えとして、私たちヘルスケアテクノロジーズはICTやAIといった技術を活用した、よりスマートで、よりオープンなヘルスケアサービスを提供していきます。"
        time.sleep(1)

    def test_corporate(self):
        el1 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/div/header/div/div[2]"
        )
        time.sleep(1)
        el1.click()
        # About start
        el2 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div/div[2]/nav/ul[1]/li[1]/a"
        )

        el2.click()
        time.sleep(1)

        # scroll
        size = self.driver.get_window_size()
        starty = size.get("height") * 0.80
        endy = size.get("height") * 0.20
        startx = size.get("width") / 2
        time.sleep(1)
        self.driver.swipe(startx, starty, startx, endy, 6000)
        size = self.driver.get_window_size()
        starty = size.get("height") * 0.80
        endy = size.get("height") * 0.20
        startx = size.get("width") / 2
        time.sleep(1)
        self.driver.swipe(startx, starty, startx, endy, 6000)
        size = self.driver.get_window_size()
        starty = size.get("height") * 0.80
        endy = size.get("height") * 0.20
        startx = size.get("width") / 2
        time.sleep(1)
        self.driver.swipe(startx, starty, startx, endy, 6000)

        # /html/body/div[2]/main/section[4]/div
        el31 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/main/section[4]/div"
        )
        assert el31.get_attribute("class") == "coporate_content__detail"
        time.sleep(1)

        # "CORPORATE"
        el32 = self.driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/main/section[4]/div/p"
        )
        time.sleep(1)
        assert el32.text == "CORPORATE"

        el33 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[1]/tbody/tr[1]/th",
        )
        time.sleep(1)
        assert el33.text == "社名"
        el34 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[1]/tbody/tr[1]/td",
        )
        time.sleep(1)
        assert el34.text == "ヘルスケアテクノロジーズ株式会社\nHEALTHCARE TECHNOLOGIES Corp."
        el35 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[1]/tbody/tr[2]/th",
        )
        time.sleep(1)
        assert el35.text == "所在地"
        el36 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[1]/tbody/tr[2]/td",
        )
        time.sleep(1)
        assert el36.text == "〒105-0014　東京都港区芝 2-28-8"
        el37 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[1]/tbody/tr[3]/th",
        )
        time.sleep(1)
        assert el37.text == "代表取締役"
        el38 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[1]/tbody/tr[3]/td",
        )
        time.sleep(1)
        assert el38.text == "代表取締役社長 兼 CEO 大石 怜史"
        el39 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[2]/tbody/tr[1]/th",
        )
        time.sleep(1)
        assert el39.text == "設立"
        el310 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[2]/tbody/tr[1]/td",
        )
        time.sleep(1)
        assert el310.text == "2018年10月15日"
        el311 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[2]/tbody/tr[2]/th",
        )
        time.sleep(1)
        assert el311.text == "事業内容"
        el312 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[2]/tbody/tr[2]/td",
        )
        time.sleep(1)
        assert el312.text == "オンラインヘルスケア事業"
        el313 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[2]/tbody/tr[3]/th",
        )
        time.sleep(1)
        assert el313.text == "資本金"

        # 38億5000万円（資本準備金含む
        el314 = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/main/section[4]/div/div/table[2]/tbody/tr[3]/td",
        )
        assert el314.text == "38億5000万円（資本準備金含む）"
        time.sleep(1)

