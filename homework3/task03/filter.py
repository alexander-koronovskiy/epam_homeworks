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


def foo(x):
    return x ** 2 == 36


def foo_first(a):
    return a % 2 == 0


Filter(foo(5))
sample_usage = Filter(foo_first, foo)
print(sample_usage.apply(data=range(10)))


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(value):
            return value[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

# make_filter(name='polly', type='bird').apply(sample_data)
# should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
