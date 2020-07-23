import pytest
# Connects our tests with our database
from ..models import Cheese
from .factories import CheeseFactory
pytestmark = pytest.mark.django_db
def test___str__():
    cheese = Cheese.objects.create(
    name="Stracchino",
    description="Semi-sweet cheese that goes well with starches.",)

    #cheese = CheeseFactory(name="Stracchino")
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"


def test_get_absolute_url():
    cheese = Cheese.objects.create(
    name="Stracchino",
    description="Semi-sweet cheese that goes well with starches.",)
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'