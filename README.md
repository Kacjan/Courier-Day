# Courier Day
A simple online application designed to help archive and view information on the amount of work of a courier.
When looking for a topic for my first Django project, I wanted to create something original and practical.
I work as a courier, and I wanted to create a convenient way to prepare statistics and compare the amount of work for the next day based on the forecast number of parcels in the facility.


## Main features

* Separated applications: for main content and users

* Registration, login, profile, and password change for users

* List of work days with 6 columns of data : Date, Facility packages, Addresses, Machine, End hour of deliveries, End hour of pick-ups

* Filtering form for a displayed number of workdays

* Form for adding new workdays

* Separated requirements files

* SQLite3 database

## Built With

* [![Python][Python.com]][Python-url]
* [![Django][Django.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

## Setup

1. Create a PyCharm project with the virtual environment

2. Clone the repository:

```sh
$ git clone https://github.com/Kacjan/Courier-Day.git
$ cd Courier-Day
```

3. Install the dependencies:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
$ python manage.py runserver
```

if it doesn't work make sure you are in the Courier-Day folder ($ cd Courier-Day)

And navigate to `http://127.0.0.1:8000`.

## Usage

Admin must add a list of facilities to the database by admin panel.
Then he can add new days with a number of facility packages.

Unlogged users can only view home, register, and login sites.

New users can register by filling register form.

Then the Admin must assign the new user to the existing facility, without this user won't be able to add a new day to his list.

Logged users can view home, courier day list, profile and logout links.

Profile site contains information about his user name, assigned facility, and link to password change form.

Courier day site contains:
- List of courier days
- Link to form adding a new day
- Form filtering list by start and end date
- Button updating chosen day
- Button deleting chosen day

Day adding form contains 5 fields

Date(Data) - linked to the day date and number of packages in the users facility on said day.
Addresses(Adresy) - Number of addresses the courier must visit that day to deliver packages.
Machine(Paczkomat) - Number of packages the courier must deliver to parcel pickup stations.
Address end(Koniec adresów) - Time of the last delivery.
Pickup end(Koniec zbiorów) - Time of the last pickup.

For new users without an assigned facility field Date will be disabled.
User is able to pick up Date only from the facility assigned to them.


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Django.com]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Bootstrap.com]: https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
