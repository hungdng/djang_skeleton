from rest_framework.renderers import JSONRenderer
import re

def underscoreToCamel(match):
    return match.group()[0] + match.group()[2].upper()

def camelize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = re.sub(r"[a-z]_[a-z]", underscoreToCamel, key)
            new_dict[new_key] = camelize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        for i in range(len(data)):
            data[i] = camelize(data[i])
        return data
    return data

class CamelCaseJSONRenderer(JSONRenderer):

    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(camelize(data), *args, **kwargs)