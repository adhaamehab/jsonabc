# JSONABC

> Json Abstract Base Class

JSONABC is a minimal, pythonic JSON to class serializer. It has __zero__ dependencies which makes it very lightweight. It provide a very minimal API with few options and play nicely with python type checking.


## Install
```shell
pip install jsonabc
```

## Examples

__example 1 (simple)__

```python
from jsonabc import JSONABC

# All you need to do is define JSONABC as your metaclass
class Response(metaclass=JSONABC):
    args: dict
    headers: dict
    origin: str
    url: str

resp = requests.get("https://httpbin.org/get")
json_data = resp.json()

# Your class can now take a single dict and automatically validate and parse it.
obj = Response(response)

# obj attributes now have their correspondent values from our json data.
# you can also convert your class back to its json form.
# JSONABC will preserve the same names for the original json and converge to it.
print(obj.json())

```

__example 2 (composite)__
```python
from jsonabc import JSONABC

# You can also define composite values instead of using dicts
class Headers(metaclass=JSONABC):
    accept: str
    accept_encoding: str

class Response(metaclass=JSONABC):
    args: dict
    headers: Headers
    origin: str
    url: str

resp = requests.get("https://httpbin.org/get")
json_data = resp.json()

obj = Response(response)

# headers attr is now an instance of Headers with the same behavior as Response
obj.headers 

```