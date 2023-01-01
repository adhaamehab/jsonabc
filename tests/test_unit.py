
from jsonabc import JSONABC


class Person(metaclass=JSONABC):
    name: str
    age: int
    address: str


def test_simple():
    data = {"name": "John", "age": 30, "address": "123 Main St"}
    person = Person(data)
    assert person.name == "John"
    assert person.age == 30
    assert person.address == "123 Main St"
    assert person.json() == data

