from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

Wait = 3
class BrowserTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def wait_cart_in_carttable(self, row_text):
		start_time = time.time()
		while time.time()-start_time<Wait:
			time.sleep(0.2)
			try:
				table = self.browser.find_element_by_id('carttable')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as error:
				if time.time()-start_time>Wait:
					raise error

	def  test_startinglist_and_retrievinglist(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Mug Shop', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Mug Shop', headerText)

		inputclient = self.browser.find_element_by_id('client')
		inputclient.click()
		# time.sleep(1)
		inputclient.send_keys('Jal Dela Cerna')
		time.sleep(.1)
		inputaddress = self.browser.find_element_by_id('address')
		inputaddress.click()
		# time.sleep(1)
		inputaddress.send_keys('blk 11 l 11 brgy Eleven, evelen City')
		time.sleep(1)
		# btnOK = self.browser.find_element_by_id('btnOK')
		# btnOK.click()
		
		# with design form
		# second input
		select1= self.browser.find_element_by_id('design')
		SelectDesign = select1.find_element_by_tag_name('option')
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		time.sleep(.1)
		Quanti1 = self.browser.find_element_by_id('Dquan')
		Quanti1.send_keys('5')
		Daddtocart = self.browser.find_element_by_id('Daddtocart')
		Daddtocart.click()
		time.sleep(.1)
		self.wait_cart_in_carttable('1: DESIGN NO.5')  #QUANTITY: 5
		# second input
		select1= self.browser.find_element_by_id('design')
		SelectDesign = select1.find_element_by_tag_name('option')
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		SelectDesign.send_keys(Keys.ARROW_DOWN)
		Quanti1 = self.browser.find_element_by_id('Dquan')
		Quanti1.send_keys('7')
		time.sleep(.1)
		Daddtocart = self.browser.find_element_by_id("Daddtocart")
		Daddtocart.click()
		self.wait_cart_in_carttable("2: DESIGN NO.3")