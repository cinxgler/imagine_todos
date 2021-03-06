from datetime import timedelta, timezone
from random import randint, uniform

import factory
from factory import LazyAttribute, LazyFunction, SubFactory, fuzzy
from factory.django import DjangoModelFactory
from faker import Factory

from demo.models import Todo

faker = Factory.create()


class TodoFactory(DjangoModelFactory):
    class Meta:
        model = Todo
        django_get_or_create = ('id',)

    id = LazyAttribute(lambda o: randint(0, 10000))
    date = LazyAttribute(lambda o: faker.date_time(tzinfo=timezone(timedelta(0))).isoformat())
    text = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    done = LazyFunction(faker.boolean)
