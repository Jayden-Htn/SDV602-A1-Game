import types
_health_value: int = 1000


def get():
    return _health_value


def reduce(pValue):
    global _health_value
    _health_value -= pValue


def increase(pValue):
    global _health_value
    _health_value += pValue
