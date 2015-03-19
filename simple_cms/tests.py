from django.test import TestCase
from simple_cms.models import *

class ImageTestCase(TestCase):
    def setUp(self):
        Image.objects.create(name="qwertasdfzxcvbnmlkja", caption="Test clause written in pain and anger.")
        Image.objects.create(name="test2", caption="Is this true?")

    def captionTest(self):
        qwerty = Image.objects.get(name="qwertasdfzxcvbnmlkja")
        test2 = Image.objects.get(name="test2")
        self.assertEqual(qwerty.caption, "Test clause written in pain and anger.")
        self.assertEqual(test2.caption, "Is this true?")