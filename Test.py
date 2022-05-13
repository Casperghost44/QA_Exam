import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class RedirectionTest(unittest.TestCase):
    ###RedirectionTest###
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://the-internet.herokuapp.com/redirector"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)


    def test_Redirection(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)

        click_elem = driver.find_element(By.ID, "redirect")
        self.assertTrue(click_elem)
        time.sleep(2)
        click_elem.click()
        driver.save_screenshot("Status_codes.png")
        time.sleep(2)
        click_elem_200 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[1]/a")
        self.assertTrue(click_elem_200)
        time.sleep(2)
        click_elem_200.click()
        time.sleep(2)
        driver.save_screenshot("200.png")
        back_elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p/a")
        self.assertTrue(back_elem)
        time.sleep(2)
        back_elem.click()
        time.sleep(2)

        click_elem_301 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[2]/a")
        self.assertTrue(click_elem_301)
        time.sleep(2)
        click_elem_301.click()
        time.sleep(2)
        driver.save_screenshot("301.png")
        back_elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p/a")
        self.assertTrue(back_elem)
        time.sleep(2)
        back_elem.click()
        time.sleep(2)

        click_elem_404 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[3]/a")
        self.assertTrue(click_elem_404)
        time.sleep(2)
        click_elem_404.click()
        time.sleep(2)
        driver.save_screenshot("404.png")
        back_elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p/a")
        self.assertTrue(back_elem)
        time.sleep(2)
        back_elem.click()
        time.sleep(2)

        click_elem_500 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[4]/a")
        self.assertTrue(click_elem_500)
        time.sleep(2)
        click_elem_500.click()
        time.sleep(2)
        driver.save_screenshot("500.png")
        back_elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p/a")
        self.assertTrue(back_elem)
        time.sleep(2)
        back_elem.click()
        time.sleep(2)

        click_detail_page = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p[1]/a")
        self.assertTrue(click_detail_page)
        time.sleep(2)
        click_detail_page.click()
        time.sleep(2)
        driver.save_screenshot("Detail_Page.png")
        time.sleep(2)







    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()