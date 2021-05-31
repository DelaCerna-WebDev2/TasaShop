from django.test import TestCase
from django.urls import resolve
from MShop.views import MainPage

class HomePageTest(TestCase):
	
	def test_root_url_resolve(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)
