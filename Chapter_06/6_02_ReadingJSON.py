import json

share_data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(share_data)
print(json_str)

python_data = {
    'a': True,  # true
    'b': 'Hello',
    'c': None,  # null
    'd': False,  # false
}
python_json_str = json.dumps(python_data)
print(python_json_str)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


share_obj = json.loads(json_str, object_hook=JSONObject)
print(share_obj.name)
print(share_obj.shares)
print(share_obj.price)


class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y


classes = {'Point': Point}


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}  # Create a dictionary with a single element __classname
    d.update(vars(obj))
    return d


def unserialize_object(dic):
    clsname = dic.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Create an object but bypass the __init__
        for key, value in dic.items():
            setattr(obj, key, value)
        return obj
    else:
        return dic


p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s)

a = json.loads(s, object_hook=unserialize_object)
print(a)
print(a.x)
print(a.y)
