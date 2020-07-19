import pytest
# Connects our tests with our database
from ..models import Cheese
pytestmark = pytest.mark.django_db
def test___str__():
    cheese = Cheese.objects.create(
    name="Stracchino",
    description="Semi-sweet cheese that goes well with starches.",)
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"