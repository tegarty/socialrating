import factory
from faker import Faker
import random

from .models import Actor, User
from django.contrib.auth.hashers import make_password

fake = Faker()


def generate_username(*args):
    return fake.profile(fields=['username'])['username'] + str(random.randint(1,99999))


def generate_password(*args):
    """
    Generate a random password and run the Django make_password function on it and return the result
    """
    pw = fake.password()
    return make_password(pw)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(generate_username)
    #password = factory.LazyAttribute(generate_password)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

