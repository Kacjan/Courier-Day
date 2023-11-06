from django.test import SimpleTestCase
from django.urls import reverse, resolve
from courier.views import Home, CourierDayCreateView
class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Home)