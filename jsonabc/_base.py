from abc import ABCMeta


def _convert_key_name(key):
    return key.replace("-", "_").lower()


class JSONABC(ABCMeta):
    def __new__(cls, name, bases, attrs):
        def __init__(self, data):
            schema = self.__annotations__.copy()
            for key, value in data.items():
                attr_name = _convert_key_name(key)
                
                if attr_name in schema:
                    if type(schema[attr_name]) is JSONABC:
                        setattr(self, attr_name, schema[key](value))
                        del schema[attr_name]
                    elif isinstance(value, schema[attr_name]):
                        setattr(self, attr_name, value)
                        del schema[attr_name]
                    else:
                        raise TypeError(f"Expected {schema[key]}, got {type(value)}")
            if schema :
                missing = [f"{key} ({value})" for key, value in schema.items()]
                raise TypeError(f"Missing: {missing}")

        def json(self, rename=lambda k: k):
            d =  self.__dict__
            for key, value in d.items():
                new_key = rename(key)
                if isinstance(type(value),JSONABC):
                    d[new_key] = value.json()
                    del d[key]
            return d        
        
        attrs["__init__"] = __init__
        attrs["json"] = json
        
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
    


