# Courier Day
A simple online application designed to help archive and view information on the amount of work of a courier.
When looking for a topic for my first Django project, I wanted to create something original and practical.
I work as a courier, and I wanted to create a convenient way to prepare statistics and compare the amount of work for the next day based on the forecast number of parcels in the facility.


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Kacjan/final_project.git
$ cd sample-django-app
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

# Features


