from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
from ..models import Cheese
from faker import Faker
from everycheese.users.tests.factories import UserFactory

import pytest

class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3)
    country_of_origin = factory.Faker('country_code')
    creator = factory.SubFactory(UserFactory)
    #firmness = factory.fuzzy.FuzzyChoice([x[0] for x in Cheese.Firmness.choices])
    
class Meta:
    model = Cheese

@pytest.fixture
def cheese():
    return CheeseFactory()
  