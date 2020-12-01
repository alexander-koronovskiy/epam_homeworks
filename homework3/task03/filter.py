# I decided to write a code that generates data filtering object
# from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []

    for key, value in keywords.items():

        def keyword_filter_func(value):
            return value[key] == value

        filter_funcs.append(keyword_filter_func)
    return filter_funcs  # Filter


# should return only second entry from the list
print(make_filter(name="polly", type="bird"))  # apply
