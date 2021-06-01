from django.test import TestCase
from django.contrib.staticfiles import finders
from MShop.models import Customer, Product, Order, Cart, Shipping

class HomePageTest(TestCase):

	def test_mainpage_return_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')

class StaticFile(TestCase):
	
	def test_static_file(self):
		static_file = finders.find('CSS/style.css')
		self.assertEqual(static_file, style)