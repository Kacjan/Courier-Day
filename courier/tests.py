from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from courier.views import Home, CourierDayCreateView, CourierDayView, UpdateCourierDay, DeleteCourierDay
from courier.models import CourierDay, User, FacilityPackages

from datetime import date
class TestUrls(SimpleTestCase):

# Testy sprawdzające czy url o danej nazwie rozwiązuje się do odpowiedniej klasy widoku.
    def test_home_url_resolves(self):
        url = reverse('home')
        # Funkcja reverse generuje URL dla widoku o nazwie 'home'
        # print(resolve(url))
        # Print informacji o widoku home. Można dodać żeby mieć podgląd w terminalu
        self.assertEquals(resolve(url).func.view_class, Home)
        #Sprawdza czy URL o nizwie 'home' rozwiązuje się do klasy widoku Home


    def test_courierday_url_resolves(self):
        url = reverse('courier_day_view')
        self.assertEquals(resolve(url).func.view_class, CourierDayView)

    def test_form_url_resolves(self):
        url = reverse('add_day_form')
        self.assertEquals(resolve(url).func.view_class, CourierDayCreateView)

    def test_update_url_resolves(self):
        url = reverse('update', args=['some-key'])
        self.assertEquals(resolve(url).func.view_class, UpdateCourierDay)

    def test_delete_url_resolves(self):
        url = reverse('delete', args=['some-key'])
        self.assertEquals(resolve(url).func.view_class, DeleteCourierDay)


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        # tworzy 'atrapę' klienta przeglądarki i jego zapytań http

        self.home_url = reverse('home')
        self.CourierDayCreateView_url = reverse('add_day_form')


        # Tworzy i loguje użytkownika dla widoków z LoginRequiredMixin żeby nie dostać kodu przekierowania (302)
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        '''PROBLEM Z FORIEGN KEY I DATETIME
        ZRÓB INNE TESTY A PÓŹNIEJ WRÓC DO TEGO'''

        self.packages1 = FacilityPackages.objects.create(date='2000-01-01', packages=10000)
        self.day1 = CourierDay.objects.create(
            user = self.user,
            packages = self.packages1,
            addresses = 50,
            machine = 100,
            stops_end= 13,
            pickup_end= 15,)

    def test_Home_GET(self):
        #response to klient(przeglądarka) pobierająca url 'home'
        response = self.client.get(self.home_url)

        # Zwraca kod HTTP 200(OK), upewnia się czy nie ma kodu 404(Not Found),
        # czy odsyła do odpowiedniego pliku html
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertNotEquals(response.status_code, 404)


    def test_CourierDayView_GET(self):

        response = self.client.get(reverse('courier_day_view'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'courier_day_view.html')

    def test_CourierDayCreateView_GET(self):
        response = self.client.get(self.CourierDayCreateView_url)

        print()
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_day.html')








