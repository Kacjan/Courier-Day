from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from courier.views import Home, CourierDayCreateView, CourierDayListView, UpdateCourierDay, DeleteCourierDay
from courier.models import CourierDay
class TestUrls(SimpleTestCase):


    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Home)

    def test_courierday_url_resolves(self):
        url = reverse('courier_day_list_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CourierDayListView)

    def test_form_url_resolves(self):
        url = reverse('add_day_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CourierDayCreateView)

    def test_update_url_resolves(self):
        url = reverse('update', args=['some-key'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UpdateCourierDay)

    def test_delete_url_resolves(self):
        url = reverse('delete', args=['some-key'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, DeleteCourierDay)


class TestViews(TestCase):

    def setUp(self):

        """tworzy symulację klienta przeglądarki i jego zapytań http"""
        self.client = Client()
        self.home_url = reverse('home')
        self.test_CourierDayCreateView =reverse('')


    def test_Home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertNotEquals(response.status_code, 404)

    def test_CourierDayCreateView_GET(self):



    # def test_CourierDayCreateView_POST(self):
    #     CourierDay.objects.create(
    #         user=
    #     )





