from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from courier.views import Home, CourierDayCreateView, CourierDayView, UpdateCourierDay, DeleteCourierDay
from courier.models import CourierDay, User, FacilityPackages, Facility


class TestUrls(SimpleTestCase):

    # Testy sprawdzające czy url o danej nazwie rozwiązuje się do odpowiedniej klasy widoku.
    def test_home_url_resolves(self):
        url = reverse('home')
        # Funkcja reverse generuje URL dla widoku o nazwie 'home'
        # print(resolve(url))
        # Print informacji o widoku home. Można dodać żeby mieć podgląd w terminalu
        self.assertEquals(resolve(url).func.view_class, Home)
        # Sprawdza czy URL o nizwie 'home' rozwiązuje się do klasy widoku Home

    def test_courierday_url_resolves(self):
        url = reverse('courier_day_view')
        self.assertEquals(resolve(url).func.view_class, CourierDayView)

    def test_form_url_resolves(self):
        url = reverse('add_day_form')
        self.assertEquals(resolve(url).func.view_class, CourierDayCreateView)

    def test_update_url_resolves(self):
        # ten URL poza ścieżką przyjmuje też argument w postaci klucza głownego
        url = reverse('update', args=[1])
        self.assertEquals(resolve(url).func.view_class, UpdateCourierDay)

    def test_delete_url_resolves(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteCourierDay)


class TestHomeView(TestCase):

    def setUp(self):
        self.client = Client()
        # tworzy 'atrapę' klienta przeglądarki i jego zapytań http

        self.home_url = reverse('home')

    def test_Home_GET(self):
        # response to klient(przeglądarka) pobierająca url 'home'
        response = self.client.get(self.home_url)

        # Zwraca kod HTTP 200(OK), upewnia się czy nie ma kodu 404(Not Found),
        # czy odsyła do odpowiedniego pliku html
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

        self.assertNotEquals(response.status_code, 404)


# Testy dla widoku listy Dni
class TestCourierDayView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_CourierDayView_GET_unlogged(self):
        response = self.client.get(reverse('courier_day_view'))

        # zwraca kod HTTP 302(przekierowanie do strony logowania)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, expected_url='/login/?next=/courierday/')

    def test_CourierDayView_GET_logged(self):
        # Tworzy i loguje użytkownika dla widoków z LoginRequiredMixin żeby nie dostać kodu przekierowania (302)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('courier_day_view'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'courier_day_view.html')


# Testy dla widoku z formularzem
class CourierDayCreateViewTest(TestCase):

    def test_CourierDayCreateView_GET_unlogged(self):
        response = self.client.get(reverse('add_day_form'))

        # zwraca kod HTTP 302(przekierowanie do strony logowania)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, expected_url='/login/?next=/form/')



    def test_CourierDayCreateView_POST(self):
        # Tworzy i loguje użytkownika żeby uniknąć przekierowania na stronę logowania
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Tworzy instancje modeli połączonych kluczami obcymi z modelem CourierDay
        facility = Facility.objects.create(name='Test Facility')
        facility_packages = FacilityPackages.objects.create(date='2023-01-01', packages=10, facility=facility)

        courier_day_1 = {
            'user': user.pk,
            'packages': facility_packages.pk,
            'addresses': 40,
            'machine': 80,
            'stops_end': '12:00',
            'pickup_end': '13:00',
        }

        response = self.client.post(reverse('add_day_form'), data=courier_day_1)

        # Przekierowuje do widoku courier_day_view
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('courier_day_view'))

    def test_CourierDayCreateView_POST_noData(self):

        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Formularz przesłany bez danych
        courier_day_1 = {}

        response = self.client.post(reverse('add_day_form'), data=courier_day_1)

        # Nie podaje pustych danych i nie przekierowuje na successurl,
        # przeładowuje ponownie stronę folmularza
        self.assertEqual(response.status_code, 200)


class UpdateCourierDayViewTest(TestCase):
    def setUp(self):
        # Tworzy użytkownika
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Tworzy instancje Facility i FacilityPackages
        self.facility = Facility.objects.create(name='Test Facility')
        self.facility_packages = FacilityPackages.objects.create(
            date='2023-11-01',
            packages=10,
            facility=self.facility
        )

        # Tworzy instancję CourierDay
        self.courier_day = CourierDay.objects.create(
            user=self.user,
            packages=self.facility_packages,
            addresses=45,
            machine=80,
            stops_end='13:00',
            pickup_end='14:00'
        )

    def test_UpdateCourierDayCreateView_GET_unlogged(self):
        response = self.client.get(reverse('update', args=[self.courier_day.pk]))
        self.assertEqual(response.status_code, 302)



# Testy dla Modelu CourierView
class CourierDayModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.facility = Facility.objects.create(name='Test Facility')
        self.facility_packages = FacilityPackages.objects.create(
            date='2023-11-01',
            packages=10000,
            facility=self.facility
        )
        self.courier_day = CourierDay.objects.create(
            user=self.user,
            packages=self.facility_packages,
            addresses=45,
            machine=100,
            stops_end='13:00:00',
            pickup_end='14:00:00'
        )

    # Testuje czy metoda str będzie zwracać poprawnego stringa
    def test_CourierDay_str_method(self):
        self.assertEqual(str(self.courier_day), '2023-11-01')

    # Testuje poprawną zalezność pomiędzy kluczami obcymi modeli
    def test_CourierDay_user_relationship(self):
        self.assertEqual(self.courier_day.user, self.user)

    def test_CourierDay_facility_packages_relationship(self):
        self.assertEqual(self.courier_day.packages, self.facility_packages)

    def test_CourierDay_fields(self):
        self.assertEqual(self.courier_day.addresses, 45)
        self.assertEqual(self.courier_day.machine, 100)
        self.assertEqual(self.courier_day.stops_end, '13:00:00')
        self.assertEqual(self.courier_day.pickup_end, '14:00:00')


# Testy do Modelu Facility
class FacilityModelTest(TestCase):
    def setUp(self):
        self.facility = Facility.objects.create(name='Test Facility')

    def test_Facility_str_method(self):
        self.assertEqual(str(self.facility), 'Test Facility')

    def test_Facility_name_field(self):
        self.assertEqual(self.facility.name, 'Test Facility')


# Testy dla modelu FaclilityPackages
class FacilityPackagesModelTest(TestCase):

    def setUp(self):
        self.facility = Facility.objects.create(name='Test Facility')
        self.facility_packages = FacilityPackages.objects.create(
            date='2023-11-01',
            packages=10000,
            facility=self.facility
        )

    def test_FacilityPackages_str_method(self):
        self.assertEqual(str(self.facility_packages), '2023-11-01 Test Facility')

    def test_FacilityPackages_relationship(self):
        self.assertEqual(self.facility_packages.facility, self.facility)

    def test_FacilityPackages_fields(self):
        self.assertEqual(self.facility_packages.date, '2023-11-01')
        self.assertEqual(self.facility_packages.packages, 10000)
