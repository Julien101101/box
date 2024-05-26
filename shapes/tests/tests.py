from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.

class ShapesViewTest(SimpleTestCase):

    def test_home_status_code(self):
        response = self.client.get('/shapes/')  # Simulate GET request
        self.assertEqual(response.status_code, 200)  # Assert status code is 200 (OK
