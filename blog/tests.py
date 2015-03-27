from django.test import TestCase
from blog.models import *

class BlogTestCase(TestCase):
	def setUp(self):
		pass
		#Blog.objects.create()
		#try slug double unique TODO