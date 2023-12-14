# blog/tests/factories.py
import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from ..models import Post


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    content = factory.Faker('text')
    author = factory.SubFactory(UserFactory)
